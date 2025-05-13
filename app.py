from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector
import re
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import openai
import os
from typing import List, Dict, Tuple, Optional, Any
import csv
import io
from pydantic import BaseModel
import uuid
import time
from serpapi import GoogleSearch
from schema import TABLE_SCHEMAS
from identifier import identify_relevant_tables

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

# Initialize FastAPI app
app = FastAPI(title="AI SQL Query Generator with Analytics")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates configuration
templates = Jinja2Templates(directory="templates")

# Initialize embeddings and vector stores
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize schema vector store
schema_documents = []
for table_name, table_info in TABLE_SCHEMAS.items():
    # Create document with table metadata
    doc_content = f"Table: {table_name}\nDescription: {table_info['description']}\nColumns:"
    for col, col_desc in table_info['columns'].items():
        doc_content += f"\n- {col}: {col_desc}"
    
    schema_documents.append(Document(
        page_content=doc_content,
        metadata={
            "table_name": table_name,
            "description": table_info['description'],
            "columns": list(table_info['columns'].keys())
        }
    ))

# Split documents into chunks for better retrieval
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)
schema_docs = text_splitter.split_documents(schema_documents)

# Create FAISS vector store for schema
schema_vectorstore = FAISS.from_documents(schema_docs, embedding)

# Initialize general vector store for context
general_vectorstore = FAISS.load_local("C:/echatbot/vectorstore", embedding, allow_dangerous_deserialization=True)

# Initialize retrievers
schema_retriever = schema_vectorstore.as_retriever(search_kwargs={"k": 5})
general_retriever = general_vectorstore.as_retriever()

# Initialize OpenAI client
openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Cache for query results
query_cache = {}

# Enhanced greeting responses with more variety
def get_greeting_response(question: str) -> str:
    """Generate dynamic greeting response with important keywords using LLM"""
    prompt = f"""
You are Bihar's Data Bot created by Harsh. Respond to the greeting in a warm, professional manner while incorporating these key elements:
- Mention you're Bihar's Data Bot created by Harsh
- Highlight you specialize in Bihar-related data
- Keep response concise (1-2 sentences)
- Maintain a friendly tone
- Include relevant emoji if appropriate

Example good responses:
"Namaste! I'm Bihar's Data Bot created by Harsh, ready to assist you with Bihar's statistics and development data. 😊"
"Hello there! I'm your Bihar data specialist bot developed by Harsh. Ask me anything about Bihar's progress and metrics!"

User greeting: "{question}"

Response:
"""
    try:
        response = openai_client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a friendly greeting bot for Bihar data."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return "Hello! I'm Bihar's Data Bot created by Harsh. How can I assist you with Bihar-related data today?"

def is_greeting(question: str) -> bool:
    """Check if the question is a greeting"""
    lower_question = question.lower().strip()
    
    # List of greeting patterns
    greeting_patterns = [
        r'^hi\b', r'^hello\b', r'^hey\b', 
        r'good morning', r'good afternoon', r'good evening',
        r'how are you', r"what's up", r'namaste', 
        r'hi bot', r'hello there', r'greetings',
        r'^bye\b', r'good night', r'see you',
        r'thank you', r'thanks' , r'who made you' , r'tell me about'
    ]
    
    # Check against patterns
    for pattern in greeting_patterns:
        if re.search(pattern, lower_question):
            return True
    
    return False

class QueryRequest(BaseModel):
    question: str

class QueryResult(BaseModel):
    query_id: str
    question: str
    sql_query: str
    process_log: List[str]
    answer: str
    data: Optional[List[Dict]]
    columns: Optional[List[str]]
    status: str
    timestamp: float
    visualization_type: Optional[str] = None
    is_bihar_map: bool = False
    is_external_data: bool = False
    question_type: Optional[str] = None

@app.on_event("startup")
async def startup_event():
    """Initialize application state"""
    # Fetch schema information
    global schema, actual_table_names, district_related_tables
    schema = fetch_schema_info()
    actual_table_names = list(schema.keys())
    district_related_tables = identify_district_tables(schema, actual_table_names)

def fetch_schema_info() -> Dict[str, List[Tuple[str, str]]]:
    """Fetch schema information with case-sensitive table names"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = %s
        """, (DB_CONFIG['database'],))
        tables = [row[0] for row in cursor.fetchall()]
        
        schema = {}
        for table in tables:
            cursor.execute(f"""
                SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_schema = %s AND table_name = %s
                ORDER BY ordinal_position
            """, (DB_CONFIG['database'], table))
            schema[table] = cursor.fetchall()
        
        return schema
    except Exception as e:
        print(f"Failed to fetch schema: {str(e)}")
        return {}
    finally:
        cursor.close()
        conn.close()

def identify_district_tables(schema: Dict, table_names: List[str]) -> List[str]:
    """Identify tables containing district information"""
    district_tables = []
    for table in table_names:
        if "district" in table.lower():
            district_tables.append(table)
        else:
            # Check if table has district-related columns
            columns = [col[0].lower() for col in schema[table]]
            if "district_name" in columns or "district" in columns:
                district_tables.append(table)
    return district_tables

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the main page"""
    return templates.TemplateResponse("index.html", {"request": request})

def is_greeting(question: str) -> bool:
    """Check if the question is a greeting"""
    lower_question = question.lower().strip()
    
    # List of greeting patterns
    greeting_patterns = [
        r'^hi\b', r'^hello\b', r'^hey\b', 
        r'good morning', r'good afternoon', r'good evening',
        r'how are you', r"what's up", r'namaste', 
        r'hi bot', r'hello there', r'greetings',
        r'^bye\b', r'good night', r'see you',
        r'thank you', r'thanks'
    ]
    
    # Check against patterns
    for pattern in greeting_patterns:
        if re.search(pattern, lower_question):
            return True
    
    return False

async def classify_question(question: str) -> str:
    """Classify the user's question into analytical, theoretical, or greeting"""
    # First check if it's a greeting
    if is_greeting(question):
        return "/greeting"
    
    # Use OpenAI to classify the question
    prompt = f"""
Analyze the following user question and classify it as either "analytical" or "theoretical" based on these detailed criteria:

ANALYTICAL QUESTIONS (Database-answerable):
These questions can be directly answered by querying the 250+ Bihar government tables. They typically:

1. Request specific numerical data:
   - Counts ("How many police stations in Patna district?")
   - Sums/Averages ("Total wheat production across Bihar in 2023")
   - Percentages ("What percentage of schools have toilets?")
   - Exact values ("Pension amount under JP Senani scheme")

2. Ask for filtered/sorted lists:
   - "List all blocks with >50% literacy rate"
   - "Show districts ordered by fire vehicle count"
   - "Schools without drinking water facilities"

3. Seek comparisons:
   - "Compare paddy procurement between 2022 and 2023"
   - "District with highest vs lowest crime rate"
   - "Gender-wise beneficiary counts for MMUY scheme"

4. Request geographical distributions:
   - "Police stations per district map"
   - "Block-wise distribution of irrigation schemes"
   - "Location of all fire hydrants in Muzaffarpur"

5. Ask about trends over time:
   - "Year-wise growth of smart city projects"
   - "Monthly grain allotment trends 2020-2025"
   - "Quarterly fertilizer stock changes"

6. Require simple joins/aggregations:
   - "Total beneficiaries by district and category"
   - "Average pension by age group and gender"
   - "Combine enrollment data with infrastructure metrics"

THEORETICAL QUESTIONS (Non-database):
These require knowledge beyond the structured data. They typically:

1. Ask "why" or "how" explanations:
   - "Why does Patna have more crime than Gaya?"
   - "How does the pension verification process work?"

2. Request policy analysis:
   - "Should the JP Senani scheme be expanded?"
   - "What's the impact of DBT on corruption?"

3. Seek subjective judgments:
   - "Which district has the best administration?"
   - "Are police stations adequately distributed?"

4. Ask about implementation:
   - "How to improve school infrastructure?"
   - "Steps to reduce land dispute cases"

5. Require external knowledge:
   - "Historical context of Bihar's irrigation systems"
   - "Comparison with other states' schemes"

6. Request predictions:
   - "Will wheat production increase next year?"
   - "Projected smart city completion dates"

DECISION TREE:
1. Does the question ask for specific numbers/values that exist in the tables? → ANALYTICAL
2. Can the answer be generated by filtering/sorting/joining tables? → ANALYTICAL
3. Does it require interpretation beyond the data? → THEORETICAL
4. Would answering require expert opinion or external sources? → THEORETICAL

EXAMPLES FROM YOUR SCHEMA:
Analytical:
- "District-wise count of artificial insemination centers"
- "Percentage of schools with functional handpumps by block"
- "Trend in paddy procurement amounts over last 5 years"
- "List of projects with <50% financial progress in Patna Smart City"

Theoretical:
- "Why are some districts performing better in crop yields?"
- "How effective is the prohibition policy in Bihar?"
- "Recommendations to improve farmer subsidy distribution"
- "Causes of gender disparity in pension schemes"

Question: "{question}"

Final determination: Respond ONLY with either "analytical" or "theoretical" based on the above criteria.
"""
    
    try:
        response = openai_client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a question classifier."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=10
        )
        classification = response.choices[0].message.content.strip().lower()
        return classification if classification in ["analytical", "theoretical"] else "theoretical"
    except Exception:
        return "theoretical"  # Default to theoretical if classification fails

def get_relevant_schema_chunks(user_input: str) -> List[Dict]:
    """Retrieve relevant schema chunks using RAG"""
    relevant_docs = schema_retriever.get_relevant_documents(user_input)
    
    schema_chunks = []
    for doc in relevant_docs:
        schema_chunks.append({
            "table_name": doc.metadata["table_name"],
            "description": doc.metadata["description"],
            "columns": doc.metadata["columns"],
            "content": doc.page_content
        })
    
    return schema_chunks

def get_relevant_context(query: str) -> str:
    """Get relevant context from general vector store"""
    docs = general_retriever.get_relevant_documents(query)
    return "\n".join([doc.page_content for doc in docs])

def normalize_years_in_question(question: str) -> List[str]:
    """Extract and normalize years mentioned in the question"""
    year_variants = set()
    single_years = re.findall(r'\b(20\d{2})\b', question)
    year_variants.update(single_years)

    ranges = re.findall(r'\b(20\d{2})\s*(?:to|-)\s*(20\d{2})\b', question)
    for start, end in ranges:
        for y in range(int(start), int(end) + 1):
            year_variants.add(str(y))
            year_variants.add(f"{y}-{str(y + 1)[2:]}")

    return list(year_variants)

def generate_sql_with_retrieved_schema(
    user_input: str, 
    relevant_tables: List[str], 
    query_history: List[Dict],
    last_table_used: Optional[str] = None,
    schema_chunks: List[Dict] = None
) -> str:
    """Generate SQL query using retrieved schema chunks to stay within token limits"""
    context = get_relevant_context(user_input)
    years = normalize_years_in_question(user_input)
    
    error_history = "\n".join(
        [f"Attempt {i+1} Error: {item['content']}" 
         for i, item in enumerate(query_history) 
         if item['type'] == 'error']
    ) if query_history else "No previous errors"
    
    # If we have a table from previous error and it's in relevant_tables, include its columns
    column_info = ""
    if last_table_used and last_table_used in relevant_tables:
        columns = [col[0] for col in schema[last_table_used]]
        column_info = f"\nACTUAL COLUMNS FOR {last_table_used}: {', '.join(columns)}"
    
    # Prepare schema information from retrieved chunks
    schema_info = []
    for chunk in schema_chunks:
        if chunk["table_name"] in relevant_tables:
            columns_desc = "\n".join([
                f"  - {col}: {TABLE_SCHEMAS[chunk['table_name']]['columns'].get(col, 'No description')}"
                for col in chunk["columns"]
            ])
            schema_info.append(
                f"Table: {chunk['table_name']}\n"
                f"Description: {chunk['description']}\n"
                f"Columns:\n{columns_desc}"
            )
    
    # Create the examples as a separate string
    examples = """
EXAMPLE QUERIES:
-- Simple district filter
SELECT district_name, police_station 
FROM Bihar_police_station 
WHERE district_name LIKE '%Patna%';

-- Aggregation with grouping
SELECT district_name, COUNT(*) as num_stations
FROM Bihar_police_station
GROUP BY district_name
ORDER BY num_stations DESC;

-- Complex analytical query with CTE
WITH district_stats AS (
  SELECT 
    district_name,
    SUM(CAST(COALESCE(NULLIF(cases_registered, ''), '0') AS DECIMAL(15,2))) as total_cases
  FROM prohibition_cases
  WHERE year = '2020'
  GROUP BY district_name
)
SELECT * FROM district_stats ORDER BY total_cases DESC;

-- Percentage calculation
SELECT 
  year,
  (SUM(CAST(COALESCE(NULLIF(achieved, ''), '0') AS DECIMAL(15,2))) / 
  SUM(CAST(COALESCE(NULLIF(target, ''), '0') AS DECIMAL(15,2)) * 100 as achievement_percentage
FROM production_data
GROUP BY year;

-- Multi-table join
SELECT 
  p.district_name,
  p.police_station,
  c.cases_registered
FROM Bihar_police_station p
JOIN consolidated_raids c ON p.district_name = c.district_name
WHERE p.district_name LIKE '%Patna%';
"""
    
    # Build the prompt in parts
    prompt_parts = [
        "You are an expert MySQL query writer specialized in statistical, analytical, and complex calculative queries for government data analysis. Generate precise SQL queries that handle:\n\n"
        "1. Multi-table joins with proper relationships\n"
        "2. Complex aggregations (SUM, COUNT, AVG, etc.)\n"
        "3. Comparative analysis between years/districts\n"
        "4. Trend analysis with proper grouping\n"
        "5. Percentage calculations and ratios\n"
        "6. Ranking queries (TOP N, HIGHEST/LOWEST)\n"
        "7. Conditional filtering for Bihar-specific data\n\n"
        f"RELEVANT TABLES FOR THIS QUERY:\n{', '.join(relevant_tables)}\n\n"
        f"TABLE SCHEMA INFORMATION:\n{'\\n\\n'.join(schema_info) if schema_info else 'No specific schema information available'}\n\n"
        f"{column_info}\n\n"
        f"PREVIOUS ERRORS (learn from these):\n{error_history}\n\n"
        "GUIDELINES:\n"
        "1. Always use the most specific table available for the query\n"
        "2. For Bihar-specific data, include 'state_name = \"Bihar\"' when relevant\n"
        "3. Return ONLY the pure SQL query, no explanations or commentary\n"
        "4. Handle NULL values with COALESCE(NULLIF(column, ''), '0') for numeric fields\n"
        "5. Include proper units in column aliases (e.g., 'total_liters', 'amount_in_rupees')\n"
        "6. For comparative queries, use CTEs (WITH clauses) when appropriate\n"
        "7. Always include relevant GROUP BY and ORDER BY clauses\n"
        "8. Use proper casting for numeric operations: CAST(COALESCE(NULLIF(column, ''), '0') AS DECIMAL(15,2))\n\n",
        examples,
        f"\nQuestion: {user_input}\n",
        f"Context: {context}\n",
        f"Years to consider: {', '.join(years) if years else 'All available years'}\n\n",
        "Generate a VALID SQL query following these rules:\n"
        "1. Always use COALESCE/NULLIF for numeric fields\n"
        "2. Include proper units in column aliases\n"
        "3. Use explicit JOIN syntax for multi-table queries\n"
        "4. Apply Bihar-specific filters when appropriate\n"
        "5. Include relevant GROUP BY and ORDER BY clauses\n\n"
        "SQL:"
    ]
    
    prompt = "".join(prompt_parts)
    
    try:
        response = openai_client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a SQL expert that generates valid MySQL queries."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )
        generated_sql = response.choices[0].message.content.strip()
        return clean_sql(generated_sql)
    except Exception as e:
        return f"Error generating SQL: {str(e)}"

def clean_sql(sql_query: str) -> str:
    """Clean the SQL query"""
    # Remove markdown code blocks if present
    clean_sql = re.sub(r'```sql|```', '', sql_query).strip()
    
    # Ensure query ends with semicolon
    if not clean_sql.endswith(';'):
        clean_sql += ';'
    
    return clean_sql

def execute_sql_query(sql_query: str) -> Dict:
    """Execute the SQL query and return results"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql_query)
        
        column_names = [col[0] for col in cursor.description] if cursor.description else []
        rows = cursor.fetchall()
        
        return {"columns": column_names, "data": rows}
    except mysql.connector.Error as err:
        return f"Database Error: {err}"
    finally:
        cursor.close()
        conn.close()

def generate_final_answer(
    user_question: str, 
    query_result: Dict, 
    visualization_type: Optional[str] = None,
    is_bihar_map: bool = False
) -> str:
    """Generate a natural language answer with strict formatting for frontend display"""
    
    if isinstance(query_result, str):
        return query_result

    if not query_result or not query_result["data"]:
        return "No matching records found in the Bihar government database."
    
    columns = query_result["columns"]
    data = query_result["data"]
    
    # Construct analysis prompt with strict formatting requirements
    analysis_prompt = f"""
Analyze this Bihar government data and provide an answer with STRICT FORMATTING for web display:

USER QUESTION: {user_question}

DATA SUMMARY:
- Records: {len(data)}
- Columns: {', '.join(columns)}
- Sample: {str(data[:1])}

FORMATTING RULES (MUST FOLLOW):
1. First line: Concise 1-sentence answer
2. Key points section:
   - Start with "Key Findings:" on new line
   - Each bullet point on its own line with "- " prefix
   - Max 5 bullet points
3. Trends section (if applicable):
   - Start with "**Trend:**" on new line
   - 1-2 sentences only
4. Visualization note (if applicable)
5. ENSURE:
   - Each bullet point is on a new line
   - No paragraphs for bullet points
   - Exactly one empty line between sections

EXAMPLE FORMAT:
Patna has the most police stations in Bihar.

Key Findings:
- Total police stations: 85
- Covers all 75 police subdivisions
- 24/7 surveillance in all stations
- Average response time: 8 minutes

**Trend:**
Police infrastructure has grown 15% annually since 2015.

[Map visualization available]

ACTUAL RESPONSE:
"""

    try:
        response = openai_client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": """You format Bihar government data responses with:
                - Strict line breaks for bullets
                - No paragraph-style bullets
                - Perfect section spacing"""},
                {"role": "user", "content": analysis_prompt}
            ],
            temperature=0.2,  # Very low temperature for consistent formatting
            max_tokens=500
        )
        
        raw_text = response.choices[0].message.content.strip()
        
        # Enforce formatting with regex
        import re
        
        # Ensure exactly one newline between sections
        formatted_text = re.sub(r'\n{3,}', '\n\n', raw_text)
        
        # Ensure bullets start with "- " and are on their own lines
        formatted_text = re.sub(
            r'^(\s*[•*]\s*)', 
            '- ', 
            formatted_text, 
            flags=re.MULTILINE
        )
        
        # Remove any bullet points that got merged into paragraphs
        formatted_text = re.sub(
            r'(- [^\n]+)([^\n-]+)(- [^\n]+)',
            r'\1\n\3',
            formatted_text
        )
        
        return formatted_text

    except Exception as e:
        return f"""We encountered an error processing your request.

**Technical Details:**
- Error: {str(e)}
- Suggestion: Please try rephrasing your query

[Our team has been notified]"""
        

def determine_visualization_type(columns: List[str], data: List[Dict]) -> Optional[str]:
    """Determine the best visualization type based on the data"""
    if not columns or not data:
        return None
    
    # Check if we have numeric data
    numeric_cols = []
    label_cols = []
    
    for col in columns:
        # Simple check for numeric data (in real app, use schema or sample data)
        if any(isinstance(row.get(col), (int, float)) for row in data):
            numeric_cols.append(col)
        else:
            label_cols.append(col)
    
    if not numeric_cols:
        return None
    
    # Simple rules for visualization type
    if len(numeric_cols) == 1 and len(label_cols) >= 1:
        if len(data) <= 10:
            return "pie"
        else:
            return "bar"
    elif len(numeric_cols) >= 2 and len(label_cols) >= 1:
        return "line"
    
    return None



def should_show_bihar_map(columns: List[str], data: List[Dict]) -> bool:
    """Determine if we should show a Bihar district map"""
    if not columns or not data:
        return False
    
    # Check if we have district information
    has_district = any(col.lower() in ["district", "district_name"] for col in columns)
    has_numeric = any(isinstance(data[0].get(col), (int, float)) for col in columns if col.lower() not in ["district", "district_name"])
    
    return has_district and has_numeric

def extract_table_from_query(sql_query: str) -> Optional[str]:
    """Extract the main table name from SQL query"""
    match = re.search(r'\bFROM\s+([a-zA-Z0-9_]+)', sql_query, re.IGNORECASE)
    if match:
        table_name = match.group(1)
        # Check if this is an alias (table name is before AS)
        if ' as ' in table_name.lower():
            table_name = table_name.split()[0]
        return table_name
    return None

def search_with_serpapi(question: str) -> str:
    """Search for information using SerpAPI when database doesn't have relevant data"""
    try:
        params = {
            "q": question,
            "hl": "en",
            "gl": "in",
            "api_key": SERPAPI_KEY
        }
        
        search = GoogleSearch(params)
        results = search.get_dict()
        
        # Extract relevant information from results
        answer = None
        
        if "answer_box" in results and "answer" in results["answer_box"]:
            answer = results["answer_box"]["answer"]
        elif "answer_box" in results and "snippet" in results["answer_box"]:
            answer = results["answer_box"]["snippet"]
        elif "organic_results" in results and len(results["organic_results"]) > 0:
            top_results = results["organic_results"][:3]
            snippets = [f"{res.get('title', '')}: {res.get('snippet', '')}" for res in top_results]
            answer = "\n\n".join(snippets)
        
        if answer:
            prompt = f"""
The user asked: "{question}"

Here are some search results I found:
{answer}

Please provide a concise, well-formatted answer to the user's question using this information.
Focus on the most relevant details and present them in a clear, professional manner.
Keep the response under 200 words.
"""
            response = openai_client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that summarizes search results."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=500
            )
            return response.choices[0].message.content.strip()
        
        return "I couldn't find any relevant information about that topic. Could you please rephrase your question or ask about something else?"
    
    except Exception as e:
        print(f"SerpAPI error: {str(e)}")
        return "I encountered an error while searching for information. Please try again later."

@app.post("/api/query", response_model=QueryResult)
async def process_query(query_request: QueryRequest):
    """Process user query and return results"""
    query_id = str(uuid.uuid4())
    user_input = query_request.question.strip()
    
    # Classify the question
    question_type = await classify_question(user_input)
    
    # Initialize query result
    query_result = QueryResult(
        query_id=query_id,
        question=user_input,
        sql_query="",
        process_log=[f"Question classified as: {question_type}"],
        answer="",
        data=None,
        columns=None,
        status="processing",
        timestamp=time.time(),
        is_external_data=False,
        question_type=question_type
    )
    
    # Store initial state in cache
    query_cache[query_id] = query_result.dict()
    
    # Process based on question type
    if question_type == "analytical":
        await process_analytical_question(query_id, user_input)
    elif question_type == "theoretical":
        await process_theoretical_question(query_id, user_input)
    elif question_type == "/greeting":
        greeting_response = get_greeting_response(user_input)
        query_result.answer = greeting_response
        query_result.status = "completed"
        query_cache[query_id] = query_result.dict()
    
    return query_result

async def process_analytical_question(query_id: str, user_input: str):
    """Process an analytical question that requires data querying"""
    query_result = QueryResult(**query_cache[query_id])
    query_result.process_log.append("Processing as analytical question")
    query_cache[query_id] = query_result.dict()
    
    max_retries = 3
    current_attempt = 0
    last_error = None
    last_table_used = None
    query_history = []
    
    while current_attempt < max_retries:
        current_attempt += 1
        query_result.process_log.append(f"Attempt {current_attempt}/{max_retries}...")
        query_cache[query_id] = query_result.dict()
        
        try:
            # Step 1: Identify relevant tables using keyword matching and RAG
            keyword_matched_tables = identify_relevant_tables(user_input, TABLE_SCHEMAS)
            schema_chunks = get_relevant_schema_chunks(user_input)
            rag_matched_tables = [chunk["table_name"] for chunk in schema_chunks]
            
            # Combine both methods and remove duplicates
            relevant_tables = list(set(keyword_matched_tables + rag_matched_tables))
            
            if not relevant_tables:
                query_result.process_log.append("No relevant tables found - switching to theoretical approach")
                query_result.question_type = "theoretical"
                await process_theoretical_question(query_id, user_input)
                return
                
            query_history.append({
                "type": "tables_selected", 
                "content": f"Selected tables: {', '.join(relevant_tables)}"
            })
            
            # Step 2: Generate SQL with retrieved schema chunks
            sql_query = generate_sql_with_retrieved_schema(
                user_input, 
                relevant_tables, 
                query_history,
                last_table_used,
                schema_chunks
            )
            
            query_history.append({"type": "generated", "content": sql_query})
            query_result.sql_query = sql_query
            query_result.process_log.append(f"Generated SQL:\n{sql_query}\n")
            query_cache[query_id] = query_result.dict()
            
            # Step 3: Execute SQL
            query_response = execute_sql_query(sql_query)
            
            if isinstance(query_response, str) and query_response.startswith("Database Error"):
                error_msg = query_response
                last_error = error_msg
                
                if "Unknown column" in error_msg:
                    table_name = extract_table_from_query(sql_query)
                    if table_name and table_name in actual_table_names:
                        last_table_used = table_name
                        raise ValueError(f"Column error detected. Will retry with correct columns for table {table_name}")
                
                raise ValueError(error_msg)
            
            # Step 4: Store query results
            query_result.data = query_response["data"]
            query_result.columns = query_response["columns"]
            query_result.process_log.append("Query executed successfully")
            
            if not query_result.data:
                query_result.process_log.append("No data found in database - switching to theoretical approach")
                query_result.question_type = "theoretical"
                await process_theoretical_question(query_id, user_input)
                return
            
            # Determine visualization type
            query_result.visualization_type = determine_visualization_type(
                query_result.columns,
                query_result.data
            )
            
            # Check if we should show Bihar map
            query_result.is_bihar_map = should_show_bihar_map(
                query_result.columns,
                query_result.data
            )
            
            query_cache[query_id] = query_result.dict()
            
            # Step 5: Generate final answer
            final_answer = generate_final_answer(
                user_input, 
                query_response, 
                query_result.visualization_type,
                query_result.is_bihar_map
            )
            query_result.answer = final_answer
            query_result.status = "completed"
            query_result.process_log.append("Analysis completed successfully")
            query_cache[query_id] = query_result.dict()
            
            break
            
        except Exception as e:
            error_msg = str(e)
            query_history.append({"type": "error", "content": error_msg})
            query_result.process_log.append(f"Attempt {current_attempt} - ERROR:\n{error_msg}\n")
            query_cache[query_id] = query_result.dict()
            
            if current_attempt >= max_retries:
                query_result.process_log.append("All attempts failed - switching to theoretical approach")
                query_result.question_type = "theoretical"
                await process_theoretical_question(query_id, user_input)
                break
            
            time.sleep(1)

async def process_theoretical_question(query_id: str, user_input: str):
    """Process a theoretical question using SerpAPI"""
    query_result = QueryResult(**query_cache[query_id])
    query_result.process_log.append("Processing as theoretical question")
    query_cache[query_id] = query_result.dict()
    
    try:
        external_answer = search_with_serpapi(user_input)
        query_result.answer = external_answer
        query_result.status = "completed"
        query_result.is_external_data = True
        query_cache[query_id] = query_result.dict()
    except Exception as e:
        query_result.answer = f"Error processing theoretical question: {str(e)}"
        query_result.status = "error"
        query_cache[query_id] = query_result.dict()

@app.get("/api/query/{query_id}", response_model=QueryResult)
async def get_query_result(query_id: str):
    """Get query result by ID"""
    if query_id not in query_cache:
        return JSONResponse(
            status_code=404,
            content={"message": "Query not found"}
        )
    return query_cache[query_id]

@app.get("/api/query/{query_id}/download")
async def download_query_results(query_id: str):
    """Download query results as CSV"""
    if query_id not in query_cache:
        return JSONResponse(
            status_code=404,
            content={"message": "Query not found"}
        )
    
    query_result = query_cache[query_id]
    if not query_result["data"]:
        return JSONResponse(
            status_code=400,
            content={"message": "No data to download"}
        )
    
    # Create CSV in memory
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=query_result["columns"])
    writer.writeheader()
    writer.writerows(query_result["data"])
    
    # Prepare response
    output.seek(0)
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename=query_results_{query_id}.csv"
        }
    )
 
@app.get("/api/schema")
async def get_schema_info():
    """Get database schema information"""
    return {
        "tables": list(schema.keys()),
        "district_related_tables": district_related_tables
    }
