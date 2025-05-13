TABLE_SCHEMAS = {
    "Bihar_police_station": {
        "description": "Stores administrative and policing data for Bihar, including district codes, district names, police station names, circle names, subdivisions, and range details.",
        "columns": {
            "a_Id": "Unique identifier for each police station entry.",
            "district_Code": "Code representing the district to which the police station belongs.",
            "district_name": "Name of the district where the police station is located.",
            "police_station": "Name of the police station.",
            "circle_Name": "Name of the police circle to which the police station belongs.",
            "subdivision_Name": "Name of the subdivision where the police station is located.",
            "subdivision_Code": "Code representing the subdivision to which the police station belongs.",
            "range_id": "Identifier for the police range.",
            "rangeName": "Name of the police range to which the police station belongs."
        }
    },
    "Bihar_jp_senani_scheme_District_wise": {
        "description": "Stores district-wise data on monthly pensioners under the JP Senani scheme, including details about gender, age, matching score, and pension amounts.",
        "columns": {
            "district_name": "Name of the district.",
            "gender": "Gender of the pensioner.",
            "age_of_pensioner": "Age of the pensioner.",
            "matchingScore": "Matching score, potentially related to Aadhaar verification or other identification processes.",
            "pension_amount": "Monthly pension amount allocated to the individual.",
            "state_name": "Name of the state (Bihar in this case).",
            "focus_area": "Department or sector focus (likely Social Welfare or a related area)."
        }
    },
    "Bihar_district_wise_water_hydrant": {
        "description": "Stores data on fire hydrants in Bihar, including source, location (latitude and longitude), fire type classification, hydrant location, district name, district code, and range name.",
        "columns": {
            "hydrant_source": "Source of the hydrant data.",
            "district_name": "Name of the district where the fire hydrant is located.",
            "fireType_N": "Classification or type of fire hydrant.",
            "latitude": "Latitude coordinate of the fire hydrant's location.",
            "longitude": "Longitude coordinate of the fire hydrant's location.",
            "hydrant_location": "Description of the specific location of the hydrant.",
            "distCode": "District code associated with the hydrant's location.",
            "range_name": "Name of the range or area to which the hydrant belongs."
        }
    },
    "Bihar_district_wise_fire_vehicle": {
        "description": "Stores information about the type, number, and location of fire vehicles in each district of Bihar.",
        "columns": {
            "type_of_fire_vehicle": "Type of fire vehicle (e.g., fire engine, water tanker).",
            "number_of_fire_vehicle": "Number of fire vehicles of a particular type available.",
            "district_name": "Name of the district where the fire vehicles are located.",
            "dist_Code": "District code of the district.",
            "latitude": "Latitude coordinate of the vehicle's location.",
            "longitude": "Longitude coordinate of the vehicle's location.",
            "location_of_vehicle": "Specific location or station where the vehicle is stationed.",
            "range_name": "Name of the fire service range to which the vehicle belongs."}
        },
    
    "Aangan_Mandey_year_wise_district_wise_category_wise_details": {
        "description": "Stores details on the pay scale and working conditions for Aangan Mandey workers in Bihar across different districts for the years 2017-18, 2018-19 and 2019-20. It includes information on education level, designation, and social category, along with salary components, deductions and leave/attendance information.",
        "columns": {
            "state_name": "Name of the state where the Aangan Mandey scheme is implemented (Bihar).",
            "focus_area": "The department or sector under which the Aangan Mandey data is categorized.",
            "year": "The year for which the data is recorded (2017-18, 2018-19, 2019-20).",
            "district_name": "Name of the district in Bihar where the Aangan Mandey worker is employed.",
            "education": "Educational qualification of the Aangan Mandey worker.",
            "designation": "Job title or position of the Aangan Mandey worker.",
            "category": "Social category of the Aangan Mandey worker.",
            "deduction_in_rupee": "Amount deducted from the Aangan Mandey worker's salary in Indian Rupees.",
            "number_of_absent_days": "Number of days the Aangan Mandey worker was absent.",
            "number_of_paid_leave_days": "Number of paid leave days taken by the Aangan Mandey worker.",
            "number_of_strike_days": "Number of days the Aangan Mandey worker participated in strikes.",
            "other_deduction_in_rupee": "Amount of other deductions from the Aangan Mandey worker's salary in Indian Rupees.",
            "salary_in_rupee": "Base salary of the Aangan Mandey worker in Indian Rupees.",
            "state_allowance_in_rupee": "State allowance provided to the Aangan Mandey worker in Indian Rupees.",
            "total_payable_amount": "Total payable amount to the Aangan Mandey worker in Indian Rupees.",
            "total_working_days": "Total number of working days for the Aangan Mandey worker in the specified period."}
        },
    "Aangan_Mandey_yearwise_distrcitwise_number_of_workers": {
        "description": "Stores the workforce distribution details under Bihar's Aangan Mandey scheme across all districts for the years 2017-18, 2018-19, and 2019-20, including counts of Sahaiyaka (helpers), Sevika (workers), and Lady Supervisors by district, education level, and social category.",
        "columns": {
            "state_name": "Name of the state (Bihar).",
            "focus_area": "Department or sector under which the data is collected and stored.",
            "year": "Year for which the workforce data is recorded (2017-18, 2018-19, 2019-20).",
            "district_name": "Name of the district in Bihar.",
            "education": "Educational qualification of the Aangan Mandey worker.",
            "category": "Social category of the Aangan Mandey worker.",
            "number_of_sahaiyaka": "Number of Sahaiyaka (helpers) in the specified district, year, education level, and category.",
            "number_of_sevika": "Number of Sevika (workers) in the specified district, year, education level, and category.",
            "number_of_lady_supervisor": "Number of Lady Supervisors in the specified district, year, education level, and category."}
            }
    ,
    "Artificial_insemination_centres_district_wise": {
        "description": "Stores data on the number of Artificial Insemination Centres (Government Agencies) across different districts.",
        "columns": {
            "sector_name": "Name of the sector to which the data belongs.",
            "sector_id": "Unique identifier for the sector.",
            "focus_area": "Indicates the specific area or department under focus.",
            "year": "Year for which the data is recorded (e.g., 2015-16).",
            "state_name": "Name of the state (Bihar).",
            "district_name": "Name of the district.",
            "centre_item": "Specific item related to the centre (e.g., total centres).",
            "centre_value": "Numerical value representing the number of centres.",
            "centre_unit": "Unit of measurement for the centre value (e.g., Number).",
            "source": "Source of the data (e.g., Directorate of Animal Husbandry)."
        }
    },
    "Artificial_insemination_performed_on_cattle_distrcit_wise": {
        "description": "Stores data on the number of artificial inseminations performed on Bonvies, buffalo, and cattle, district-wise.",
        "columns": {
            "sector_name": "Name of the sector.",
            "sector_id": "ID of the sector.",
            "focus_area": "The department or area of focus for the data collection.",
            "year": "The year in which the artificial insemination was performed.",
            "state_name": "Name of the state where the artificial insemination was performed (Bihar).",
            "district_name": "Name of the district where the artificial insemination was performed.",
            "cattle_item": "Type of cattle on which artificial insemination was performed (Bonvies, Buffalo, and Cattle).",
            "cattle_value": "Number of artificial inseminations performed, in thousands.",
            "cattle_unit": "Unit of measurement for the cattle value (Thousands).",
            "source": "Source of the data (Directorate of Animal Husbandry, Animal & Fisheries, Resources Department, Govt. of Bihar)."
        }
    },
    "Bhagalpur_smartcity_projectwise_progress_report": {
        "description": "Contains progress details of Bhagalpur Smart City projects in Bihar for the year 2024-25, including project costs, financial and physical progress, and target completion dates across various focus areas.",
        "columns": {
            "state_name": "Name of the state where the project is located (Bihar).",
            "district_name": "Name of the district where the project is located (Bhagalpur).",
            "year": "The year for which the project progress data is reported (2024-25).",
            "focus_area": "Area of focus for the project (e.g., infrastructure, public spaces, sustainability).",
            "project_id": "Unique identifier for the project.",
            "project_name": "Name of the Smart City project.",
            "project_cost_in_crore": "Total estimated cost of the project in crore (Indian Rupees).",
            "total_cost_in_crore": "The total cost of the project in crore (Indian Rupees).",
            "financial_progress_in_crore": "Amount of financial expenditure incurred on the project in crore (Indian Rupees).",
            "physical_progress_in_percentage": "Percentage of physical work completed on the project.",
            "financial_progress_in_percentage": "Percentage of financial expenditure compared to the total project cost.",
            "target_work_completion_date": "Planned date for the completion of the project work."
        }
    },
    "Bihar_District_block_wise_School_infrastructure_and_facilities": {
        "description": "Stores detailed data on school infrastructure and facilities, categorized by district and block in Bihar, including school types, building conditions, amenities, and other relevant information.",
        "columns": {
            "district_name": "Name of the district in Bihar.",
            "sector_name": "Name of the sector.",
            "focus_area": "The specific area of focus within education.",
            "year": "Year the data was collected.",
            "state_name": "Name of the state (Bihar).",
            "block_name": "Name of the block within the district.",
            "school_count": "Total number of schools in the specified district and block.",
            "number_of_schools_under_Department_of_Education": "Number of schools administered by the Department of Education.",
            "number_of_Private_Unaided_Recognized_Schools": "Number of privately owned, unaided but recognized schools.",
            "number_of_School_College_Affiliated_Schools": "Number of schools affiliated with colleges.",
            "number_of_Unrecognized_Schools": "Number of schools that are not officially recognized.",
            "number_of_Constituent_Colleges": "Number of colleges that are part of a larger university.",
            "number_of_Buniyadi_Schools": "Number of Buniyadi schools.",
            "number_of_Recognized_Aided_Sanskrit_Schools": "Number of recognized Sanskrit schools that receive financial aid.",
            "number_of_madarasa_unaided_recognized_schools": "Number of unaided but recognized Madarasa schools.",
            "number_of_Project_Girls_High_Schools": "Number of Project Girls High Schools.",
            "number_of_Rajkiya_High_Schools": "Number of Rajkiya (Government) High Schools.",
            "number_of_madarasa_unrecognized_schools": "Number of unrecognized Madarasa schools.",
            "number_of_schools_under_Social_Welfare_Department": "Number of schools administered by the Social Welfare Department.",
            "number_of_madarasa_aided_recognized_schools": "Number of aided and recognized Madarasa schools.",
            "number_of_Recognized_Government_Unaided_Sanskrit_Schools": "Number of government-run, unaided but recognized Sanskrit schools.",
            "number_of_schools_under_Tribal_Welfare_Department": "Number of schools administered by the Tribal Welfare Department.",
            "number_of_Sainik_Schools": "Number of Sainik (Military) Schools.",
            "number_of_Railway_Schools": "Number of schools run by the Railway Department.",
            "number_of_Primary_with_Upper_Primary_Schools": "Number of schools offering both primary and upper primary education.",
            "number_of_Primary_Upper_Primary_and_Secondary_Schools": "Number of schools offering primary, upper primary, and secondary education.",
            "number_of_Primary_Schools": "Number of schools offering only primary education.",
            "number_of_Pri_with_Upper_Pri_Sec_and_High_Sec_Schools": "Number of schools offering primary, upper primary, secondary, and higher secondary education.",
            "number_of_Higher_Secondary_Only_Junior_Colleges": "Number of junior colleges offering only higher secondary education.",
            "number_of_Upper_Pri_Sec_and_High_Sec_Schools": "Number of schools offering upper primary, secondary, and higher secondary education.",
            "number_of_Upper_Primary_Only_Schools": "Number of schools offering only upper primary education.",
            "number_of_Upper_Primary_and_Secondary_Schools": "Number of schools offering upper primary and secondary education.",
            "number_of_Secondary_Only_Schools": "Number of schools offering only secondary education.",
            "number_of_Urban_Schools": "Number of schools located in urban areas.",
            "number_of_Rural_Schools": "Number of schools located in rural areas.",
            "number_of_Government_Schools": "Number of government-run schools.",
            "number_of_Private_Schools": "Number of privately owned schools.",
            "number_of_Government_Schools_in_Rent_Free_Buildings": "Number of government schools operating in rent-free buildings.",
            "number_of_Rented_Schools": "Number of schools operating in rented buildings.",
            "number_of_Schools_Running_in_Other_Department_Buildings": "Number of schools running in buildings belonging to other government departments.",
            "number_of_buildings_in_schools": "Total number of buildings in all schools.",
            "number_of_blocks_in_schools": "Total number of blocks (separate structures) in all schools.",
            "number_of_pucca_school_building": "Number of schools with permanent (pucca) buildings.",
            "number_of_kuchcha_school_building": "Number of schools with temporary (kuchcha) buildings.",
            "number_of_tents": "Number of schools using tents as structures.",
            "number_of_buildings_under_construction": "Number of school buildings currently under construction.",
            "number_of_Pucca_School_boundary_walls": "Number of schools with permanent (pucca) boundary walls.",
            "number_of_Pucca_But_Broken_School_boundary_walls": "Number of schools with permanent but broken boundary walls.",
            "number_of_Schools_with_No_Boundary_Walls": "Number of schools with no boundary walls.",
            "number_of_Schools_with_Other_Boundary_Walls": "Number of schools with boundary walls made of other materials.",
            "number_of_Schools_with_Partial_Boundary_Walls": "Number of schools with only partial boundary walls.",
            "number_of_Schools_with_Hedges_as_Boundary_Walls": "Number of schools using hedges as boundary walls.",
            "number_of_Schools_with_Under_Construction_Boundary_Walls": "Number of schools with boundary walls currently under construction.",
            "number_of_Schools_with_Barbed_Wire_Fencing": "Number of schools with barbed wire fencing.",
            "number_of_classrooms_used_for_instructional_purpose": "Number of classrooms used for teaching.",
            "number_of_classrooms_not_used_for_instructional_purpose": "Number of classrooms not used for teaching.",
            "number_of_classrooms_under_construction": "Number of classrooms currently under construction.",
            "number_of_additional_classrooms": "Number of additional classrooms.",
            "number_of_classrooms_for_instructional_purpose_pre_primary": "Number of classrooms used for pre-primary instruction.",
            "number_of_classrooms_for_instructional_purpose_primary": "Number of classrooms used for primary instruction.",
            "number_of_classrooms_for_instructional_purpose_upper_primary": "Number of classrooms used for upper primary instruction.",
            "number_of_classrooms_for_instructional_purpose_secondary": "Number of classrooms used for secondary instruction.",
            "number_of_classrooms_for_instructional_purpose_higher_secondary": "Number of classrooms used for higher secondary instruction.",
            "number_of_other_rooms": "Number of other rooms in schools.",
            "number_of_school_land_available_for_expand_school_facilities": "Number of schools with available land for expanding facilities.",
            "number_of_school_land_not_available_for_expand_school_facilities": "Number of schools with no available land for expanding facilities.",
            "number_of_school_with_toilet": "Number of schools with toilet facilities.",
            "number_of_school_without_toilet": "Number of schools without toilet facilities.",
            "number_of_schools_with_handwashing_facility_toilet_urinal": "Number of schools with handwashing facilities near toilets/urinals.",
            "number_of_schools_without_handwashing_facility_toilet_urinal": "Number of schools without handwashing facilities near toilets/urinals.",
            "number_of_school_having_incinerator_avail_in_girls_toilets": "Number of schools with incinerators available in girls' toilets.",
            "number_of_school_not_having_incinerator_avail_in_girls_toilets": "Number of schools without incinerators in girls' toilets.",
            "number_of_school_having_drinking_water_available": "Number of schools with drinking water available.",
            "number_of_school_not_having_drinking_water_available": "Number of schools without drinking water available.",
            "number_of_school_having_handpump_available": "Number of schools with a handpump available.",
            "number_of_school_not_having_handpump_available": "Number of schools without a handpump available.",
            "number_of_school_having_functional_handpump": "Number of schools with a functional handpump.",
            "number_of_school_not_having_functional_handpump": "Number of schools without a functional handpump.",
            "number_of_schools_having_protected_well": "Number of schools with a protected well.",
            "number_of_schools_not_having_protected_well": "Number of schools without a protected well.",
            "number_of_school_having_functional_protected": "Number of schools with a functional protected well.",
            "number_of_school_not_having_functional_protected": "Number of schools without a functional protected well.",
            "number_of_school_having_unprotected_well": "Number of schools with an unprotected well.",
            "number_of_school_not_having_unprotected_well": "Number of schools without an unprotected well.",
            "number_of_school_having_functional_unprotected_well": "Number of schools with a functional unprotected well.",
            "number_of_school_not_having_functional_unprotected_well": "Number of schools without a functional unprotected well.",
            "number_od_school_having_tap_water": "Number of schools with tap water available.",
            "number_of_school_not_having_tap_water": "Number of schools without tap water available.",
            "number_of_school_having_functional_tap_water": "Number of schools with functional tap water.",
            "number_of_school_not_having_functional_tap_water": "Number of schools without functional tap water.",
            "number_of_school_having_packaged_bottled_water": "Number of schools with packaged/bottled water available.",
            "number_of_school_not_having_packaged_bottled_water": "Number of schools without packaged/bottled water available.",
            "number_of_school_having_functional_packaged_bottled_water": "Number of schools with functional packaged/bottled water (available and usable).",
            "number_of_school_not_having_func_packaged_bottled_water": "Number of schools without functional packaged/bottled water.",
            "number_of_school_having_other_drinking_water_sources": "Number of schools with other sources of drinking water.",
            "number_of_school_not_having_other_drinking_water_sources": "Number of schools without other sources of drinking water.",
            "number_of_school_having_func_other_drinking_water_sources": "Number of schools with functional other sources of drinking water.",
            "number_of_school_not_having_func_other_drinking_water_sources": "Number of schools without functional other sources of drinking water.",
            "number_of_school_having_water_purifier_in_school": "Number of schools with a water purifier.",
            "number_of_school_not_having_water_purifier_in_school": "Number of schools without a water purifier.",
            "number_of_school_having_water_quality_tested": "Number of schools that have had their water quality tested.",
            "number_of_school_not_having_water_quality_tested": "Number of schools that have not had their water quality tested.",
            "number_of_school_having_rainwater_harvesting_in_school": "Number of schools with rainwater harvesting systems.",
            "number_of_school_not_having_rainwater_harvesting_in_school": "Number of schools without rainwater harvesting systems.",
            "number_of_school_having_handwashing_after_meal_in_school": "Number of schools promoting handwashing after meals.",
            "number_of_school_not_having_handwashing_after_meal_in_school": "Number of schools not promoting handwashing after meals.",
            "number_of_wash_points_in_school": "Number of hand wash points in school.",
            "number_of_school_having_electricity_in_school": "Number of schools with electricity.",
            "number_of_school_not_having_electricity_in_school": "Number of schools without electricity.",
            "number_of_library_books": "Number of books in the school library.",
            "number_of_ncert_books_in_library": "Number of NCERT books in the school library.",
            "number_of_books_in_book_bank": "Number of books in the school's book bank.",
            "number_of_ncert_books_in_book_bank": "Number of NCERT books in the school's book bank.",
            "number_of_books_in_reading_corner": "Number of books in the school's reading corner.",
            "school_arrangement_for_playing": "Indicates the school arrangement for playing.",
            "condition_of_last_year_medical_checkup": "Indicates the condition of medical checkups done in schools last year.",
            "number_of_school_having_solar_panels": "Number of schools with solar panels.",
            "number_of_school_not_having_solar_panels": "Number of schools without solar panels.",
            "number_of_school_having_library_in_school": "Number of schools with a library.",
            "number_of_school_not_having_library_in_school": "Number of schools without a library.",
            "number_of_school_having_book_bank": "Number of schools with a book bank.",
            "number_of_school_not_having_book_bank": "Number of schools without a book bank.",
            "number_of_school_having_reading_corner": "Number of schools with a reading corner.",
            "number_of_school_not_having_reading_corner": "Number of schools without a reading corner.",
            "number_of_school_having_librarian_available": "Number of schools with a librarian.",
            "number_of_school_not_having_librarian_available": "Number of schools without a librarian.",
            "number_of_school_having_newspapers_and_magazines": "Number of schools subscribing to newspapers and magazines.",
            "number_of_school_not_having_newspapers_and_magazines": "Number of schools not subscribing to newspapers and magazines.",
            "number_of_school_having_playground_facility": "Number of schools with a playground.",
            "number_of_school_not_having_playground_facility": "Number of schools without a playground.",
            "number_of_school_having_alternative_playground_arrangement": "Number of schools with alternative playground arrangements.",
            "number_of_school_not_having_alternative_playground_arrangement": "Number of schools without alternative playground arrangements.",
            "number_of_school_having_medical_checkup": "Number of schools conducting medical checkups.",
            "number_of_school_not_having_medical_checkup": "Number of schools not conducting medical checkups.",
            "number_of_school_having_health_height_in_school": "Number of schools recording students' height.",
            "number_of_school_not_having_health_height_in_school": "Number of schools not recording students' height.",
            "number_of_school_having_health_weight_in_school": "Number of schools recording students' weight.",
            "number_of_school_not_having_health_weight_in_school": "Number of schools not recording students' weight.",
            "number_of_school_having_health_eyes_in_school": "Number of schools conducting eye exams.",
            "number_of_school_not_having_health_eyes_in_school": "Number of schools not conducting eye exams.",
            "number_of_school_having_health_dental_in_school": "Number of schools conducting dental checkups.",
            "number_of_school_not_having_health_dental_in_school": "Number of schools not conducting dental checkups.",
            "number_of_school_having_health_throat_in_school": "Number of schools conducting throat examinations.",
            "number_of_school_not_having_health_throat_in_school": "Number of schools not conducting throat examinations.",
            "number_of_school_having_school_having_annual_health_record": "Number of schools maintaining annual health records.",
            "number_of_school_not_having_school_having_annual_health_record": "Number of schools not maintaining annual health records.",
            "number_of_school_having_thermal_scanner_in_school": "Number of schools with thermal scanners.",
            "number_of_school_not_having_thermal_scanner_in_school": "Number of schools without thermal scanners.",
            "number_of_school_having_first_aid_kit_in_school": "Number of schools with a first-aid kit.",
            "number_of_school_not_having_first_aid_kit_in_school": "Number of schools without a first-aid kit.",
            "number_of_school_having_medicines_in_schools": "Number of schools having medicine in schools.",
            "number_of_school_not_having_medicines_in_schools": "Number of schools not having medicine in schools.",
            "number_of_school_having_iron_and_folic_acid_tablets": "Number of schools distributing iron and folic acid tablets.",
            "number_of_school_not_having_iron_and_folic_acid_tablets": "Number of schools not distributing iron and folic acid tablets.",
            "number_of_school_having_ramp_in_school": "Number of schools with ramps for accessibility.",
            "number_of_school_not_having_ramp_in_school": "Number of schools without ramps for accessibility.",
            "number_of_school_having_hand_rails_in_school": "Number of schools with handrails.",
            "number_of_school_not_having_hand_rails_in_school": "Number of schools without handrails.",
            "number_of_school_having_kitchen_garden_in_school": "Number of schools with a kitchen garden.",
            "number_of_school_not_having_kitchen_garden_in_school": "Number of schools without a kitchen garden.",
            "number_of_school_having_kitchen_shed_in_school": "Number of schools with a kitchen shed.",
            "number_of_school_not_having_kitchen_shed_in_school": "Number of schools without a kitchen shed.",
            "number_of_school_having_kitchen_dustbin_in_school": "Number of schools with a kitchen dustbin.",
            "number_of_school_not_having_kitchen_dustbin_in_school": "Number of schools without a kitchen dustbin.",
            "number_of_students_with_furniture": "Number of students having access to furniture."
        }
    },
    "Bihar_district_wise_fire_vehicle": {
        "description": "Stores information about the type, number, and location of fire vehicles in each district of Bihar.",
        "columns": {
            "type_of_fire_vehicle": "Type of fire vehicle (e.g., fire engine, water tanker).",
            "number_of_fire_vehicle": "Number of fire vehicles of a particular type available.",
            "district_name": "Name of the district where the fire vehicles are located.",
            "dist_Code": "District code of the district.",
            "latitude": "Latitude coordinate of the vehicle's location.",
            "longitude": "Longitude coordinate of the vehicle's location.",
            "location_of_vehicle": "Specific location or station where the vehicle is stationed.",
            "range_name": "Name of the fire service range to which the vehicle belongs."
        }
    },
    "Bihar_district_wise_water_hydrant": {
        "description": "Stores data on fire hydrants in Bihar, including source, location (latitude and longitude), fire type classification, hydrant location, district name, district code, and range name.",
        "columns": {
            "hydrant_source": "Source of the hydrant data.",
            "district_name": "Name of the district where the fire hydrant is located.",
            "fireType_N": "Classification or type of fire hydrant.",
            "latitude": "Latitude coordinate of the fire hydrant's location.",
            "longitude": "Longitude coordinate of the fire hydrant's location.",
            "hydrant_location": "Description of the specific location of the hydrant.",
            "distCode": "District code associated with the hydrant's location.",
            "range_name": "Name of the range or area to which the hydrant belongs."
        }
    },
    "Bihar_jp_senani_scheme_District_wise": {
        "description": "Stores district-wise data on monthly pensioners under the JP Senani scheme, including details about gender, age, matching score, and pension amounts.",
        "columns": {
            "district_name": "Name of the district.",
            "gender": "Gender of the pensioner.",
            "age_of_pensioner": "Age of the pensioner.",
            "matchingScore": "Matching score, potentially related to Aadhaar verification or other identification processes.",
            "pension_amount": "Monthly pension amount allocated to the individual.",
            "state_name": "Name of the state (Bihar in this case).",
            "focus_area": "Department or sector focus (likely Social Welfare or a related area)."
        }
    },
    "Bihar_police_station": {
        "description": "Stores administrative and policing data for Bihar, including district codes, district names, police station names, circle names, subdivisions, and range details.",
        "columns": {
            "a_Id": "Unique identifier for each police station entry.",
            "district_Code": "Code representing the district to which the police station belongs.",
            "district_name": "Name of the district where the police station is located.",
            "police_station": "Name of the police station.",
            "circle_Name": "Name of the police circle to which the police station belongs.",
            "subdivision_Name": "Name of the subdivision where the police station is located.",
            "subdivision_Code": "Code representing the subdivision to which the police station belongs.",
            "range_id": "Identifier for the police range.",
            "rangeName": "Name of the police range to which the police station belongs."
        }
    },
    "Biharsharif_smartcity_projectwise_progress_report": {
        "description": "Stores project-wise progress reports for Smart City initiatives in Biharsharif, including project costs, timelines, physical and financial progress, and remarks on project status for the year 2024-25.",
        "columns": {
            "state_name": "Name of the state (Bihar).",
            "district_name": "Name of the district (Biharsharif).",
            "focus_area": "The specific sector or area of development the project falls under.",
            "project_Name": "Name of the Smart City project.",
            "project_cost_in_crore": "The estimated or actual cost of the project in crore rupees.",
            "year": "The year for which the progress is being reported (2024-25).",
            "project_start_date": "The date when the project officially commenced.",
            "completion_date": "The planned or actual date of project completion.",
            "physical_Progress_in_percentage": "Percentage of physical work completed for the project.",
            "financial_progress_in_percentage": "Percentage of funds utilized for the project.",
            "Remarks": "Any notes, observations, or status updates regarding the project."
        }
    },
    "Block_wise_enrollment_of_students_gender_class_wise_year_wise": {
  "description": "Stores block-wise student enrollment data, categorized by gender (boys, girls, transgender) and class (PP3, PP2, PP1, 1-12), on a yearly basis (2022-23 and 2023-24) sourced from the UDISE portal.",
  "columns": {
    "state_name": "Name of the state.",
    "sector_name": "Name of the sector.",
    "source": "Source of the data, likely UDISE.",
    "focus_area": "Focus area or department collecting the data.",
    "year": "Year of the enrollment data (e.g., 2022-23, 2023-24).",
    "district_name": "Name of the district.",
    "block_name": "Name of the block.",
    "school_name": "Name of the school.",
    "school_type": "Type of school (e.g., government, private).",
    "school_category": "Category of the school.",
    "pre_primary_three_boys": "Number of boys enrolled in Pre-Primary class 3.",
    "pre_primary_three_girls": "Number of girls enrolled in Pre-Primary class 3.",
    "pre_primary_three_transgender": "Number of transgender students enrolled in Pre-Primary class 3.",
    "pre_primary_three_total": "Total number of students enrolled in Pre-Primary class 3.",
    "pre_primary_two_boys": "Number of boys enrolled in Pre-Primary class 2.",
    "pre_primary_two_girls": "Number of girls enrolled in Pre-Primary class 2.",
    "pre_primary_two_transgender": "Number of transgender students enrolled in Pre-Primary class 2.",
    "pre_primary_two_total": "Total number of students enrolled in Pre-Primary class 2.",
    "pre_primary_one_boys": "Number of boys enrolled in Pre-Primary class 1.",
    "pre_primary_one_girls": "Number of girls enrolled in Pre-Primary class 1.",
    "pre_primary_one_transgender": "Number of transgender students enrolled in Pre-Primary class 1.",
    "pre_primary_one_total": "Total number of students enrolled in Pre-Primary class 1.",
    "class_one_boys": "Number of boys enrolled in class 1.",
    "class_one_girls": "Number of girls enrolled in class 1.",
    "class_one_transgender": "Number of transgender students enrolled in class 1.",
    "class_one_total": "Total number of students enrolled in class 1.",
    "class_two_boys": "Number of boys enrolled in class 2.",
    "class_two_girls": "Number of girls enrolled in class 2.",
    "class_two_transgender": "Number of transgender students enrolled in class 2.",
    "class_two_total": "Total number of students enrolled in class 2.",
    "class_three_boys": "Number of boys enrolled in class 3.",
    "class_three_girls": "Number of girls enrolled in class 3.",
    "class_three_transgender": "Number of transgender students enrolled in class 3.",
    "class_three_total": "Total number of students enrolled in class 3.",
    "class_four_boys": "Number of boys enrolled in class 4.",
    "class_four_girls": "Number of girls enrolled in class 4.",
    "class_four_transgender": "Number of transgender students enrolled in class 4.",
    "class_four_total": "Total number of students enrolled in class 4.",
    "class_five_boys": "Number of boys enrolled in class 5.",
    "class_five_girls": "Number of girls enrolled in class 5.",
    "class_five_transgender": "Number of transgender students enrolled in class 5.",
    "class_five_total": "Total number of students enrolled in class 5.",
    "class_six_boys": "Number of boys enrolled in class 6.",
    "class_six_girls": "Number of girls enrolled in class 6.",
    "class_six_transgender": "Number of transgender students enrolled in class 6.",
    "class_six_total": "Total number of students enrolled in class 6.",
    "class_seven_boys": "Number of boys enrolled in class 7.",
    "class_seven_girls": "Number of girls enrolled in class 7.",
    "class_seven_transgender": "Number of transgender students enrolled in class 7.",
    "class_seven_total": "Total number of students enrolled in class 7.",
    "class_eight_boys": "Number of boys enrolled in class 8.",
    "class_eight_girls": "Number of girls enrolled in class 8.",
    "class_eight_transgender": "Number of transgender students enrolled in class 8.",
    "class_eight_total": "Total number of students enrolled in class 8.",
    "class_nine_boys": "Number of boys enrolled in class 9.",
    "class_nine_girls": "Number of girls enrolled in class 9.",
    "class_nine_transgender": "Number of transgender students enrolled in class 9.",
    "class_nine_total": "Total number of students enrolled in class 9.",
    "class_ten_boys": "Number of boys enrolled in class 10.",
    "class_ten_girls": "Number of girls enrolled in class 10.",
    "class_ten_transgender": "Number of transgender students enrolled in class 10.",
    "class_ten_total": "Total number of students enrolled in class 10.",
    "class_eleven_boys": "Number of boys enrolled in class 11.",
    "class_eleven_girls": "Number of girls enrolled in class 11.",
    "class_eleven_transgender": "Number of transgender students enrolled in class 11.",
    "class_eleven_total": "Total number of students enrolled in class 11.",
    "class_twelve_boys": "Number of boys enrolled in class 12.",
    "class_twelve_girls": "Number of girls enrolled in class 12.",
    "class_twelve_transgender": "Number of transgender students enrolled in class 12.",
    "class_twelve_total": "Total number of students enrolled in class 12.",
    "total_students": "Total number of students across all classes."
  }
},
    "Cases_of_Land_dispute_in_bihar": {
        "description": "Stores data regarding the number of land dispute cases filed in police stations across Bihar, categorized by dispute type.",
        "columns": {
            "focus_area": "Indicates the department or area of focus for the data collection.",
            "year": "The year in which the land dispute case was registered.",
            "state_name": "The name of the state where the land dispute occurred (Bihar).",
            "dispute_type": "The type or nature of the land dispute.",
            "number_of_case": "The number of land dispute cases registered."
        }
    },
    "Civil_Seva_Protsahan_Yojna_for_bc_ebc_students": {
        "description": "Stores data about One Time Payment to BC and EBC Students completing UPSC PT/BPSC PT in Bihar state, tracking exam registrations, pass rates, and payment details.",
        "columns": {
            "state_name": "Name of the state (Bihar in this case).",
            "focus_area": "Department or sector focus related to the scheme.",
            "scheme_name": "Name of the Civil Seva Protsahan Yojna scheme.",
            "district_name": "Name of the district in Bihar.",
            "year": "Year for which the data is recorded.",
            "number_of_candidates": "Total number of candidates registered under the scheme.",
            "number_of_candidates_cleared_upsc": "Number of candidates who cleared the UPSC exam.",
            "number_of_candidates_cleared_bpsc": "Number of candidates who cleared the BPSC exam.",
            "number_of_candidates_selected_for_upsc_amount": "Number of candidates selected for UPSC-related financial assistance.",
            "number_of_candidates_selected_for_bpsc_amount": "Number of candidates selected for BPSC-related financial assistance.",
            "number_of_upsc_payment_done": "Number of UPSC candidates for whom payment was completed.",
            "number_of_bpsc_payment_done": "Number of BPSC candidates for whom payment was completed."
        }
    },
    "Civil_Seva_Protsahan_Yojna_for_female_students": {
        "description": "Stores data related to the Civil Seva Protsahan Yojna scheme for female students, potentially including information on candidates, their success in UPSC/BPSC exams, and associated payments.",
        "columns": {
            "state_name": "Name of the state where the scheme is being implemented.",
            "focus_area": "The area of focus for the scheme (e.g., Social Welfare, Education).",
            "scheme_name": "Name of the specific Civil Seva Protsahan Yojna scheme.",
            "year": "Year for which the data is recorded.",
            "district_name": "Name of the district to which the data pertains.",
            "category_name": "Category of the female students (e.g., General, OBC, SC, ST).",
            "gender_name": "Gender of the candidates, likely limited to \"Female\".",
            "number_of_candidates": "Total number of female candidates under the scheme.",
            "number_of_candidates_cleared_upsc": "Number of female candidates who cleared the UPSC exam.",
            "number_of_candidates_cleared_bpsc": "Number of female candidates who cleared the BPSC exam.",
            "number_of_candidates_selected_for_upsc_amount": "Number of candidates selected for the UPSC incentive amount.",
            "number_of_candidates_selected_for_bpsc_amount": "Number of candidates selected for the BPSC incentive amount.",
            "number_of_upsc_payment_done": "Number of UPSC incentive payments completed.",
            "number_of_upsc_payment_not_done": "Number of UPSC incentive payments not completed.",
            "number_of_bpsc_payment_done": "Number of BPSC incentive payments completed.",
            "number_of_bpsc_payment_not_done": "Number of BPSC incentive payments not completed.",
            "number_of_bpsc_paymeny_not_done": "Number of BPSC incentive payments not completed (likely a duplicate and typo)."
        }
    },
    "District_wise_Digital_India_Land_Records_Modernization_Programme": {
        "description": "Stores data related to the progress of the Digital India Land Records Modernization Programme at the district level.",
        "columns": {
            "scheme_name": "Name of the scheme, which is likely Digital India Land Records Modernization Programme.",
            "state_name": "Name of the state where the program is being implemented.",
            "district_name": "Name of the district.",
            "year": "Year for which the data is recorded.",
            "number_of_villages_computerization__land_records_completed": "Number of villages where computerization of land records has been completed.",
            "number_of_computerized_sub_registrar_offices": "Number of sub-registrar offices that have been computerized.",
            "number_of_digitized_mapsheets": "Number of map sheets that have been digitized.",
            "number_of_sub_registrar_linked_with_land_records_system": "Number of sub-registrar offices linked with the land records system.",
            "number_of_villages_with_mapping_linked_to_record_of_rights": "Number of villages where mapping is linked to the record of rights."
        }
    },
    "District_wise_Direct_Benefit_Transfer": {
        "description": "Stores data related to Direct Benefit Transfer (DBT) schemes, including the number of beneficiaries, funds transferred, and transactions, organized by district, state, scheme, and year.",
        "columns": {
            "scheme_name": "Name of the Direct Benefit Transfer scheme.",
            "state_name": "Name of the state where the DBT scheme is implemented.",
            "district_name": "Name of the district where the DBT scheme is being tracked.",
            "year": "Year for which the DBT data is recorded.",
            "authenticated_direct_benefit_transfer_beneficiaries_in_lakh": "Number of beneficiaries whose DBT was authenticated, measured in lakhs.",
            "number_of_direct_benefit_transfer_beneficiaries_in_lakh": "Total number of DBT beneficiaries, measured in lakhs.",
            "direct_benefit_transfer_fund_in_crore": "Amount of funds transferred through DBT, measured in crores.",
            "unit": "Unit of measurement for the data, likely specifying currency or quantity.",
            "number_of_direct_benefit_transfer_transactions_in_lakh": "Number of DBT transactions, measured in lakhs."
        }
    },
    "District_wise_Fertilizer_Stock_Supply": {
        "description": "Stores data on district-wise fertilizer stock and supply, including urea and non-urea fertilizers, potentially related to the Direct Benefit Transfer (DBT) scheme.",
        "columns": {
            "scheme_name": "Name of the scheme under which the fertilizer distribution is managed, possibly related to DBT.",
            "state_name": "Name of the state for which the fertilizer stock and supply data is recorded.",
            "district_name": "Name of the district for which the fertilizer stock and supply data is recorded.",
            "year": "Year for which the fertilizer stock and supply data is recorded.",
            "quarter": "Quarter of the year for which the fertilizer stock and supply data is recorded.",
            "stock_of_urea": "Amount of urea fertilizer in stock.",
            "requirement_of_urea_fertilizer": "Amount of urea fertilizer required.",
            "stock_of_non_urea_fertilizer": "Amount of non-urea fertilizer in stock.",
            "requirement_of_non_urea_fertilizer": "Amount of non-urea fertilizer required.",
            "supply_of_non_urea_fertilizer": "Amount of non-urea fertilizer supplied.",
            "unit": "Unit of measurement for the fertilizer quantities (e.g., tonnes, kilograms).",
            "supply _of_urea_fertilizer": "Amount of urea fertilizer supplied."
        }
    },
    "Horticulture_area_production_yearwise": {
        "description": "Stores year-wise data about the area and production of various horticulture crops, categorized by sector, state, district, crop type, and crop name.",
        "columns": {
            "sector_name": "Name of the horticulture sector.",
            "state": "Name of the state where the horticulture data is recorded.",
            "focus_area": "Specific area of focus within the horticulture sector.",
            "district_name": "Name of the district where the horticulture activity is taking place.",
            "crop_type": "Type or category of the horticulture crop.",
            "crop_name": "Specific name of the horticulture crop.",
            "year": "Year for which the area and production data is recorded.",
            "crop_area_value": "Numerical value representing the area of the crop.",
            "crop_area_value_unit": "Unit of measurement for the crop area value (e.g., hectares, acres).",
            "crop_production_value": "Numerical value representing the production of the crop.",
            "crop_production_value_unit": "Unit of measurement for the crop production value (e.g., tonnes, kilograms)."
        }
    },
    "Hostel_grant_scheme_SCST_district_category_gender_wise": {
        "description": "Stores data on the CM SC/ST Hostel Scholarship Scheme in Bihar, detailing beneficiaries' hostel, district, category, gender and the year of the grant.",
        "columns": {
            "year": "Financial year for which the scholarship data is recorded.",
            "district_name": "Name of the district where the beneficiary hostel is located.",
            "beneficiary_hostel_name": "Name of the hostel where the beneficiary resides.",
            "scheme_name": "Name of the scholarship scheme (CM SC/ST Hostel Scholarship Scheme).",
            "beneficiary_gender": "Gender of the beneficiary (Male or Female).",
            "beneficiary_category": "Category of the beneficiary.",
            "focus_area": "Department or sector under which the data has been collected and stored."
        }
    },
    "JJHM_Scheme_structure_and_amount_allotment": {
        "description": "Stores data related to the structure and amount allotment for various schemes under the JJHM program, including project type, location, financial info, and department.",
        "columns": {
            "focus_area": "Type of project or scheme being implemented (e.g., MGREGA Plantation, Waterbodies).",
            "state_name": "Name of the state where the scheme is being implemented.",
            "year": "Year in which the scheme was implemented or the data was recorded.",
            "department_name": "Name of the department responsible for executing the scheme.",
            "type_of_structure": "Type of physical structure created or maintained under the scheme.",
            "measurement_of_structure": "Dimensions or specifications of the structure.",
            "district_name": "Name of the district where the structure is located.",
            "block_name": "Name of the block where the structure is located.",
            "panchyat_name": "Name of the panchayat where the structure is located.",
            "area_type": "Type of area where the structure is located (Rural or Urban).",
            "villageCode": "Code of the village where the structure is located.",
            "village_name": "Name of the village where the structure is located.",
            "estimated_Amount": "Estimated cost of the project or structure.",
            "final_amount": "Final or actual cost of the project or structure.",
            "activity_name": "Name of the specific activity undertaken within the scheme."
        }
    },
    "JJHM_nursery_data": {
        "description": "Stores details of nurseries in Bihar, categorized by district, block, and panchayat, including location info, nursery name, size, and number of trees.",
        "columns": {
            "nurseryID": "Unique identifier for each nursery.",
            "district_name": "Name of the district where the nursery is located.",
            "block_name": "Name of the block where the nursery is located.",
            "panchayat_name": "Name of the panchayat where the nursery is located.",
            "urban_area": "Indicates whether the nursery is located in an urban area.",
            "nurseryName": "Name of the nursery.",
            "total_area": "Total area covered by the nursery.",
            "total_number_of_tree": "Total number of trees in the nursery.",
            "Column9": "Additional column; purpose unclear."
        }
    },
    "MMUY_BLUY_beneficiaries_category_wise": {
        "description": "Stores data on beneficiaries under the Bihar Laghu Udyami Yojna (BLUY) and Mukhya Mantri Udyami Yojna (MMUY), categorized by beneficiary types in Bihar.",
        "columns": {
            "focus_area": "Target group or objective of the MMUY or BLUY scheme.",
            "state_name": "Name of the state to which the data belongs (Bihar).",
            "category_name": "Specific category under which beneficiaries are classified.",
            "scheme_name": "Name of the scheme, either MMUY or BLUY.",
            "number_of_beneficiaries": "Number of beneficiaries belonging to the specified category under the respective scheme."
        }
    },
    "MMUY_BLUY_beneficiaries_district_wise": {
        "description": "Stores district-wise beneficiary count under MMUY and BLUY schemes in Bihar.",
        "columns": {
            "focus_area": "Specific objective or target group of the scheme.",
            "state_name": "Name of the state (Bihar).",
            "district_name": "Name of the district in Bihar.",
            "scheme_name": "Name of the scheme (MMUY or BLUY).",
            "number_of_beneficiaries": "Number of beneficiaries for the specified scheme in the specified district."
        }
    },
    "MMUY_BLUY_beneficiaries_project_wise": {
        "description": "Contains beneficiary data under MMUY and BLUY schemes in Bihar, categorized by focus area and type of business.",
        "columns": {
            "focus_area": "The specific area of focus for the scheme (e.g., sector or type of support).",
            "state_name": "The name of the state to which the data pertains (Bihar).",
            "type_of_business_or_enterpreneurship": "The type of business or entrepreneurship the beneficiary is involved in.",
            "scheme_name": "The name of the specific scheme (MMUY or BLUY).",
            "number_of_beneficiaries": "The number of beneficiaries under the specified scheme, focus area, and project."
        }
    },

    "MMUY_BLUY_beneficiaries_year_wise": {
        "description": "Year-wise data of beneficiaries under the Bihar Laghu Udyami Yojna (BLUY) and Mukhya Mantri Udyami Yojna (MMUY).",
        "columns": {
            "focus_area": "Indicates the scheme, specifically 'Beneficiaries Under BLUY MMUY SCHEME'.",
            "state_name": "Name of the state where the schemes are implemented, which is Bihar.",
            "year": "The year for which the beneficiary data is recorded, ranging from 2018 to 2029.",
            "scheme_name": "The name of the specific scheme, either 'BLUY' or 'MMUY'.",
            "number_of_beneficiaries": "The number of beneficiaries under the specified scheme for the given year."
        }
    },
    "Muzaffarpur_smartcity_projectwise_progress_report": {
        "description": "Project-wise progress data for Smart City initiatives in Muzaffarpur for 2024–25.",
        "columns": {
            "state_name": "State where the Smart City project is located.",
            "city_name": "Name of the city (Muzaffarpur).",
            "year": "Year for which the project progress data is reported (2024-25).",
            "project_id": "Unique identifier for each Smart City project.",
            "project_name": "Name of the specific project.",
            "total_cost_in_crore": "Total estimated project cost in crore rupees.",
            "physical_progress​_in_percentage": "Percentage of physical work completed.",
            "financial_progress_a_in_crore": "Financial progress, amount 'A' spent in crore rupees.",
            "financial_progress_b_in_crore": "Financial progress, amount 'B' spent in crore rupees.",
            "overall_financial_progress_a+b_in_crore": "Total financial progress (A+B) in crore rupees.",
            "target_work_completion_date": "Scheduled/estimated date for completion."
        }
    },
    "Paddy_Procurement_districtwise_yearwise_in_Bihar": {
        "description": "District and year-wise paddy procurement data in Bihar, including farmer demographics and procurement details.",
        "columns": {
            "sector_name": "Sector involved in paddy procurement.",
            "state_name": "State name (Bihar).",
            "year": "Year of procurement.",
            "district_name": "District where paddy was procured.",
            "block_name": "Block within the district.",
            "focus_area": "Related scheme or focus area.",
            "total_farmers": "Total number of farmers involved.",
            "total_number_of_male_farmers": "Number of male farmers.",
            "total_number_of_female_farmers": "Number of female farmers.",
            "number_of_general_category_farmers": "Number from general category.",
            "number_of_disciplined_caste_category_farmers": "Number from SC category.",
            "number_of_backward_class_category_farmers": "Number from BC category.",
            "number_of_minority_category_farmers": "Number from minority category.",
            "number_of_extremely_backward_class_category_farmers": "Number from EBC category.",
            "number_of_disciplined_tribe_category_farmers": "Number from ST category.",
            "number_of_others_category_farmers": "Number from other categories.",
            "total_quantity_of_paddy_in_metric_tonnes": "Total quantity procured (metric tonnes).",
            "total_amount_paid_in_Rupees": "Total payment to farmers (INR).",
            "source": "Data source (e.g., NIC)."
        }
    },
    "Patna_smartcity_projectwise_progress_report": {
        "description": "Project-wise progress report for Patna Smart City initiative (2024–25), including physical and financial status.",
        "columns": {
            "state_name": "State name (Bihar).",
            "district_name": "District name (Patna).",
            "focus_area": "Focus area of the project (e.g., Infrastructure, Environment).",
            "project_name": "Name of the project.",
            "administrative_approval_amount_in_cr": "Approved budget in crore rupees.",
            "agreement_amout_in_cr": "Agreed project amount in crore rupees.",
            "year": "Year of report (2024–25).",
            "agreement_date": "Date of agreement.",
            "physical_progress": "Physical progress percentage.",
            "Financial Work Progress": "Financial work progress percentage.",
            "agency_name": "Executing agency.",
            "work_status": "Current project status."
        }
    },
    "Payment_given_to_farmers_for_crops_loss_blockwise_yearwise": {
    "description": "Block-wise and year-wise data on payments disbursed to farmers for crop loss, including demographic and scheme-related attributes.",
    "columns": {
        "sector_name": "Name of the sector to which the data belongs.",
        "state_name": "Name of the state where the payments were made.",
        "district_name": "Name of the district where the payments were made.",
        "block_name": "Name of the block where the payments were made.",
        "focus_area": "Specifies the focus area or department responsible for the data.",
        "scheme_name": "Name of the scheme under which the payment was disbursed.",
        "year": "Year in which the payment was disbursed.",
        "crop_type": "Type of crop for which the loss occurred.",
        "total_farmers": "Total number of farmers who received payment.",
        "number_of_male_farmer": "Number of male farmers who received payment.",
        "number_of_female_farmer": "Number of female farmers who received payment.",
        "number_of_backward_class_category_farmers": "Number of farmers belonging to backward class category who received payment.",
        "number_of_general_category_farmers": "Number of farmers belonging to general category who received payment.",
        "number_of_extremely_backward_class_category_farmers": "Number of farmers belonging to extremely backward class category who received payment.",
        "number_of_disciplined_caste_category_farmers": "Number of farmers belonging to scheduled caste category who received payment.",
        "number_of_disciplined_tribe_category_farmers": "Number of farmers belonging to scheduled tribe category who received payment.",
        "total_loan_paid_in_Rupees": "Total amount of loan paid (compensation) in Rupees.",
        "source": "Source of the data."
    }
},
"Payment_students_for_basic_facilities_blockwise_in_Bihar": {
    "description": "Block-wise data on payments made to students for basic facilities under various schemes in Bihar.",
    "columns": {
        "sector_name": "Name of the sector to which the scheme belongs.",
        "state_name": "Name of the state (Bihar).",
        "focus_area": "Specific focus area of the scheme or program.",
        "district_name": "Name of the district where the payments are being made.",
        "block_name": "Name of the block where the payments are being made.",
        "scheme_name": "Name of the specific scheme under which the payment is made.",
        "gender": "Gender of the beneficiary student.",
        "number_of_beneficiary": "Number of students benefiting from the payment.",
        "category_type": "Category to which the student belongs (e.g., SC, ST, OBC, General).",
        "age_group": "Age group of the beneficiary students.",
        "total_amount_in_rupees": "Total amount disbursed in Rupees.",
        "source": "Source of the data."
    }
},
"State_level_banker_Committee_loan_applied": {
    "description": "Loan application data under various schemes and departments, categorized by state, district, block, location type, and year.",
    "columns": {
        "focus_area": "The specific area or department to which the loan application pertains.",
        "state_name": "The name of the state where the loan application was submitted.",
        "department_name": "The name of the department associated with the loan application.",
        "scheme_name": "The name of the specific scheme under which the loan application was made.",
        "district_name": "The name of the district where the loan application was submitted.",
        "block_name": "The name of the block where the loan application was submitted.",
        "location_type": "The type of location (e.g., rural, urban) where the loan application originated.",
        "year": "The year in which the loan application was submitted.",
        "applied_loan_amount_in_rupees": "The amount of loan applied for, in Indian Rupees."
    }
},
"Temporary_shelters_during_winter_season": {
    "description": "Information about temporary shelters established in Bihar during the winter season, including number of shelters and beds available.",
    "columns": {
        "state_name": "Name of the state where the shelters are located (Bihar).",
        "year": "The year for which the shelter data is recorded (2024-25).",
        "focus_area": "The department or sector responsible for managing the shelters.",
        "ulbs_name": "Name of the Urban Local Body (ULB) where the shelter is located (e.g., Patna, Dehri, Danapur).",
        "number_of_shelter": "Number of temporary shelters established in the ULB.",
        "number_of_beds": "Total number of beds available in the shelters of that ULB."
    }
},
"Tri_cycle_distribution_district_wise": {
    "description": "District-wise data on tricycle distribution to physically handicapped individuals in Bihar, categorized by gender, category, and nationality.",
    "columns": {
        "focus_area": "The department or organization responsible for the tricycle distribution program.",
        "state_name": "The name of the state where the tricycle distribution took place.",
        "category_type": "The category or group to which the beneficiary belongs (e.g., social category).",
        "gender": "The gender of the tricycle recipient.",
        "nationality": "The nationality of the tricycle recipient.",
        "district_name": "The district where the tricycle was distributed.",
        "physically_handicapped_category": "Specific category of physical handicap of the recipient."
    }
},

  "Water_resource_in_bihar": {
    "description": "Data on irrigation schemes across Bihar detailing location, energy type, infrastructure, cost, water source, and defects.",
    "columns": {
      "inspectionId": "Unique identifier for the inspection record.",
      "deptId": "Identifier for the department responsible for the scheme.",
      "district_code": "Code representing the district.",
      "block_code": "Code representing the block.",
      "panchayat_code": "Code representing the panchayat.",
      "villcode": "Code representing the village.",
      "focus_area": "Department or area of focus for the data.",
      "state_name": "Name of the state (Bihar).",
      "district_name": "Name of the district.",
      "block_name": "Name of the block.",
      "panchayat_name": "Name of the panchayat.",
      "village_name": "Name of the village.",
      "scheme_name": "Name of the irrigation scheme.",
      "energy_type": "Type of energy used for the scheme (e.g., electricity, diesel).",
      "number_of_pole": "Number of poles used in the scheme's infrastructure.",
      "motor_pump_power": "Power rating of the motor pump used in the scheme.",
      "distribution_of_channel_length": "Length of the distribution channel.",
      "distribution_of_channel_width": "Width of the distribution channel.",
      "distribution_of_channel_height": "Height of the distribution channel.",
      "distribution_of_pipe_diamater": "Diameter of the distribution pipes.",
      "distribution_of_pipe_length": "Length of the distribution pipes.",
      "command_area": "Area that the scheme irrigates.",
      "scheme_approx_amount": "Approximate cost of the scheme.",
      "source_of_water": "Source of water for the scheme (e.g., river, groundwater).",
      "distributionPaenLength": "Length of the distribution paen (water channel).",
      "distributionPaenWidth": "Width of the distribution paen.",
      "distributionPaenHeight": "Height of the distribution paen.",
      "dam_length": "Length of the dam associated with the scheme.",
      "dam_height": "Height of the dam associated with the scheme.",
      "nalkup_type": "Type of nalkup (tube well).",
      "nalkoop_water_source_type": "Type of water source for the nalkup.",
      "type_of_defect_in_nalkup": "Type of defect observed in the nalkup.",
      "existingDistributionPaenLength": "Length of the existing distribution paen.",
      "existingDistributionPaenWidth": "Width of the existing distribution paen.",
      "existingDistributionPaenHeight": "Height of the existing distribution paen.",
      "nahar_length": "Length of the nahar (canal).",
      "nahar_width": "Width of the nahar (canal).",
      "nahar_height": "Height of the nahar (canal).",
      "micro_irrigation": "Details on micro-irrigation practices used.",
      "disrict_code": "Integer representation of the district code.",
      "latitude": "Latitude coordinate of the scheme's location.",
      "longitude": "Longitude coordinate of the scheme's location.",
      "distributionSystemType": "Type of distribution system used.",
      "isLandAvlblForDistChanel": "Whether land is available for distribution channel construction.",
      "checkDamHFL": "High Flood Level of the check dam.",
      "existingDistributionChannelLength": "Length of the existing distribution channel.",
      "existingDistributionChannelWidth": "Width of the existing distribution channel.",
      "existingDistributionChannelDepth": "Depth of the existing distribution channel."
    }
  },
  "Weather_shelters_under_day_nulm_scheme": {
    "description": "Details of weather shelters under the DAY-NULM scheme in Bihar for 2024-25, including capacity, type, and location.",
    "columns": {
      "ulb_name": "Name of the Urban Local Body where the shelter is located.",
      "shelter_type": "Type of shelter (e.g., New, Refurbished, O&M).",
      "shelter_address": "Physical address of the shelter.",
      "Capacity": "Maximum number of people the shelter can accommodate.",
      "type_of_scheme": "Type of scheme (DAY-NULM).",
      "state_name": "Name of the state (Bihar).",
      "district_name": "Name of the district.",
      "year": "The year for which the data is relevant (2024-25).",
      "focus_area": "Primary focus area of the shelter."
    }
  },
  "Wheat_Procurement_districtwise_yearwise_in_Bihar": {
    "description": "Wheat procurement data in Bihar categorized by district, year, farmer demographics, quantity procured, and payments.",
    "columns": {
      "Sector_name": "Sector involved in wheat procurement.",
      "year": "Year of procurement.",
      "state_name": "Name of the state (Bihar).",
      "district_name": "District where procurement occurred.",
      "block_name": "Block within the district.",
      "focus_area": "Department or sector of data collection.",
      "total_farmers": "Total number of participating farmers.",
      "number_of_male_farmers": "Count of male farmers.",
      "number_of_female_farmers": "Count of female farmers.",
      "number_of_general_category_farmers": "General category farmer count.",
      "number_of_disciplined_caste_category_farmers": "Scheduled Caste farmer count.",
      "number_of_backward_class_category_farmers": "Backward Class farmer count.",
      "number_of_minority_category_farmers": "Minority farmer count.",
      "number_of_extremely_backward_class_category_farmers": "Extremely Backward Class farmer count.",
      "total_quantity_of_wheat_in_metric_tonnes": "Quantity of wheat procured (in metric tonnes).",
      "total_amount_paid_in_rupees": "Total amount paid in Indian Rupees.",
      "source": "Data source (e.g., NIC)."
    }
  },
  "abhiyan_basera_beneficiary_year_wise_district_wise_category_wise": {
    "description": "District-wise, category-wise data on Abhiyan Basera beneficiaries in Bihar for the year 2024-25.",
    "columns": {
      "focus_area": "Department or sector for Abhiyan Basera.",
      "state_name": "State name (Bihar).",
      "year": "Financial year (2024-25).",
      "district_name": "District name.",
      "category_name": "Caste category of beneficiaries (e.g., SC, ST, EBC).",
      "number_of_beneficiary": "Number of beneficiaries in the given category."
    }
  },
  "age_wise_houses_sanctioned_under_pmay_scheme": {
    "description": "Data on houses sanctioned under PMAY in Bihar, categorized by age group, district, and financial year.",
    "columns": {
      "sector_name": "Sector associated with PMAY.",
      "district_name": "District where houses are sanctioned.",
      "age_group": "Age group of sanctioned individuals.",
      "state_name": "Name of the state (Bihar).",
      "year": "Financial year (e.g., 2023-2024).",
      "focus_area": "Department or scheme focus.",
      "scheme_name": "Scheme name (Pradhan Mantri Awas Yojana).",
      "number_of_sancation_house": "Number of houses sanctioned."
    }
  },
  "aggregate_technical_commercial_loss_year_wise": {
    "description": "Stores the aggregate technical and commercial loss percentage of electricity across different states, tracked on a yearly basis.",
    "columns": {
      "focus_area": "The specific area or department responsible for the data.",
      "state": "The name of the state for which the loss data is recorded.",
      "year": "The year for which the aggregate technical and commercial loss percentage is recorded.",
      "aggregate_technical_commercial_loss_percentage": "The percentage of electricity loss due to technical and commercial factors."
    }
  },
  "agricultural_administration_buildings_district_wise": {
    "description": "Stores district-wise data about agricultural administration buildings in Bihar, including the number of panchayats, government buildings, and rented buildings.",
    "columns": {
      "focus_area": "The department or sector to which the data pertains (likely Agriculture).",
      "year": "The year the data was collected or is relevant to.",
      "state_name": "The name of the state (Bihar in this case).",
      "district_name": "The name of the district in Bihar.",
      "total_panchayats": "The total number of panchayats in the specified district.",
      "govt_buildings_in_number": "The number of government-owned agricultural administration buildings in the specified district.",
      "rented_buildings_in_number": "The number of rented agricultural administration buildings in the specified district."
    }
  },
  "agriculture_equipment_subsidy_bihar": {
    "description": "Stores data on government subsidies for agricultural equipment in Bihar, detailing subsidy rates and maximum amounts for different equipment types and beneficiary categories (General and SC/ST/OBC).",
    "columns": {
      "focus_area": "The department or sector under which the subsidy program falls (e.g., Agriculture Department).",
      "state_name": "The name of the state where the subsidy is applicable (Bihar).",
      "year": "The year for which the subsidy information is relevant.",
      "equipment_name": "The name of the agricultural equipment for which the subsidy is provided (e.g., Chisel Cutter, Happy Seeder).",
      "subsidy_rate_general_percentage": "The percentage of subsidy provided to general category farmers.",
      "subsidy_rate_general_max_amount_in_rupees": "The maximum amount of subsidy in Rupees provided to general category farmers.",
      "subsidy_rate_sc_st_obc_percentage": "The percentage of subsidy provided to farmers belonging to SC/ST/OBC categories.",
      "subsidy_rate_sc_st_obc_max_amount_in_rupees": "The maximum amount of subsidy in Rupees provided to farmers belonging to SC/ST/OBC categories."
    }
  },
  "allotment_of_grains_district_wise_year_wise": {
    "description": "Stores data regarding the district-wise monthly allotment of grains in Bihar from 2020 to 2025, categorized under key focus areas, detailing the allocation of wheat and rice, including fortified rice, under Antyodaya Anna Yojana (AAY) and Priority Household (PHH) schemes.",
    "columns": {
      "month": "Month for which the grain allotment is recorded.",
      "focus_area": "The department or scheme under which the data is collected.",
      "year": "Year for which the grain allotment is recorded (from 2020 to 2025).",
      "district_name": "Name of the district in Bihar for which the grain allotment is recorded.",
      "antyodaya_anna_yojana_wheat_in_kgs": "Quantity of wheat allotted under the Antyodaya Anna Yojana (AAY) scheme, measured in kilograms.",
      "antyodaya_anna_yojana_rice_in_kgs": "Quantity of rice allotted under the Antyodaya Anna Yojana (AAY) scheme, measured in kilograms.",
      "antyodaya_anna_yojana_fortifiedrice_in_kgs": "Quantity of fortified rice allotted under the Antyodaya Anna Yojana (AAY) scheme, measured in kilograms.",
      "priority_household_wheat_in_kgs": "Quantity of wheat allotted under the Priority Household (PHH) scheme, measured in kilograms.",
      "priority_household_rice_in_kgs": "Quantity of rice allotted under the Priority Household (PHH) scheme, measured in kilograms.",
      "priority_household_fortified_rice_in_kgs": "Quantity of fortified rice allotted under the Priority Household (PHH) scheme, measured in kilograms.",
      "total_wheat_in_kgs": "Total quantity of wheat allotted, combining AAY and PHH schemes, measured in kilograms.",
      "total_rice_in_kgs": "Total quantity of rice allotted, combining AAY and PHH schemes, measured in kilograms.",
      "total_fortified_rice_in_kgs": "Total quantity of fortified rice allotted, combining AAY and PHH schemes, measured in kilograms."
    }
  },
  "application_details_service_wise": {
    "description": "Stores data on application statistics for various public services offered in Bihar through the \"Service Plus\" platform, including the number of applications received, approved (within and after timeline), rejected (within and after timeline), pending, and expired, categorized by service type.",
    "columns": {
      "service_name": "Name of the public service offered (e.g., BC/EBC(NCL), BIRTH REGISTRATION, CASTE certificates).",
      "total_received_applications": "Total number of applications received for the specified service.",
      "total_approved_applications": "Total number of applications approved for the specified service.",
      "total_approved_withintimeline_applications": "Total number of applications approved within the defined timeline for the specified service.",
      "total_approved_aftertimeline_applications": "Total number of applications approved after the defined timeline for the specified service.",
      "total_rejected_applications": "Total number of applications rejected for the specified service.",
      "total_rejected_withintimeline_applications": "Total number of applications rejected within the defined timeline for the specified service.",
      "total_rejected_aftertimeline_applications": "Total number of applications rejected after the defined timeline for the specified service.",
      "total_pending_applications": "Total number of applications currently pending for the specified service.",
      "total_expired_applications": "Total number of applications that have expired for the specified service.",
      "state_name": "Name of the state where the service is offered (Bihar).",
      "focus_area": "The department or sector under which the data has been collected and stored."
    }
  },
  "area_of_crop_irrigation_yearwise_trend_Bihar": {
    "description": "Stores data on the gross area under irrigation for various crops in Bihar, from 2016-17 to 2020-21.",
    "columns": {
      "sector_name": "Name of the sector to which the crop belongs.",
      "sector_id": "Unique identifier for the sector.",
      "focus_area": "Specific area of focus or department responsible for the data.",
      "crop_name": "Name of the crop.",
      "year": "Year of data collection (e.g., 2016-17).",
      "area_under_irrigation_in_hectares": "Area under irrigation for the specific crop in hectares.",
      "crop_unit": "Unit of measurement for the crop (likely Hectares, but this clarifies it).",
      "source": "Source of the data (e.g., Directorate of Economics and Statistics, Patna, Bihar)."
    }
  },
  "arrests_seized_liquor_seized_vehicles_district_wise_year_wise": {
    "description": "Contains district-wise statistics on prohibition and excise enforcement activities related to illegal liquor in Bihar from 2016 to 2024, including raids, arrests, seizures of liquor and vehicles.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or sector focus (Prohibition and Excise).",
      "year": "Year of data collection (2016-2024).",
      "district_name": "Name of the district in Bihar.",
      "department_conducting_raids": "Name of the department that conducted the raids.",
      "total_raids_conducted": "Total number of raids conducted.",
      "total_cases_registered": "Total number of cases registered related to illegal liquor.",
      "total_arrested_people": "Total number of people arrested in connection with illegal liquor.",
      "seized_illegal_country_made_liquor_in_litres": "Amount of seized illegal country-made liquor in litres.",
      "seized_illegal_foreign_made_liquor_in_litres": "Amount of seized illegal foreign-made liquor in litres.",
      "seized_total_liquor_in_litres": "Total amount of seized illegal liquor (country-made and foreign-made) in litres.",
      "seized_total_vehicles": "Total number of vehicles seized.",
      "seized_two_wheeler_vehicles": "Number of two-wheeler vehicles seized.",
      "seized_three_wheeler_vehicles": "Number of three-wheeler vehicles seized.",
      "seized_four_wheeler_vehicles": "Number of four-wheeler vehicles seized.",
      "seized_trucks": "Number of trucks seized."
    }
  },
  "art_culture_youth_department_bihar_organization_structure": {
    "description": "Stores the organizational structure of the Art, Culture, and Youth Department of Bihar, including details of personnel, their designations, roles, and the department they belong to.",
    "columns": {
      "focus_area": "The specific area or sector of focus within the Art, Culture, and Youth Department.",
      "state_name": "Name of the state (Bihar).",
      "designation": "The official job title or designation of the person within the department.",
      "department_name": "The name of the specific department or sub-division within the Art, Culture, and Youth Department.",
      "person_name": "The name of the individual holding the position.",
      "role_description": "A description of the responsibilities and duties associated with the designation.",
      "year": "The year for which the organizational structure is being represented."
    }
  },
  "art_culture_youth_department_events_timeline_year_wise": {
    "description": "Stores timeline data of events organized by the Art, Culture, and Youth Department, categorized by year.",
    "columns": {
      "focus_area": "The specific area or sub-department within the Art, Culture, and Youth Department responsible for the event.",
      "state_name": "The name of the state where the event took place.",
      "event_month": "The month in which the event occurred.",
      "event_year": "The year in which the event occurred.",
      "event_description": "A textual description of the event."
    }
  },
  "auctioned_or_seized_vehicle_or_land": {
    "description": "Stores data on the number of vehicles and properties seized, auctioned, and released on penalty in Bihar from 2016 to 2024.",
    "columns": {
      "state_name": "Name of the state (Bihar in this case).",
      "focus_area": "Department or sector focus (e.g., related to law enforcement or revenue).",
      "year": "Year of data collection, ranging from 2016 to 2024.",
      "auctioned_vehicles": "Number of vehicles that were auctioned.",
      "vehicles_released_on_penalty": "Number of vehicles released after payment of a penalty.",
      "seized_premises_or_land": "Number of premises or land parcels that were seized.",
      "auctioned_premises_or_land": "Number of premises or land parcels that were auctioned.",
      "premises_or_land_released_on_penalty": "Number of premises or land parcels released after payment of a penalty."
    }
  },
  "balak_balika_protsahan_yojan_number_of_beneficiaries": {
    "description": "Stores district-wise counts of beneficiaries for the Balak Balika Protsahan Yojan scheme, specifically for students passing 10th grade with 1st division, categorized by gender and social group.",
    "columns": {
      "sector_name": "Sector to which the scheme belongs.",
      "focus_area": "Focus area of the scheme.",
      "scheme_name": "Name of the scheme (Balak Balika Protsahan Yojan).",
      "district_name": "Name of the district where the beneficiaries are located.",
      "number_of_male_beneficiaries": "Number of male students who are beneficiaries.",
      "number_of_female_beneficiaries": "Number of female students who are beneficiaries.",
      "number_of_economically_backward_classes": "Number of beneficiaries belonging to economically backward classes.",
      "number_of_general": "Number of beneficiaries belonging to the general category.",
      "number_of_scheduled_caste": "Number of beneficiaries belonging to the scheduled caste.",
      "number_of_backward_class": "Number of beneficiaries belonging to the backward class.",
      "number_of_scheduled_tribe": "Number of beneficiaries belonging to the scheduled tribe.",
      "number_of_minorities": "Number of beneficiaries belonging to minority communities."
    }
  },
  "beneficiary_of_Aapda_Sampoorti": {
    "description": "Stores data on beneficiaries of the \"Aapda Sampoorti\" scheme in Bihar, tracking individuals who receive disaster relief and rehabilitation assistance, categorized by administrative level, age, and other relevant criteria.",
    "columns": {
      "state_name": "Name of the state (Bihar in this case).",
      "focus_area": "Indicates the specific department or area of focus within the scheme.",
      "district_name": "Name of the district where the beneficiary resides.",
      "block_name": "Name of the block where the beneficiary resides.",
      "panchayat_name": "Name of the panchayat where the beneficiary resides.",
      "category_name": "Category or classification of the beneficiary based on specific criteria related to the scheme.",
      "area_type": "Type of area (e.g., rural, urban) where the beneficiary resides.",
      "beneficiary_age": "Age of the beneficiary."
    }
  },
  "bihar_archaeological_sites_district_location_year_wise": {
    "description": "Stores information about archaeological sites and historic monuments in Bihar, including their location, description, and the district they are located in.",
    "columns": {
      "focus_area": "The specific area or department that the site falls under.",
      "state_name": "The name of the state where the archaeological site is located (Bihar).",
      "site_name": "The name of the archaeological site or historic monument.",
      "location": "Specific location details of the archaeological site.",
      "site_description": "A description of the archaeological site or historic monument.",
      "district_name": "The name of the district in Bihar where the site is located.",
      "year": "The year associated with the site (e.g., year of discovery, construction, or significance)."
    }
  },
  "bihar_archaeology_and_museums_related_schemes_year_wise_budget": {
    "description": "Stores year-wise budget allocations for various schemes related to archaeology and museums in Bihar for the financial years 2023-24 and 2024-25.",
    "columns": {
      "focus_area": "The specific area of focus within archaeology and museums that the scheme addresses.",
      "state_name": "Name of the state (Bihar).",
      "scheme_name": "Name of the specific scheme related to archaeology and museums.",
      "budget_type": "Type of budget allocation (e.g., planned, actual).",
      "budget_value_in_lakh": "Budget allocated to the scheme, expressed in lakhs (Indian Rupees).",
      "year": "Financial year for which the budget is allocated (e.g., 2023-24, 2024-25)."
    }
  },
  "bihar_climate_resilient_agriculture_data": {
    "description": "Stores year-wise and crop-season-wise data on Bihar's climate-resilient agricultural initiatives from 2019–20 to 2023–24, including targeted and achieved production figures.",
    "columns": {
      "focus_area": "Indicates the specific area of focus for the agricultural initiative.",
      "state": "Name of the state (Bihar).",
      "year": "The year for which the data is recorded (e.g., 2019-20).",
      "crop_season": "The crop season to which the data pertains (e.g., Rabi, Kharif, Summer).",
      "targeted_districts": "The number of districts targeted by the initiative.",
      "target_in_tons": "The targeted production volume in tons.",
      "achieved_in_tons": "The actual production volume achieved in tons.",
      "achievement_percentage": "The percentage of the target achieved."
    }
  },
  "bihar_dams_operational_information": {
    "description": "Stores operational information about dams in Bihar, including location, structural details, and capacity.",
    "columns": {
      "name_of_dam": "Name of the dam.",
      "latitude": "Latitude coordinate of the dam's location.",
      "longitude": "Longitude coordinate of the dam's location.",
      "year": "Year of dam construction or operational data.",
      "river": "Name of the river on which the dam is built.",
      "district": "District in Bihar where the dam is located.",
      "height_above_lowest_foundation_level_in_meters": "Height of the dam above its lowest foundation level, measured in meters.",
      "dam_length_in_meters": "Length of the dam structure, measured in meters.",
      "gross_storage_capacity_in_1000m3": "Total storage capacity of the dam's reservoir, measured in 1000 cubic meters.",
      "reservoir_area_in_1000m2": "Surface area of the dam's reservoir, measured in 1000 square meters.",
      "effective_storage_capacity_in_1000m3": "Usable or functional storage capacity of the dam's reservoir, measured in 1000 cubic meters.",
      "designed_spillway_capacity_in_cubic_meters_per_second": "Maximum discharge capacity of the dam's spillway, measured in cubic meters per second."
    }
  },
  "bihar_district_wise_shooting_locations": {
    "description": "Contains information about locations suitable for film and photography shoots in various districts of Bihar.",
    "columns": {
      "focus_area": "Specifies the department or sector that collected or manages the data.",
      "year": "Year when the shooting location data was recorded or assessed.",
      "state_name": "Name of the state where the shooting location is situated (Bihar).",
      "district_name": "Name of the district in Bihar where the shooting location is present.",
      "shooting_location": "Specific location within the district that is suitable for shooting (films, photography, etc.)."
    }
  },
  "bihar_electricity_board_operational_performance_year_wise": {
    "description": "Stores year-wise operational performance data for the Bihar Electricity Board, including details on various operational aspects and their corresponding values and units.",
    "columns": {
      "focus_area": "The specific area of focus within the Bihar Electricity Board's operations (e.g., Generation, Distribution).",
      "state_name": "Name of the state for which the data is recorded (Bihar).",
      "particulars": "Specific operational parameter or metric being tracked (e.g., Total Power Generated, Distribution Losses).",
      "year": "The year to which the operational performance data pertains.",
      "value": "The measured value for the specified particular in the given year.",
      "unit": "The unit of measurement for the 'value' column (e.g., MW, %, kWh)."
    }
  },
  "bihar_hall_art_gallery_reservation_details": {
    "description": "Stores reservation details for art galleries and halls in Bihar, including capacity, deposit amount, and reservation fees.",
    "columns": {
      "focus_area": "The department or sector under which the data is collected.",
      "year": "The year for which the reservation details are recorded.",
      "state_name": "The name of the state (Bihar).",
      "district_name": "The name of the district where the hall or gallery is located.",
      "location": "Specific location of the hall or art gallery.",
      "description": "A description of the hall or art gallery.",
      "capacity": "The seating or holding capacity of the hall or art gallery.",
      "deposit_amount_in_rupees": "The deposit amount required for reservation in Indian Rupees.",
      "reservation_fee_per_day_in_rupees": "The reservation fee charged per day in Indian Rupees."
    }
  },
  "bihar_irrigation_data": {
    "description": "Stores historical irrigation data for Bihar, providing details on irrigation targets and achievements for the Kharif, Rabi, and Hot Weather seasons, reported annually.",
    "columns": {
      "financial_year": "The financial year for which the irrigation data is recorded (e.g., 1987-88 to 2021-22).",
      "potential_created_in_thousand_hectare": "The potential irrigation capacity created, measured in thousands of hectares.",
      "kharif_target_in_thousand_hectare": "The irrigation target for the Kharif season, measured in thousands of hectares.",
      "kharif_irrigation_in_thousand_hectare": "The actual irrigation achieved during the Kharif season, measured in thousands of hectares.",
      "kharif_sudkar_in_thousand_hectare": "Adjustment or reduction to the Kharif target, measured in thousands of hectares.",
      "rabbi_target_in_thousand_hectare": "The irrigation target for the Rabi season, measured in thousands of hectares.",
      "rabbi_irrigation_in_thousand_hectare": "The actual irrigation achieved during the Rabi season, measured in thousands of hectares.",
      "rabbi_sudkar_in_thousand_hectare": "Adjustment or reduction to the Rabi target, measured in thousands of hectares.",
      "hot_weather_target_in_thousand_hectare": "The irrigation target for the Hot Weather season, measured in thousands of hectares.",
      "hot_weather_irrigation_in_thousand_hectare": "The actual irrigation achieved during the Hot Weather season, measured in thousands of hectares.",
      "hot_weather_sudkar_in_thousand_hectare": "Adjustment or reduction to the Hot Weather target, measured in thousands of hectares.",
      "total_irrigation_in_thousand_hectare": "The total irrigation achieved across all seasons, measured in thousands of hectares.",
      "total_sudkar_in_thousand_hectare": "The total adjustments or reductions to the irrigation targets across all seasons, measured in thousands of hectares."
    }
  },
  "bihar_monuments_district_wise_year_wise_details": {
    "description": "Stores district-wise and year-wise details of monuments in Bihar, including their names and locations.",
    "columns": {
      "focus_area": "The department or area of focus for the data collection.",
      "state_name": "Name of the state (Bihar).",
      "year": "Year the monument data was recorded or is relevant to.",
      "district_name": "Name of the district in Bihar where the monument is located.",
      "monument_name": "Name of the monument.",
      "monument_location": "Specific location or address of the monument."
    }
  },
  "bihar_museums_data_with_ownership_and_highlights": {
    "description": "Stores information about museums located in Bihar, including their ownership, location details, and highlights of their exhibits.",
    "columns": {
      "focus_area": "The department or sector to which the museum data pertains.",
      "state_name": "The name of the state where the museum is located (Bihar).",
      "year": "The year of data collection or reporting.",
      "museum_name": "The name of the museum.",
      "district_name": "The name of the district where the museum is located.",
      "location": "Specific location details of the museum.",
      "established_year": "The year the museum was established or founded.",
      "highlights": "Key features, exhibits, or attractions of the museum.",
      "ownership": "The type of ownership or governing body of the museum (e.g., Government, Private)."
    }
  },
  "bihar_state_disability_pension_district_wise_year_wise": {
    "description": "Stores district-wise and year-wise data on the Bihar State Disability Pension scheme, including beneficiary details, disbursement amounts, and transaction information at various administrative levels.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or sector focus (e-labharthi scheme).",
      "year": "Year of data collection for the disability pension scheme.",
      "district_name": "Name of the district in Bihar.",
      "block_name": "Name of the block within the district.",
      "panchayat_name": "Name of the panchayat within the block.",
      "village_name": "Name of the village within the panchayat.",
      "benefit_transfer_mode": "Mode of benefit transfer (e.g., direct benefit transfer).",
      "amount": "Amount of pension disbursed.",
      "no_of_beneficiaries_transactions": "Number of beneficiaries or transactions related to the pension disbursement."
    }
  },
  "bihar_state_disability_pension_progress_report": {
    "description": "Stores data on the progress of the Bihar State Disability Pension scheme, tracking applications received, pending at various stages (DEO verification, panchayat verification, provisional verification, error correction, approval), approved, and rejected applications across different districts of Bihar.",
    "columns": {
      "year": "Year for which the disability pension progress data is recorded.",
      "state_name": "Name of the state (Bihar).",
      "focus_area": "The department or area of focus related to the data.",
      "scheme_name": "Name of the disability pension scheme.",
      "district_name": "Name of the district in Bihar.",
      "total_number_of_applications_received": "Total number of applications received for the disability pension scheme in the district.",
      "pending_applications_with_deo": "Number of applications pending with the Data Entry Operator (DEO) for verification.",
      "pending_applications_for_panchayat_verification": "Number of applications pending for verification at the panchayat level.",
      "pending_applications_for_provisional_verification": "Number of applications pending for provisional verification.",
      "new_pending_applications_within_district": "Number of newly pending applications within the district.",
      "pending_applications_for_error_correction": "Number of applications pending for error correction.",
      "new_and_error_correction_pending_applications": "Number of applications that are either new or pending for error correction.",
      "pending_applications_for_approval": "Number of applications pending final approval.",
      "approved_applications": "Number of applications that have been approved for the disability pension.",
      "rejected_applications": "Number of applications that have been rejected for the disability pension."
    }
  },
  "block_wise_panchayat_wise_damaged_crops": {
    "description": "Stores data about damaged crops in Bihar, categorized by block, panchayat, and revenue thana, including the area affected.",
    "columns": {
      "block_name": "Name of the block where the crop damage occurred.",
      "panchayat_name": "Name of the panchayat where the crop damage occurred.",
      "revenue_thana_name": "Name of the revenue thana associated with the affected area.",
      "damaged_crop": "Type of crop that has been damaged (e.g., wheat).",
      "state_name": "Name of the state where the data is recorded (Bihar).",
      "focus_area": "Department or sector focus (likely Agriculture).",
      "area_in_acre": "Area of the damaged crop measured in acres."
    }
  },
  "blocks_ghats_kilns_mineral_wise": {
    "description": "Stores data on the number of operational blocks, ghats, and kilns associated with different minerals in various districts of Bihar.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or sector focus area (e.g., Mining).",
      "mineral": "Type of mineral being extracted or processed (e.g., sand, limestone).",
      "category": "Category of the mineral (e.g., Minor Minerals, Major Minerals).",
      "district_name": "Name of the district where the mineral resources are located.",
      "number_of_blocks": "Number of operational blocks associated with the specific mineral in the district.",
      "number_of_ghats": "Number of ghats (riverbanks or access points) used for mineral extraction or transportation in the district.",
      "number_of_kilns": "Number of kilns used for processing the mineral in the district."
    }
  },
  "brick_kilns_district_wise": {
    "description": "Stores district-wise data on the number of brick kilns in Bihar for the financial year 2023-24, providing insights into the distribution of brick production across the state.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or sector the data falls under.",
      "district_name": "Name of the district in Bihar.",
      "number_of_brick_kilns": "Number of brick kilns in the specified district.",
      "financial_year": "The financial year for which the data is recorded (2023-24)."
    }
  },
  "building_construction_measurement_book_records_year_wise": {
    "description": "Stores records of measurement book entries for building construction projects under the Building Construction Department in Bihar, including project details, recorded amounts, and entry dates.",
    "columns": {
      "focus_area": "Department or sector under which the project falls (e.g., Building Construction Department).",
      "state_name": "Name of the state where the project is located (Bihar).",
      "project_work_id": "Unique identifier for the specific project work.",
      "amount_recorded_in _measurement_book_in_rupees": "Amount recorded in the measurement book for the project work, in Indian Rupees.",
      "measurement_book_entry_year": "Year in which the measurement book entry was made.",
      "measurement_book_entry_month": "Month in which the measurement book entry was made.",
      "measurement_book_entry_day": "Day on which the measurement book entry was made."
    }
  },
  "building_project_funding_records_departmentwise": {
    "description": "Stores detailed records of funding, budget, and project information for building construction projects undertaken by the Building Construction Department of Bihar for various departments.",
    "columns": {
      "focus_area": "The department or sector to which the building construction project belongs.",
      "state_name": "The name of the state where the project is being carried out (Bihar).",
      "department_name": "The specific department for which the building construction project is being executed.",
      "project_description": "A textual description of the building construction project.",
      "approved_budget_amount_in_rupees": "The total budget approved for the project, in Indian Rupees.",
      "allocated_funds_in_rupees": "The amount of funds that have been allocated to the project, in Indian Rupees.",
      "requested_funds_in_rupees": "The amount of funds that have been requested for the project, in Indian Rupees.",
      "is_payment_pending": "Indicates whether payment for the project is currently pending (Yes/No or similar).",
      "is_record_reviewed": "Indicates whether the record has been reviewed (Yes/No or similar).",
      "year": "The year in which the record was created or is relevant to.",
      "record_month_name": "The month in which the record was created.",
      "record_day": "The day of the month on which the record was created."
    }
  },
  "business_overview_of_vegfed_district_wise_year_wise": {
    "description": "Stores data regarding the business overview of the VEGFED initiative in Bihar, providing details on vegetable sales and revenue generated across districts on a yearly basis.",
    "columns": {
      "focus_area": "The specific area or department within VEGFED responsible for the data.",
      "state_name": "Name of the state where VEGFED operates (Bihar).",
      "district_name": "Name of the district in Bihar where vegetables are sold.",
      "year": "The year for which the sales and revenue data is recorded (2021-22 to 2024-25).",
      "vegetables_sold_in_metric_tons": "Amount of vegetables sold, measured in metric tons.",
      "revenue_generated_in_rupee": "The revenue generated from vegetable sales, measured in Indian Rupees."
    }
  },
  "call_center_based_raids_arrests_district_wise_year_wise": {
    "description": "Stores district-wise data on complaints received by call centers, the resulting raids conducted, and arrests made by Bihar's Prohibition and Excise department from 2018 to 2024.",
    "columns": {
      "state_name": "Name of the state (Bihar in this case).",
      "focus_area": "Department or area of focus (Prohibition and Excise).",
      "district_name": "Name of the district in Bihar.",
      "type_of_raid": "Type or description of the raid conducted.",
      "year": "Year in which the complaints, raids, and arrests occurred (2018-2024).",
      "total_complaints": "Total number of complaints received by the call center.",
      "number_of_raids": "Number of raids conducted based on the complaints.",
      "number_of_arrests": "Number of arrests made as a result of the raids."
    }
  },
  "cattle_breed_population_district_wise_in_bihar": {
    "description": "Stores district-wise cattle population data in Bihar, categorized by breed, with population figures sourced from the Livestock Population Breedwise survey of 2013.",
    "columns": {
      "sector_name": "Name of the sector to which the data belongs.",
      "sector_id": "ID of the sector.",
      "focus_area": "Specifies the area of focus for the data collection.",
      "cattle_name": "Name of the cattle breed (e.g., Bachaur, Hairana, Holstein Friesian exotic and crossbred, jersery and exotic crossbred, murrah, sahiwal and surti).",
      "state_name": "Name of the state (Bihar).",
      "district_name": "Name of the district in Bihar.",
      "cattle_item": "Type of cattle related item (Population in this case).",
      "cattle_value": "Population value for the corresponding cattle breed in the district.",
      "cattle_unit": "Unit of measurement for the cattle value (Number).",
      "source": "Source of the data (Livestock Population Breedwise, Based on Breed Survey, 2013, Department of Animal Husbandry, Dairying and Fisheries, Govt. of India).",
      "year": "Year of the data collection (2013)."
    }
  },
  "cattle_milk_production_district_wise_bihar": {
    "description": "Stores data regarding milk production by cattle type (bovine, buffalo, crossbreed, indigenous) in different districts of Bihar for the year 2017-18.",
    "columns": {
      "sector_name": "Name of the sector under which the data is collected.",
      "sector_id": "ID of the sector under which the data is collected.",
      "focus_area": "Indicates the department or area of focus for the data.",
      "cattle_name": "Type of cattle for which milk production is recorded (e.g., Bovine, Buffalo, Crossbreed, Indigenous).",
      "year": "The year for which the milk production data is recorded (2017-18).",
      "cattle_item": "Specific item related to cattle (likely related to type or breed clarification).",
      "state_name": "Name of the state (Bihar).",
      "district_name": "Name of the district in Bihar.",
      "milk_production": "Amount of milk produced.",
      "unit": "Unit of measurement for milk production (Million tonnes).",
      "source": "Source of the data (Integrated Sample Survey Reports, Department of Animal Husbandry & Dairying, Government of Bihar)."
    }
  },
  "census_2011_industrial_category_main_workers_age_wise_details": {
    "description": "Contains information about the number of main workers in rural areas, categorized by age group, gender (males and females), and industrial category, based on the 2011 census data.",
    "columns": {
      "state_name": "Name of the state.",
      "district_name": "Name of the district.",
      "year": "Year of the census data (2011).",
      "focus_area": "Indicates the area of focus or data collection (likely related to census operations).",
      "area_type": "Type of area (e.g., rural, urban, or combined).",
      "age_group": "Age group of the workers (e.g., 15-19, 20-24, etc.).",
      "cultivators_males": "Number of male main workers engaged as cultivators.",
      "cultivators_females": "Number of female main workers engaged as cultivators.",
      "agricultural_labourers_males": "Number of male main workers engaged as agricultural labourers.",
      "agricultural_labourers_females": "Number of female main workers engaged as agricultural labourers.",
      "forestry_and_fishing_males": "Number of male main workers engaged in forestry and fishing activities.",
      "forestry_and_fishing_females": "Number of female main workers engaged in forestry and fishing activities.",
      "mining_and_quarrying_males": "Number of male main workers engaged in mining and quarrying activities.",
      "mining_and_quarrying_females": "Number of female main workers engaged in mining and quarrying activities.",
      "hhi_manufacturing_males": "Number of male main workers engaged in household industry (HHI) manufacturing.",
      "hhi_manufacturing_females": "Number of female main workers engaged in household industry (HHI) manufacturing.",
      "non_hhi_manufacturing_males": "Number of male main workers engaged in non-household industry (Non-HHI) manufacturing.",
      "non_hhi_manufacturing_females": "Number of female main workers engaged in non-household industry (Non-HHI) manufacturing.",
      "electricity_and_watersupply_males": "Number of male main workers engaged in electricity and water supply.",
      "electricity_and_watersupply_females": "Number of female main workers engaged in electricity and water supply.",
      "construction_males": "Number of male main workers engaged in construction activities.",
      "construction_females": "Number of female main workers engaged in construction activities.",
      "hhi_wholesale_and_retail_trade_males": "Number of male main workers engaged in household industry (HHI) wholesale and retail trade.",
      "hhi_wholesale_and_retail_trade_females": "Number of female main workers engaged in household industry (HHI) wholesale and retail trade.",
      "non_hhi_wholesale_and_retail_trade_males": "Number of male main workers engaged in non-household industry (Non-HHI) wholesale and retail trade.",
      "non_hhi_wholesale_and_retail_trade_females": "Number of female main workers engaged in non-household industry (Non-HHI) wholesale and retail trade.",
      "transportation_and_storage_males": "Number of male main workers engaged in transportation and storage.",
      "transportation_and_storage_females": "Number of female main workers engaged in transportation and storage.",
      "accomodation_and_food_service_males": "Number of male main workers engaged in accommodation and food service activities.",
      "accomodation_and_food_service_females": "Number of female main workers engaged in accommodation and food service activities.",
      "hhi_information_and_communication_males": "Number of male main workers engaged in household industry (HHI) information and communication.",
      "hhi_information_and_communication_females": "Number of female main workers engaged in household industry (HHI) information and communication.",
      "non_hhi_information_and_communication_males": "Number of male main workers engaged in non-household industry (Non-HHI) information and communication.",
      "non_hhi_information_and_communication_females": "Number of female main workers engaged in non-household industry (Non-HHI) information and communication.",
      "financial_real_estate_professional_males": "Number of male main workers engaged in financial, real estate, and professional activities.",
      "financial_real_estate_professional_females": "Number of female main workers engaged in financial, real estate, and professional activities.",
      "administrative_public_defence_males": "Number of male main workers engaged in administrative, public, and defence services.",
      "administrative_public_defence_females": "Number of female main workers engaged in administrative, public, and defence services.",
      "education_human_health_males": "Number of male main workers engaged in education and human health services.",
      "education_human_health_females": "Number of female main workers engaged in education and human health services.",
      "hhi_arts_otherservices_males": "Number of male main workers engaged in household industry (HHI) arts and other services.",
      "hhi_arts_otherservices_females": "Number of female main workers engaged in household industry (HHI) arts and other services.",
      "non_hhi_arts_otherservices_males": "Number of male main workers engaged in non-household industry (Non-HHI) arts and other services.",
      "non_hhi_arts_otherservices_females": "Number of female main workers engaged in non-household industry (Non-HHI) arts and other services."
    }
  },
  "census_2011_industrial_category_main_workers_educational_wise": {
    "description": "Stores data on the occupational distribution of workers in various states for the year 2011, categorized by gender, educational level (literate/illiterate), area type (rural/urban), and industry.",
    "columns": {
      "state_name": "Name of the state.",
      "district_name": "Name of the district.",
      "year": "Year of the census data (2011).",
      "focus_area": "Indicates the focus area of the data collection, likely related to census operations.",
      "area_type": "Type of area, either rural or urban.",
      "literacy_status": "Literacy status of the workers (literate or illiterate).",
      "cultivators_males": "Number of male cultivators.",
      "cultivators_females": "Number of female cultivators.",
      "agricultural_labourers_males": "Number of male agricultural laborers.",
      "agricultural_labourers_females": "Number of female agricultural laborers.",
      "forestry_and_fishing_males": "Number of males working in forestry and fishing.",
      "forestry_and_fishing_females": "Number of females working in forestry and fishing.",
      "mining_and_quarrying_males": "Number of males working in mining and quarrying.",
      "mining_and_quarrying_females": "Number of females working in mining and quarrying.",
      "hhi_manufacturing_males": "Number of males working in household industry manufacturing.",
      "hhi_manufacturing_females": "Number of females working in household industry manufacturing.",
      "non_hhi_manufacturing_males": "Number of males working in non-household industry manufacturing.",
      "non_hhi_manufacturing_females": "Number of females working in non-household industry manufacturing.",
      "electricity_and_watersupply_males": "Number of males working in electricity and water supply.",
      "electricity_and_watersupply_females": "Number of females working in electricity and water supply.",
      "construction_males": "Number of males working in construction.",
      "construction_females": "Number of females working in construction.",
      "hhi_wholesale_and_retail_trade_males": "Number of males working in household industry wholesale and retail trade.",
      "hhi_wholesale_and_retail_trade_females": "Number of females working in household industry wholesale and retail trade.",
      "non_hhi_wholesale_and_retail_trade_males": "Number of males working in non-household industry wholesale and retail trade.",
      "non_hhi_wholesale_and_retail_trade_females": "Number of females working in non-household industry wholesale and retail trade.",
      "transportation_and_storage_males": "Number of males working in transportation and storage.",
      "transportation_and_storage_females": "Number of females working in transportation and storage.",
      "accomodation_and_food_service_males": "Number of males working in accommodation and food service activities.",
      "accomodation_and_food_service_females": "Number of females working in accommodation and food service activities.",
      "hhi_information_and_communication_males": "Number of males working in household industry information and communication.",
      "hhi_information_and_communication_females": "Number of females working in household industry information and communication.",
      "non_hhi_information_and_communication_males": "Number of males working in non-household industry information and communication.",
      "non_hhi_information_and_communication_females": "Number of females working in non-household industry information and communication.",
      "financial_real_estate_professional_males": "Number of males working in financial, real estate, and professional activities.",
      "financial_real_estate_professional_females": "Number of females working in financial, real estate, and professional activities.",
      "administrative_public_defence_males": "Number of males working in administrative, public, and defence sectors.",
      "administrative_public_defence_females": "Number of females working in administrative, public, and defence sectors.",
      "education_human_health_males": "Number of males working in education and human health.",
      "education_human_health_females": "Number of females working in education and human health.",
      "hhi_arts_otherservices_males": "Number of males working in household industry arts and other services.",
      "hhi_arts_otherservices_females": "Number of females working in household industry arts and other services.",
      "non_hhi_arts_otherservices_males": "Number of males working in non-household industry arts and other services.",
      "non_hhi_arts_otherservices_females": "Number of females working in non-household industry arts and other services."
    }
  },
  "census_2011_industrial_category_marginal_workers_age_wise": {
    "description": "Contains data on marginal workers in rural areas from the 2011 census, classified by age group, gender, and industrial category, including information on the duration of their work.",
    "columns": {
      "state_name": "Name of the state.",
      "district_name": "Name of the district.",
      "year": "Year of the census (2011).",
      "focus_area": "Indicates the focus or scope of the data collection.",
      "area_type": "Type of area (e.g., rural, urban).",
      "age_group": "Age group of the marginal workers.",
      "mgw_worked_more_three_less_six_months_males": "Number of male marginal workers who worked for more than three months but less than six months.",
      "mgw_worked_more_three_less_six_months_females": "Number of female marginal workers who worked for more than three months but less than six months.",
      "mgw_worked_less_three_months_males": "Number of male marginal workers who worked for less than three months.",
      "mgw_worked_less_three_months_females": "Number of female marginal workers who worked for less than three months.",
      "cultivators_males": "Number of male marginal workers engaged as cultivators.",
      "cultivators_females": "Number of female marginal workers engaged as cultivators.",
      "agricultural_labourers_males": "Number of male marginal workers engaged as agricultural laborers.",
      "agricultural_labourers_females": "Number of female marginal workers engaged as agricultural laborers.",
      "forestry_and_fishing_males": "Number of male marginal workers engaged in forestry and fishing.",
      "forestry_and_fishing_females": "Number of female marginal workers engaged in forestry and fishing.",
      "mining_and_quarrying_males": "Number of male marginal workers engaged in mining and quarrying.",
      "mining_and_quarrying_females": "Number of female marginal workers engaged in mining and quarrying.",
      "hhi_manufacturing_males": "Number of male marginal workers engaged in household industry (HHI) manufacturing.",
      "hhi_manufacturing_females": "Number of female marginal workers engaged in household industry (HHI) manufacturing.",
      "non_hhi_manufacturing_males": "Number of male marginal workers engaged in non-household industry (Non-HHI) manufacturing.",
      "non_hhi_manufacturing_females": "Number of female marginal workers engaged in non-household industry (Non-HHI) manufacturing.",
      "electricity_and_watersupply_males": "Number of male marginal workers engaged in electricity and water supply.",
      "electricity_and_watersupply_females": "Number of female marginal workers engaged in electricity and water supply.",
      "construction_males": "Number of male marginal workers engaged in construction.",
      "construction_females": "Number of female marginal workers engaged in construction.",
      "hhi_wholesale_and_retail_trade_males": "Number of male marginal workers engaged in household industry (HHI) wholesale and retail trade.",
      "hhi_wholesale_and_retail_trade_females": "Number of female marginal workers engaged in household industry (HHI) wholesale and retail trade.",
      "non_hhi_wholesale_and_retail_trade_males": "Number of male marginal workers engaged in non-household industry (Non-HHI) wholesale and retail trade.",
      "non_hhi_wholesale_and_retail_trade_females": "Number of female marginal workers engaged in non-household industry (Non-HHI) wholesale and retail trade.",
      "transportation_and_storage_males": "Number of male marginal workers engaged in transportation and storage.",
      "transportation_and_storage_females": "Number of female marginal workers engaged in transportation and storage.",
      "accomodation_and_food_service_males": "Number of male marginal workers engaged in accommodation and food services.",
      "accomodation_and_food_service_females": "Number of female marginal workers engaged in accommodation and food services.",
      "hhi_information_and_communication_males": "Number of male marginal workers engaged in household industry (HHI) information and communication.",
      "hhi_information_and_communication_females": "Number of female marginal workers engaged in household industry (HHI) information and communication.",
      "non_hhi_information_and_communication_males": "Number of male marginal workers engaged in non-household industry (Non-HHI) information and communication.",
      "non_hhi_information_and_communication_females": "Number of female marginal workers engaged in non-household industry (Non-HHI) information and communication.",
      "financial_real_estate_professional_males": "Number of male marginal workers engaged in financial, real estate, and professional services.",
      "financial_real_estate_professional_females": "Number of female marginal workers engaged in financial, real estate, and professional services.",
      "administrative_public_defence_males": "Number of male marginal workers engaged in administrative, public, and defence services.",
      "administrative_public_defence_females": "Number of female marginal workers engaged in administrative, public, and defence services.",
      "education_human_health_males": "Number of male marginal workers engaged in education and human health services.",
      "education_human_health_females": "Number of female marginal workers engaged in education and human health services.",
      "hhi_arts_otherservices_males": "Number of male marginal workers engaged in household industry (HHI) arts and other services.",
      "hhi_arts_otherservices_females": "Number of female marginal workers engaged in household industry (HHI) arts and other services.",
      "non_hhi_arts_otherservices_males": "Number of male marginal workers engaged in non-household industry (Non-HHI) arts and other services.",
      "non_hhi_arts_otherservices_females": "Number of female marginal workers engaged in non-household industry (Non-HHI) arts and other services."
    }
  },
  "census_2011_literacy_district_wise_age_wise": {
    "description": "Stores demographic data from the 2011 Census of India, providing a breakdown of population, gender distribution, and literacy levels at the state and district levels, categorized by age groups and rural/urban areas.",
    "columns": {
      "state_name": "Name of the state.",
      "district_name": "Name of the district.",
      "type_of_area": "Indicates whether the area is rural or urban.",
      "age": "Age group for the population data.",
      "total_population": "Total population count for the specified state, district, area type, and age group.",
      "total_males": "Total number of males for the specified state, district, area type, and age group.",
      "total_females": "Total number of females for the specified state, district, area type, and age group.",
      "total_illiterate_population": "Total number of illiterate individuals for the specified state, district, area type, and age group.",
      "total_male_illiterate_population": "Total number of illiterate males for the specified state, district, area type, and age group.",
      "total_female_illiterate_population": "Total number of illiterate females for the specified state, district, area type, and age group.",
      "total_literate_population": "Total number of literate individuals for the specified state, district, area type, and age group.",
      "total_male_literate_population": "Total number of literate males for the specified state, district, area type, and age group.",
      "total_female_literate_population": "Total number of literate females for the specified state, district, area type, and age group."
    }
  },
  "census_2011_population_state_wise_by_mother_tongue": {
    "description": "Stores the population of India as per the 2011 Census, categorized by state, mother tongue, and further divided into rural and urban populations by gender (male/female).",
    "columns": {
      "year": "The year of the census data (2011).",
      "focus_area": "The focus or department responsible for data collection (likely Census).",
      "state_name": "The name of the state in India.",
      "mother_tongue_name": "The name of the mother tongue spoken by the population.",
      "rural_males": "Number of males in the rural population speaking the specified mother tongue.",
      "rural_females": "Number of females in the rural population speaking the specified mother tongue.",
      "urban_males": "Number of males in the urban population speaking the specified mother tongue.",
      "urban_females": "Number of females in the urban population speaking the specified mother tongue."
    }
  },
  "census_2011_religion_wise_population": {
    "description": "Stores data from the 2011 Census of India, detailing population figures, literacy rates, and workforce participation across different religious communities in various regions, including rural and urban areas.",
    "columns": {
      "focus_area": "Indicates the administrative or reporting area/department responsible for the data collection.",
      "year": "The year the census data was collected (2011).",
      "district_name": "The name of the district to which the data pertains.",
      "type_of_area": "Specifies the type of area (e.g., rural, urban, municipal corporation, town panchayat).",
      "state_name": "The name of the state to which the data belongs.",
      "religion": "The religious affiliation of the population being reported (e.g., Hindu, Muslim, Christian).",
      "total_population": "The total population count for the specified religion and area.",
      "male_population": "The male population count for the specified religion and area.",
      "female_population": "The female population count for the specified religion and area.",
      "total_working_population": "The total number of working individuals for the specified religion and area.",
      "male_working_population": "The number of male working individuals for the specified religion and area.",
      "female_working_population": "The number of female working individuals for the specified religion and area."
    }
  },
  "census_2011_villages_towns_population_above_below_five_thousand": {
    "description": "Stores data about the number and population of villages with populations of 5,000 or more and towns with populations below 5,000 in various districts and sub-districts, along with rural and urban population percentages.",
    "columns": {
      "year": "The year of the census data (2011).",
      "focus_area": "Indicates the department or area of focus for the data collection.",
      "state_name": "The name of the state for which the data is recorded.",
      "district_name": "The name of the district for which the data is recorded.",
      "tashil_name": "The name of the tehsil/sub-district for which the data is recorded.",
      "number_of_vilages": "The total number of villages in the specified area.",
      "village_population_in_five_or_above_five_thousand": "The number of villages having population of 5000 or more.",
      "percentage_of_rural_population": "The percentage of the population that resides in rural areas.",
      "number_of_towns": "The total number of towns in the specified area.",
      "towns_population_below_five_thousand": "The number of towns having population of less than 5000.",
      "percentage_of_urban_population": "The percentage of the population that resides in urban areas."
    }
  },
  "census_2011_villages_towns_population_area_state_wise": {
    "description": "Contains Census 2011 data for various states, districts, and sub-districts, detailing the number of villages, towns, households, male and female populations, area, and population density.",
    "columns": {
      "year": "The year the census data was collected, which is 2011.",
      "focus_area": "The department or sector under which the census data was collected and stored.",
      "state_name": "Name of the state for which the census data is recorded.",
      "district_name": "Name of the district within the state for which the census data is recorded.",
      "sub_district": "Name of the sub-district within the district for which the census data is recorded.",
      "area_type": "Type of area, either rural or urban.",
      "number_of_villages_inhabited": "Count of inhabited villages in the specified area.",
      "number_of_villages_uninhabited": "Count of uninhabited villages in the specified area.",
      "number_of_towns": "Count of towns in the specified area.",
      "number_of_households": "Count of households in the specified area.",
      "males_population": "Number of males in the population of the specified area.",
      "females_populations": "Number of females in the population of the specified area.",
      "area_in_square_km": "Total area of the specified region in square kilometers.",
      "population_per_square_km": "Population density, representing the number of people per square kilometer in the specified area."
    }
  },
  "census_2011_villages_wise_population_size_and_class": {
    "description": "Stores census data from 2011, classifying villages by population size and providing gender-wise population statistics for each category within different sub-districts.",
    "columns": {
      "year": "Year of the census data (2011).",
      "focus_area": "Department or sector focus of the data collection (likely Census).",
      "state_name": "Name of the state.",
      "district_name": "Name of the district.",
      "sub_district_name": "Name of the sub-district.",
      "number_of_villages_less_than_200_population": "Number of villages with a population less than 200.",
      "males_less_than_200_population": "Number of males in villages with a population less than 200.",
      "females_less_than_200_population": "Number of females in villages with a population less than 200.",
      "number_of_villages_population_above_two_hundred": "Number of villages with a population above 200.",
      "males_population_above_two_hundred": "Number of males in villages with a population above 200.",
      "females_population_above_two_hundred": "Number of females in villages with a population above 200.",
      "number_of_villages_population_above_five_hundred": "Number of villages with a population above 500.",
      "males_population_above_five_hundred": "Number of males in villages with a population above 500.",
      "females_population_above_five_hundred": "Number of females in villages with a population above 500.",
      "number_of_villages_population_above_one_thousand": "Number of villages with a population above 1000.",
      "males_population_above_one_thousand": "Number of males in villages with a population above 1000.",
      "females_population_above_one_thousand": "Number of females in villages with a population above 1000.",
      "number_of_villages_population_above_two_thousand": "Number of villages with a population above 2000.",
      "males_population_above_two_thousand": "Number of males in villages with a population above 2000.",
      "females_population_above_two_thousand": "Number of females in villages with a population above 2000.",
      "number_of_villages_population_above_five_thousand": "Number of villages with a population above 5000.",
      "males_population_above_five_thousand": "Number of males in villages with a population above 5000.",
      "females_population_above_two_five_thousand": "Number of females in villages with a population above 5000. *Note: There might be a typo here and it's likely intended to be 'females_population_above_five_thousand'.",
      "number_of_villages_population_above_ten_thousand": "Number of villages with a population above 10000.",
      "males_population_above_ten_thousand": "Number of males in villages with a population above 10000.",
      "females_population_above_ten_thousand": "Number of females in villages with a population above 10000."
    }
  },
  "census_india_2011_employment_statewise_industry_wise": {
    "description": "Stores employment statistics from the Census of India 2011, categorized by state, district, and industry, including details on main and marginal workers, gender, and rural-urban distribution.",
    "columns": {
      "focus_area": "Indicates the area or department responsible for collecting the data.",
      "state_name": "Name of the state in India.",
      "district_name": "Name of the district within the state.",
      "national_industrial_classification_name": "Name of the industry based on the National Industrial Classification.",
      "total_main_workers": "Total number of main workers in the specified category.",
      "main_workers_male": "Number of male main workers in the specified category.",
      "main_workers_female": "Number of female main workers in the specified category.",
      "rural_total_main_workers": "Total number of main workers in rural areas within the specified category.",
      "rural_main_workers_male": "Number of male main workers in rural areas within the specified category.",
      "rural_main_workers_female": "Number of female main workers in rural areas within the specified category.",
      "urban_total_main_workers": "Total number of main workers in urban areas within the specified category.",
      "urban_main_workers_male": "Number of male main workers in urban areas within the specified category.",
      "urban_main_workers_female": "Number of female main workers in urban areas within the specified category.",
      "total_marginal_workers": "Total number of marginal workers in the specified category.",
      "marginal_male_workers": "Number of male marginal workers in the specified category.",
      "marginal_female_workers": "Number of female marginal workers in the specified category.",
      "rural_total_marginal_workers": "Total number of marginal workers in rural areas within the specified category.",
      "rural_marginal_male_workers": "Number of male marginal workers in rural areas within the specified category.",
      "rural_marginal_female_workers": "Number of female marginal workers in rural areas within the specified category.",
      "urban_total_marginal_workers": "Total number of marginal workers in urban areas within the specified category.",
      "urban_marginal_male_workers": "Number of male marginal workers in urban areas within the specified category.",
      "urban_marginal_female_workers": "Number of female marginal workers in urban areas within the specified category."
    }
  },
  "census_india_2011_marital_status_state_wise": {
    "description": "Stores marital status demographics from the Census of India 2011, categorized by state, district, area type, and age group, including population distribution by gender and marital status (never married, married, widowed, separated, divorced, and unspecified).",
    "columns": {
      "focus_area": "Department or sector under which the data has been collected.",
      "state_name": "Name of the state.",
      "district_name": "Name of the district.",
      "year": "Year of the census data (2011).",
      "area_type": "Type of area (e.g., Rural, Urban, Total).",
      "age_group": "Age group for the marital status data.",
      "total_population": "Total population for the specified area, age group, and marital status category.",
      "male_population": "Number of males in the specified area, age group, and marital status category.",
      "female_population": "Number of females in the specified area, age group, and marital status category.",
      "total_persons_never_married": "Total number of persons who have never been married in the specified area and age group.",
      "males_never_married": "Number of males who have never been married in the specified area and age group.",
      "females_never_married": "Number of females who have never been married in the specified area and age group.",
      "total_married_persons": "Total number of married persons in the specified area and age group.",
      "married_males": "Number of married males in the specified area and age group.",
      "married_females": "Number of married females in the specified area and age group.",
      "total_widowed_persons": "Total number of widowed persons in the specified area and age group.",
      "widowed_males": "Number of widowed males in the specified area and age group.",
      "widowed_females": "Number of widowed females in the specified area and age group.",
      "total_seperated_persons": "Total number of separated persons in the specified area and age group.",
      "seperated_males": "Number of separated males in the specified area and age group.",
      "seperated_females": "Number of separated females in the specified area and age group.",
      "total_divorced_persons": "Total number of divorced persons in the specified area and age group.",
      "divorced_males": "Number of divorced males in the specified area and age group.",
      "divorced_females": "Number of divorced females in the specified area and age group.",
      "unspecified_total_persons": "Total number of persons with unspecified marital status in the specified area and age group.",
      "unspecified_males": "Number of males with unspecified marital status in the specified area and age group.",
      "unspecified_females": "Number of females with unspecified marital status in the specified area and age group.",
    }
  },
  
  "census_india_2011_occupation_classification_statewise": {
    "description": "Stores occupational classification and workforce distribution data from the 2011 Census of India, categorized by occupation, gender, employment type, and area.",
    "columns": {
      "focus_area": "Indicates the specific area or department within the census responsible for the data collection.",
      "state_name": "Name of the state in India.",
      "district_name": "Name of the district within the state.",
      "national_classification_of_occupations_name": "Name of the occupation as per the National Classification of Occupations (NCO).",
      "area_type": "Type of area, either rural or urban.",
      "total_main_workers": "Total number of main workers in the specified category.",
      "total_male_workers": "Total number of male main workers in the specified category.",
      "total_female_workers": "Total number of female main workers in the specified category.",
      "total_employers": "Total number of employers in the specified category.",
      "male_employers": "Total number of male employers in the specified category.",
      "female_employers": "Total number of female employers in the specified category.",
      "total_employees": "Total number of employees in the specified category.",
      "male_employees": "Total number of male employees in the specified category.",
      "female_employees": "Total number of female employees in the specified category.",
      "total_single_workers": "Total number of single workers in the specified category.",
      "single_male_workers": "Total number of single male workers in the specified category.",
      "single_female_workers": "Total number of single female workers in the specified category.",
      "total_workers_having_family": "Total number of workers having family in the specified category.",
      "male_workers_having_family": "Total number of male workers having family in the specified category.",
      "female_workers_having_family": "Total number of female workers having family in the specified category."
    }
  },
  "census_india_2011_workforce_statewise": {
    "description": "Stores workforce distribution data from the Census of India 2011, categorized by state, district, and area type, including population, workforce participation, and employment status segmented by gender.",
    "columns": {
      "focus_area": "Indicates the department or sector the data pertains to (e.g., Census).",
      "state_name": "Name of the Indian state.",
      "district_name": "Name of the district within the state.",
      "area_type": "Type of area: urban or rural.",
      "year": "Year the census data was collected (2011).",
      "literacy_status": "Literacy status of the population.",
      "total_population": "Total population count.",
      "male_population": "Total male population count.",
      "female_population": "Total female population count.",
      "total_main_workers": "Total number of main workers.",
      "main_workers_male": "Number of male main workers.",
      "main_workers_female": "Number of female main workers.",
      "total_marginal_workers": "Total number of marginal workers.",
      "marginal_workers_male": "Number of male marginal workers.",
      "marginal_workers_female": "Number of female marginal workers.",
      "total_marginal_workers_seeking_work": "Total number of marginal workers seeking work.",
      "marginal_male_workers_seeking_work": "Number of male marginal workers seeking work.",
      "marginal_female_workers_seeking_work": "Number of female marginal workers seeking work.",
      "total_non_working_persons": "Total number of non-working individuals.",
      "non_working_male": "Number of non-working males.",
      "non_working_female": "Number of non-working females.",
      "total_non_working_persons_seeking_work": "Total number of non-working individuals seeking work.",
      "non_working_male_seeking_work": "Number of non-working males seeking work.",
      "non_working_female_seeking_work": "Number of non-working females seeking work."
    }
  },
  "certificate_financial_accounting_trainees_district_wise": {
    "description": "Stores information on trainees enrolled in the Bihar State-Certificate in Financial Accounting (BS-CFA) Course, including their contact details and the locations of their training centers across Bihar's districts and blocks.",
    "columns": {
      "state_name": "Name of the state where the training is conducted (Bihar).",
      "focus_name": "Specific area or department responsible for the training program.",
      "candidate_name": "Name of the trainee enrolled in the BS-CFA course.",
      "candidate_mobile_number": "Mobile phone number of the trainee.",
      "district_name": "District in Bihar where the trainee resides or is from.",
      "block_name": "Block in Bihar where the trainee resides or is from.",
      "skill_development_center_code": "Unique code or identifier for the skill development center.",
      "skill_development_center_name": "Name of the skill development center where the trainee received training.",
      "skill_development_center_district_name": "District in Bihar where the skill development center is located.",
      "skill_development_center_block_name": "Block in Bihar where the skill development center is located."
    }
  },
  "checkpost_arrests_seized_liquor_seized_vehicles_district_wise": {
    "description": "Stores data regarding enforcement activities by the Prohibition and Excise department at checkposts in various districts of Bihar, including registered cases, arrests, liquor seized, and vehicles seized, from 2016 to 2024.",
    "columns": {
      "state_name": "Name of the state where the enforcement activities took place (Bihar).",
      "focus_area": "Department or sector focus (Prohibition and Excise).",
      "year": "Year in which the enforcement activities were conducted.",
      "type_of_raid": "Type of enforcement action or raid conducted.",
      "district_name": "Name of the district where the checkpost is located.",
      "checkpost_name": "Name of the checkpost where the enforcement activities occurred.",
      "total_registered_cases": "Total number of cases registered at the checkpost.",
      "total_arrested": "Total number of individuals arrested at the checkpost.",
      "total_seized_liquor_in_litres": "Total amount of liquor seized at the checkpost, measured in litres.",
      "total_seized_vehicles": "Total number of vehicles seized at the checkpost."
    }
  },
  "children_details_year_wise_district_wise_aangan_mandey": {
    "description": "Stores year-wise and district-wise data about children registered and present in Aanganwadi centers.",
    "columns": {
      "year": "Year for which the child data is recorded.",
      "focus_area": "Department or sector under which the data has been collected and stored.",
      "state": "Name of the state where the Aanganwadi center is located.",
      "district_name": "Name of the district where the Aanganwadi center is located.",
      "block_name": "Name of the block where the Aanganwadi center is located.",
      "number_of_registered_children": "Count of children registered at the Aanganwadi center.",
      "number_of_present_children": "Count of children present at the Aanganwadi center."
    }
  },
  "civil_seva_protsahan_yojana_scst": {
    "description": "Stores the number of beneficiaries from Scheduled Castes (SC) and Scheduled Tribes (ST) under the Civil Seva Protsahan Yojana across different districts of Bihar, including details on caste, gender, and year.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "district_name": "Name of the district in Bihar.",
      "category_type": "Category of beneficiaries, either SC (Scheduled Caste) or ST (Scheduled Tribe).",
      "caste_name": "Name of the specific caste or tribe of the beneficiary.",
      "gender": "Gender of the beneficiary (Male or Female).",
      "year": "Year for which the beneficiary data is recorded (e.g., 2018).",
      "number_of_beneficiries": "Number of beneficiaries belonging to the specified caste, gender, and district."
    }
  },
  "commercial_taxes_department_collection_state_wise_year_wise": {
    "description": "Stores state-wise Goods and Services Tax (GST) collection data from the Commercial Taxes Department for the years 2017-18 to 2024-25, including revenue from Central GST, State GST, Integrated GST, CESS, and total tax revenue.",
    "columns": {
      "focus_area": "Indicates the specific area or department within the Commercial Taxes Department responsible for the data collection.",
      "state_name": "Name of the state or union territory for which the GST collection data is recorded.",
      "central_gst_in_crore_rupee": "Revenue collected from Central Goods and Services Tax, measured in crore Rupees.",
      "state_gst_in_crore_rupee": "Revenue collected from State Goods and Services Tax, measured in crore Rupees.",
      "integrated_gst_in_crore_rupee": "Revenue collected from Integrated Goods and Services Tax, measured in crore Rupees.",
      "cess_in_crore_rupee": "Revenue collected from CESS, measured in crore Rupees.",
      "total_tax_revenue_in_crore_rupee": "Total tax revenue collected, measured in crore Rupees.",
      "year": "The financial year for which the GST data is recorded (e.g., 2017-18)."
    }
  },
  "commercial_taxes_department_refund_state_wise_year_wise": {
    "description": "Stores state-wise and year-wise data on tax refunds issued by the Commercial Taxes Department, including breakdowns of Central GST, State GST, Integrated GST, and Cess, alongside total tax revenue.",
    "columns": {
      "focus_area": "Indicates the specific department or area within the Commercial Taxes Department responsible for the data.",
      "state_name": "Name of the Indian state or union territory for which the tax refund data is recorded.",
      "central_gst_in_crore_rupee": "Amount of Central Goods and Services Tax (CGST) refunded in crore rupees.",
      "state_gst_in_crore_rupee": "Amount of State Goods and Services Tax (SGST) refunded in crore rupees.",
      "integrated_gst_in_crore_rupee": "Amount of Integrated Goods and Services Tax (IGST) refunded in crore rupees.",
      "cess_in_crore_rupee": "Amount of Cess refunded in crore rupees.",
      "total_tax_revenue_in_crore_rupee": "Total tax revenue collected in crore rupees for the respective state and year.",
      "year": "Financial year for which the tax refund data is reported (e.g., 2020-21)."
    }
  },
  "commercial_taxes_igst_settlement_state_yearwise": {
    "description": "Stores state-wise data on the settlement of Integrated GST (IGST) for the years 2017-18 to 2024-25, including regular, ad hoc, and total settlement amounts processed by the Commercial Taxes Department.",
    "columns": {
      "focus_area": "Indicates the department or area responsible for the data collection and processing (Commercial Taxes Department).",
      "state_name": "Name of the state or union territory for which the IGST settlement data is recorded.",
      "year": "Fiscal year for which the IGST settlement data is recorded (e.g., 2017-18).",
      "regular_settlement_rupee_in_crore": "Amount of IGST settled through regular channels, expressed in crore rupees.",
      "adhoc_settlement_rupee_in_crore": "Amount of IGST settled through ad hoc or special arrangements, expressed in crore rupees.",
      "total_settlement_rupee_in_crore": "Total amount of IGST settled, calculated as the sum of regular and ad hoc settlements, expressed in crore rupees."
    }
  },
  "consolidated_raids_report_excise_and_police_year_wise": {
    "description": "Stores consolidated reports of raids conducted by the Excise and Police departments in Bihar from 2016 to 2024, detailing cases registered, liquor seizures, arrests, and vehicle confiscations.",
    "columns": {
      "state_name": "Name of the state where the raids were conducted (Bihar).",
      "focus_area": "Specifies the department or area of focus for the data (Excise and Police raids).",
      "year": "Year in which the raids were conducted (2016-2024).",
      "department_conducting_raid": "Name of the department that conducted the raid (Excise or Police).",
      "cases_registered": "Number of cases registered as a result of the raids.",
      "seized_countrymade_liquor_in_litres": "Quantity of country-made liquor seized during the raids, measured in litres.",
      "seized_foreign_liquor_in_litres": "Quantity of foreign liquor seized during the raids, measured in litres.",
      "total_seized_liquor_in_litres": "Total quantity of liquor seized during the raids, measured in litres.",
      "destruction_of_liquor_in_litres": "Quantity of seized liquor that was destroyed, measured in litres.",
      "number_of_arrests": "Number of arrests made during the raids.",
      "number_of_seized_vehicles": "Number of vehicles seized during the raids."
    }
  },
  "construction_of_bridges_year_wise": {
    "description": "Stores data related to bridge construction projects in Bihar, tracking the number of bridges constructed, financial turnover, income, expenses, and profit metrics from 2012-13 to 2023-24.",
    "columns": {
      "focus_area": "The department or sector under which the bridge construction project falls.",
      "state_name": "Name of the state where the bridge construction is taking place (Bihar).",
      "year": "The year in which the bridge construction data was recorded (e.g., 2012-13).",
      "number_of_bridges": "The number of bridges constructed in the given year.",
      "work_turnover_in_crore_rupee": "The financial turnover generated by the bridge construction work, measured in crore Rupees.",
      "agency_charge_or_other_income_in_crore_rupee": "Income generated by the agency from charges or other sources, measured in crore Rupees.",
      "administrative_expenditure_in_crore_rupee": "Expenses incurred on administrative tasks related to bridge construction, measured in crore Rupees.",
      "gross_profit_in_crore_rupee": "The gross profit earned from the bridge construction projects, measured in crore Rupees.",
      "net_profit_in_crore_rupee": "The net profit earned from the bridge construction projects, measured in crore Rupees."
    }
  },
  "consumption_npk_fertilizer_year_wise": {
    "description": "Stores the year-wise consumption data of NPK fertilizers in Bihar from 2018-19 to 2022-23.",
    "columns": {
      "year": "Year for which the fertilizer consumption data is recorded (e.g., 2018-19).",
      "state_name": "Name of the state (Bihar in this case).",
      "focus_area": "Department or sector focus.",
      "consumption_npk_fertilizer_in_metric_tons": "Amount of NPK fertilizer consumed in metric tons for the given year and state."
    }
  },
  "course_certificate_details": {
    "description": "Stores certificate details of trainees who participated in courses at the Bihar Institute of Public Administration and Rural Development (BIPARD), including course information, trainee details, and certificate numbers.",
    "columns": {
      "course_name": "Name of the course for which the certificate was issued.",
      "focus_area": "Indicates that the data represents 'BIPARD Course wise Certificate details'.",
      "group_name": "Name of the group or batch the trainee belonged to during the course.",
      "course_start_date": "The date on which the course started.",
      "course_end_date": "The date on which the course ended.",
      "trainee_name": "Name of the trainee who received the certificate.",
      "certificate_number": "Unique number assigned to the certificate."
    }
  },
  "crime_against_sc_st_yearwise": {
    "description": "Stores data on registered cases, criminals, and victims related to crimes against Scheduled Castes (SC) and Scheduled Tribes (ST) in Bihar, broken down by district and year (2008-2012). It details victim demographics including gender and caste.",
    "columns": {
      "focus_area": "Indicates the department or area of focus for the data collection (e.g., 'Prevention of Atrocities').",
      "state_name": "Name of the state where the crimes occurred (Bihar).",
      "year": "Year in which the crime was registered (between 2008 and 2012).",
      "district_name": "Name of the district where the crime was registered.",
      "number_of_cases_registered": "Number of crime cases registered.",
      "number_of_criminals": "Number of criminals involved in the registered cases.",
      "total_victims": "Total number of victims affected by the crimes.",
      "male_victims": "Number of male victims.",
      "female_victims": "Number of female victims.",
      "sc_victims": "Number of victims belonging to the Scheduled Castes (SC) category.",
      "st_victims": "Number of victims belonging to the Scheduled Tribes (ST) category.",
      "unknown_victims": "Number of victims whose caste is unknown or not specified."
    }
  },
  "crop_area_production_yield_seasonwise_year_and_district_in_bihar": {
    "description": "Stores district-wise and year-wise data on crop area, production, and yield for various crops in Bihar between 2012 and 2023, categorized by season.",
    "columns": {
      "sector_name": "The sector to which the data pertains (e.g., Agriculture).",
      "focus_area": "The specific area of focus within the sector.",
      "state_name": "The name of the state (Bihar).",
      "district_name": "The name of the district in Bihar.",
      "crop_name": "The name of the crop.",
      "crop_type": "The type of crop (e.g., food crop, cash crop).",
      "crop_season": "The season in which the crop is grown (e.g., Kharif, Rabi).",
      "year": "The year of data collection (2012 to 2023).",
      "crop_area_value_in_hectare": "The area under cultivation for the crop in hectares.",
      "crop_area_value_unit_in_hectare": "The unit of measurement for the crop area (hectare).",
      "crop_production_in_metric_tonne": "The total production of the crop in metric tonnes.",
      "crop_production_value_unit_in_metric_tone": "The unit of measurement for crop production (metric tonne).",
      "crop_yield_in_kg_per_hectare": "The yield of the crop in kilograms per hectare.",
      "crop_yield_value_unit_hectare_per_kg": "The unit of measurement for crop yield (hectare per kg).",
      "source": "The source of the data (e.g., Department of Agriculture)."
    }
  },
  "crop_price_yearwise_varietywise_in_Bihar_per_kg": {
    "description": "Stores year-wise crop price data in Bihar, categorized by crop name, variety, and type, with prices specified per kilogram.",
    "columns": {
      "sector_name": "Name of the sector associated with the crop data.",
      "state_name": "Name of the state (Bihar).",
      "year": "Year for which the crop price data is recorded.",
      "focus_area": "Specific area of focus related to the crop data collection.",
      "crop_name": "Name of the crop.",
      "crop_variety": "Specific variety of the crop.",
      "crop_type": "Type or category of the crop.",
      "crop_price": "Price of the crop.",
      "price_unit_per_kg": "Unit of the crop price, specified as per kilogram.",
      "source": "Source of the crop price data (Ministry of Agriculture & Farmers Welfare)."
    }
  },
  "department_of_it_skill_development_trainees_district_wise": {
    "description": "Stores district-wise trainee statistics from Bihar's State Data Centres, providing details on enrollment, training, assessment, certification, and placement outcomes.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_are": "Department or sector focus (IT Skill Development).",
      "district_name": "Name of the district in Bihar.",
      "district_code": "Code representing the district.",
      "number_of_state_data_centres": "Number of State Data Centres in the district.",
      "number_of_enrolled_candidates": "Number of candidates enrolled in training programs.",
      "number_of_dropout_candidates": "Number of candidates who dropped out of training programs.",
      "number_of_trained_candidates": "Number of candidates who completed the training programs.",
      "number_of_candidates_undergoing_training": "Number of candidates currently undergoing training.",
      "number_of_candidates_assessed": "Number of candidates who were assessed.",
      "number_of_candidates_absent_in_assessment": "Number of candidates absent during assessment.",
      "number_of_failed_candidates": "Number of candidates who failed the assessment.",
      "number_of_passed_candidates": "Number of candidates who passed the assessment.",
      "number_of_certified_candidates": "Number of candidates who received certification.",
      "number_of_reported_placement": "Number of candidates who were reported to have been placed."
    }
  },
  "department_of_it_skill_development_trainees_sector_job_role_wise": {
    "description": "Stores data on the enrollment, training, assessment, and certification outcomes of candidates in IT-ITES and Electronics sector job roles under the Department of IT in Bihar.",
    "columns": {
      "state_name": "Name of the state where the training program is conducted (Bihar).",
      "focus_area": "The department or initiative under which the data is collected (Department of IT skill development).",
      "sector": "The specific industry sector of the job role (e.g., IT-ITES, Electronics).",
      "job_role_type_one": "The primary job role being trained for (e.g., Domestic Data Entry Operator).",
      "job_role_type_two": "A secondary or more specific description of the job role, if applicable.",
      "number_of_enrolled_candidates": "Total number of candidates who initially enrolled in the training program.",
      "number_of_dropout_candidates": "Number of candidates who dropped out of the training program before completion.",
      "number_of_trained_candidates": "Number of candidates who successfully completed the training program.",
      "number_of_candidates_undergoing_training": "Number of candidates currently in the process of undergoing training.",
      "number_of_candidates_assessed": "Number of candidates who participated in the assessment process.",
      "number_of_candidates_absent_in_assessment": "Number of candidates who were absent during the assessment.",
      "number_of_failed_candidates": "Number of candidates who failed the assessment.",
      "number_of_passed_candidates": "Number of candidates who passed the assessment.",
      "number_of_certified_candidates": "Number of candidates who received certification upon successful completion of training and assessment."
    }
  },
  "department_of_it_skill_development_trainees_year_wise": {
    "description": "Stores year-wise statistics on training batches from 2017-18 to 2023-24, including enrollment, training, assessment, certification, and placement figures for candidates in IT skill development programs.",
    "columns": {
      "state_name": "Name of the state where the IT skill development training is conducted.",
      "focus_area": "Specific area or domain of IT skill development.",
      "year": "Year for which the training statistics are recorded (e.g., 2017-18, 2023-24).",
      "number_of_batches": "Number of training batches conducted in the given year.",
      "number_of_enrolled_candidates": "Number of candidates who enrolled in the training programs.",
      "number_of_trained_candidates": "Number of candidates who completed the training programs.",
      "number_of_candidates_undergoing_training": "Number of candidates currently undergoing training.",
      "number_of_candidates_assessed": "Number of candidates who were assessed after the training.",
      "number_of_certified_candidates": "Number of candidates who received certification after assessment.",
      "number_of_reported_placement": "Number of candidates who were reported to have been placed after the training and certification."
    }
  },
  "departmental_budget_requests_year_wise": {
    "description": "Contains information about budgetary allocations and requisition requests made by different departments under the Building Construction Department in Bihar across multiple years.",
    "columns": {
      "focus_area": "The specific area or sector to which the budget request pertains.",
      "state_name": "The name of the state (Bihar in this case).",
      "requisition_id": "A unique identifier for the budget requisition request.",
      "allocated_budget_amount_in_rupees": "The amount of budget allocated in Indian Rupees.",
      "requisition_department_name": "The name of the department making the budget requisition.",
      "requisition_year": "The year in which the budget requisition was made.",
      "requisition_month": "The month in which the budget requisition was made.",
      "requisition_day": "The day on which the budget requisition was made."
    }
  },
  "diesel_subsidy_district_wise_data_bihar": {
    "description": "Stores district-wise data for the Diesel Subsidy program in Bihar for the year 2022-23, including application counts, approval status, and subsidy amounts disbursed.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "year": "Year for which the data is recorded (2022-23).",
      "focus_area": "Department or sector under which the subsidy program falls.",
      "district_name": "Name of the district in Bihar.",
      "total_applications": "Total number of applications received for the diesel subsidy.",
      "AC_approved": "Number of applications approved by the AC (Agriculture Coordinator/Committee).",
      "DAO_approved": "Number of applications approved by the DAO (District Agriculture Officer).",
      "sent_to_bank": "Number of applications sent to the bank for subsidy disbursement.",
      "amount_sent_by_bank_in_rupees": "Total amount of subsidy disbursed by the bank in Indian Rupees."
    }
  },
  "district_wise_Irrigation_area": {
    "description": "Stores district-wise irrigation area data in Bihar from 2011 to 2023, including the total and net irrigated areas from various sources like government canals, private canals, ponds, tubewells, and other resources.",
    "columns": {
      "district_name": "Name of the district in Bihar.",
      "year": "Year of the irrigation data (2011-2023).",
      "focus_area": "Department or sector focus for the data collection.",
      "total_area_of_government_canal": "Total area irrigated by government canals in hectares.",
      "total_area_of_total_canal": "Total area irrigated by all canals (government and private) in hectares.",
      "total_area_of_pond": "Total area irrigated by ponds in hectares.",
      "total_area_of_tubewell": "Total area irrigated by tubewells in hectares.",
      "total_area_of_other_well": "Total area irrigated by other types of wells in hectares.",
      "total_area_of_other_resources": "Total area irrigated by other irrigation resources in hectares.",
      "total_irrigated_area": "Total irrigated area from all sources in hectares.",
      "total_area_unit": "Unit of measurement for the total area (Hectares).",
      "net_area_of_government_canal": "Net area irrigated by government canals in hectares.",
      "net_area_of_total_canal": "Net area irrigated by all canals in hectares.",
      "net_area_of_pond": "Net area irrigated by ponds in hectares.",
      "net_area_of_tubewell": "Net area irrigated by tubewells in hectares.",
      "net_area_of_other_well": "Net area irrigated by other wells in hectares.",
      "net_area_of_other_resources": "Net area irrigated by other resources in hectares.",
      "net_irrigated_area": "Net irrigated area from all sources in hectares.",
      "net_area_unit": "Unit of measurement for the net area (Hectares)."
    }
  },
  "district_wise_amenities": {
    "description": "Stores district-level data on access to electricity, improved drinking water, and sanitation facilities across several Indian states, providing percentages of the population with access to these amenities.",
    "columns": {
      "id": "Unique identifier for the record.",
      "district_name": "Name of the district.",
      "district_lgd_code": "Local Government Directory code for the district.",
      "state_name": "Name of the state.",
      "state_lgd_code": "Local Government Directory code for the state.",
      "population_with_electricity_in_percentage": "Percentage of the district's population with access to electricity.",
      "population_with_improved_drinking_water_percentage": "Percentage of the district's population with access to improved drinking water sources.",
      "population_with_improved_sanitation_facility_percentage": "Percentage of the district's population with access to improved sanitation facilities."
    }
  },
  "district_wise_asha_health_workers": {
    "description": "Stores financial allocation data related to the 'Ashwin' scheme for ASHA health workers in Bihar, specifically for the year 2024-25. It includes details about beneficiaries across different districts, blocks, and panchayats.",
    "columns": {
      "focus_area": "The department or program under which the data is categorized (likely related to health or ASHA programs).",
      "state_name": "Name of the state (Bihar in this case).",
      "district_name": "Name of the district in Bihar.",
      "block_name": "Name of the block within the district.",
      "panchayat_code": "Code identifying the panchayat.",
      "gender": "Gender of the ASHA health worker (likely Female).",
      "category": "Social category of the ASHA health worker (e.g., OBC, EBC, SC).",
      "is_minority": "Indicates whether the ASHA health worker belongs to a minority community (Yes/No).",
      "is_divyang": "Indicates whether the ASHA health worker is physically challenged (Divyang) (Yes/No).",
      "total_amount": "Total financial allocation or remuneration amount.",
      "year": "The year for which the data is recorded (2024-25)."
    }
  },
  "district_wise_bharat_net_scheme": {
    "description": "Stores district-wise data on the progress of the BharatNet scheme, tracking the number of villages planned, covered, and remaining to be covered with high-speed broadband connectivity.",
    "columns": {
      "scheme_name": "Name of the scheme (BharatNet).",
      "state_name": "Name of the state where the scheme is being implemented.",
      "district_name": "Name of the district where the scheme is being implemented.",
      "year": "Year of data collection for the scheme's progress.",
      "number_of_villages": "Total number of villages planned to be covered under the BharatNet scheme in the district.",
      "number_of_villages_covered": "Number of villages successfully connected with broadband under the scheme in the district.",
      "number_of_villages_not_covered": "Number of villages yet to be connected under the scheme in the district.",
      "unknown_status_of_villages": "Number of villages with unclear or unknown status regarding BharatNet connectivity in the district."
    }
  },
  "district_wise_common_services_centre": {
    "description": "Stores data about the number of functional Common Service Centres (CSCs) in each district, providing e-governance services in rural and remote areas.",
    "columns": {
      "scheme_name": "Name of the scheme under which the Common Service Centres are operating.",
      "state_name": "Name of the state where the Common Service Centres are located.",
      "district_name": "Name of the district where the Common Service Centres are located.",
      "year": "Year for which the number of functional Common Service Centres is recorded.",
      "number_of_functional_common_service_centre": "Number of Common Service Centres that are functional in the specified district and year."
    }
  },
  "district_wise_craftsmen_training_scheme_CTS_ITI": {
    "description": "Stores data related to the Craftsmen Training Scheme (CTS) and Industrial Training Institutes (ITIs), including trainee admissions, the number of ITIs, and scheme details, organized by district.",
    "columns": {
      "scheme_name": "Name of the Craftsmen Training Scheme.",
      "state_name": "Name of the state where the scheme is implemented.",
      "district_name": "Name of the district where the ITIs are located.",
      "year": "Year for which the data is recorded.",
      "number_of_total_trainee_admissions": "Total number of trainee admissions in ITIs.",
      "number_of_women_trainee_admissions": "Number of women trainee admissions in ITIs.",
      "number_of_scheduled_caste_trainee_admissions": "Number of trainee admissions from Scheduled Caste (SC) category in ITIs.",
      "number_of_scheduled_tribes_trainee_admissions": "Number of trainee admissions from Scheduled Tribe (ST) category in ITIs.",
      "number_of_other_backward_class_trainee_admissions": "Number of trainee admissions from Other Backward Class (OBC) category in ITIs.",
      "number_of_trainees_admitted_in_new_age_courses": "Number of trainees admitted in new-age or emerging technology courses.",
      "number_of_government_industrial_training_institutes": "Number of government-run Industrial Training Institutes in the district.",
      "number_of_private_industrial_training_institutes": "Number of privately-run Industrial Training Institutes in the district.",
      "number_of_women_exclusive_industrial_training_institutes": "Number of Industrial Training Institutes exclusively for women in the district."
    }
  },
  "district_wise_engineering_and_polytechinc_colleges_seat": {
    "description": "Stores district-wise data on seat capacity in engineering and polytechnic colleges across Bihar.",
    "columns": {
      "focus_area": "The department or sector under which the data falls.",
      "state_name": "Name of the state (Bihar).",
      "district_name": "Name of the district in Bihar.",
      "institute_name": "Name of the engineering or polytechnic college.",
      "total_seats_capacity": "Total number of seats available in the institute.",
      "year": "Year for which the seat capacity data is recorded.",
      "education_type": "Type of education, indicating whether it's engineering or polytechnic."
    }
  },
  "district_wise_fca_fpo_pacs": {
    "description": "Stores district-level data from various states in India, detailing the number of open defecation-free plus (ODF+) villages and the presence of Farmer Producer Organizations (FPO), Farmer Cooperative Societies (FCA), and Primary Agricultural Credit Societies (PACS).",
    "columns": {
      "id": "Unique identifier for the record.",
      "district_name": "Name of the district.",
      "district_lgd_code": "LGD (Local Government Directory) code of the district.",
      "state_name": "Name of the state.",
      "state_lgd_code": "LGD (Local Government Directory) code of the state.",
      "number_of_open_defecation_free_plus_villages": "Number of villages in the district that are Open Defecation Free Plus (ODF+).",
      "villages_with_fca_fpo_and_pacs": "Number of villages in the district with Farmer Cooperative Societies (FCA), Farmer Producer Organizations (FPO), and Primary Agricultural Credit Societies (PACS)."
    }
  },
  "district_wise_government_schools_2022_23_bihar": {
    "description": "Stores the number of elementary, secondary, and higher secondary government schools in each district of Bihar for the year 2022-23.",
    "columns": {
      "sector_name": "Name of the sector to which the data pertains.",
      "focus_area": "Indicates the department or area of focus for the data collection.",
      "district_name": "Name of the district in Bihar.",
      "elementary_schools": "Number of elementary government schools in the district.",
      "secondary_and_higher_secondary_schools": "Number of secondary and higher secondary government schools in the district.",
      "source": "Source of the data.",
      "year": "Year for which the data is recorded (2022-23)."
    }
  },
  "district_wise_healthcare": {
    "description": "Stores health-related statistics across various districts and states in India, focusing on metrics such as the number of functional sub-centres, primary health centres, Ayushman Bharat cards created, and authorized hospital admissions per thousand people.",
    "columns": {
      "id": "Unique identifier for the record.",
      "district_name": "Name of the district.",
      "district_lgd_code": "The Local Government Directory (LGD) code for the district.",
      "state_name": "Name of the state.",
      "state_lgd_code": "The Local Government Directory (LGD) code for the state.",
      "number_of_functional_sub_centres_per_thousand_population": "Number of functional sub-centres available per thousand population in the district.",
      "functional_primary_health_centres_per_thousand_population": "Number of functional primary health centres available per thousand population in the district.",
      "number_of_ayushman_cards_created_per_thousand_population": "Number of Ayushman Bharat cards created per thousand population in the district.",
      "number_of_authorised_hospital_admissions_per_thousand_population": "Number of authorized hospital admissions under Ayushman Bharat scheme per thousand population in the district."
    }
  },
  "district_wise_households_amenities": {
    "description": "Stores data on district-wise household amenities, specifically the percentage of households with tap water connections and clean cooking fuel, across various states in India.",
    "columns": {
      "id": "Unique identifier for each record.",
      "district_name": "Name of the district.",
      "district_lgd_code": "LGD (Local Government Directory) code for the district.",
      "state_name": "Name of the state.",
      "state_lgd_code": "LGD (Local Government Directory) code for the state.",
      "households_with_tap_water_connection_percentage": "Percentage of households in the district with tap water connections.",
      "households_using_clean_fuel_for_cooking_percentage": "Percentage of households in the district using clean fuel for cooking."
    }
  },
  "district_wise_irrigation": {
    "description": "Stores district-level statistics on groundwater extraction rates and the adoption of drip or sprinkler irrigation methods across various districts in India.",
    "columns": {
      "id": "Unique identifier for each record.",
      "district_name": "Name of the district.",
      "district_lgd_code": "LGD (Local Government Directory) code for the district.",
      "state_name": "Name of the state to which the district belongs.",
      "state_lgd_code": "LGD code for the state.",
      "stage_of_ground_water_extraction": "Percentage or level indicating the stage of groundwater extraction in the district.",
      "farmers_using_drip_or_sprinkler_irrigation": "Percentage or proportion of farmers in the district using drip or sprinkler irrigation methods."
    }
  },
  "district_wise_school_category": {
    "description": "Provides a detailed breakdown of school types across districts and blocks in Bihar for the 2023-24 academic year, categorized by the educational levels they offer.",
    "columns": {
      "sector_name": "The sector to which the data belongs.",
      "focus_area": "The specific area of focus or department responsible for the data.",
      "year": "The academic year for which the data is reported (2023-24).",
      "state_name": "The name of the state (Bihar).",
      "district_name": "The name of the district.",
      "block_name": "The name of the block within the district.",
      "number_of_primary_with_upper_primary": "The number of schools offering primary and upper primary levels (Classes 1 to 8).",
      "number_of_primary_upper_primary_and_secondary": "The number of schools offering primary, upper primary, and secondary levels (Classes 1 to 10).",
      "number_of_primary": "The number of schools offering only primary level (Classes 1 to 5).",
      "number_of_primary_with_upper_primary_and_higher_secondary": "The number of schools offering primary, upper primary, and higher secondary levels (Classes 1 to 12).",
      "number_of_secondary_with_higher_secondary": "The number of schools offering secondary and higher secondary levels (Classes 9 to 12).",
      "number_of_higher_secondary_only_junior_college": "The number of schools offering only higher secondary level or junior college (Classes 11 to 12).",
      "number_of_upper_primary_secondary_and_higher_secondary": "The number of schools offering upper primary, secondary, and higher secondary levels (Classes 6 to 12).",
      "number_of_upper_primary_only": "The number of schools offering only upper primary level (Classes 6 to 8).",
      "number_of_upper_primary_and_secondary": "The number of schools offering upper primary and secondary levels (Classes 6 to 10).",
      "number_of_secondary_only": "The number of schools offering only secondary level (Classes 9 to 10)."
    }
  },
  "district_wise_school_location": {
    "description": "Stores the number of urban, rural, and not defined schools, organized by various geographical divisions for the 2023-24 period.",
    "columns": {
      "sector_name": "Name of the sector to which the data pertains (e.g., Education).",
      "focus_area": "Specific area of focus within the sector (e.g., School Statistics).",
      "year": "Year for which the data is recorded (2023-24).",
      "state_name": "Name of the state where the schools are located.",
      "district_name": "Name of the district where the schools are located.",
      "block_name": "Name of the block where the schools are located.",
      "school_count": "Total number of schools in the specified area.",
      "urban_school": "Number of schools located in urban areas.",
      "rural_school": "Number of schools located in rural areas.",
      "not_defined_school": "Number of schools whose location (urban or rural) is not defined."
    }
  },
  "district_wise_school_recognition": {
    "description": "Stores district-wise data for the year 2023-24 on the number of schools recognized and not recognized at various levels (Pre-Primary, Primary, Upper Primary, Secondary, and Higher Secondary).",
    "columns": {
      "sector_name": "Name of the sector related to education.",
      "focus_area": "Indicates the specific focus area within the education sector.",
      "year": "The year for which the data is recorded (2023-24).",
      "state_name": "Name of the state.",
      "district_name": "Name of the district.",
      "block_name": "Name of the block within the district.",
      "number_of_school_having_pre_primary_section": "Number of schools in the block that have a pre-primary section.",
      "number_of_school_not_having_pre_primary_section_no": "Number of schools in the block that do not have a pre-primary section.",
      "number_of_school_having_primary_recognition": "Number of schools in the block that have primary recognition.",
      "number_of_school_not_having_primary_recognition": "Number of schools in the block that do not have primary recognition.",
      "number_of_school_having_upper_primary": "Number of schools in the block that have an upper primary section.",
      "number_of_school_not_having_upper_primary": "Number of schools in the block that do not have an upper primary section.",
      "number_of_school_having_secondary": "Number of schools in the block that have a secondary section.",
      "number_of_school_not_having_secondary": "Number of schools in the block that do not have a secondary section.",
      "number_of_school_having_higher_secondary": "Number of schools in the block that have a higher secondary section.",
      "number_of_school_not_having_higher_secondary": "Number of schools in the block that do not have a higher secondary section.",
      "number_of_school_having_primary_to_upper_primary": "Number of schools in the block that have primary to upper primary levels.",
      "number_of_school_not_having_primary_to_upper_primary": "Number of schools in the block that do not have primary to upper primary levels.",
      "number_of_school_having_upper_primary_to_secondary": "Number of schools in the block that have upper primary to secondary levels.",
      "number_of_school_not_having_upper_primary_to_secondary": "Number of schools in the block that do not have upper primary to secondary levels.",
      "number_of_school_having_secondary_to_higher_secondary": "Number of schools in the block that have secondary to higher secondary levels.",
      "primmary_clases_one_to_five": "Represents whether schools having primary classes from one to five.",
      "number_of_school_not_having_secondary_to_higher_secondary": "Number of schools in the block that do not have secondary to higher secondary levels."
    }
  },
  "district_wise_school_special_facilities": {
    "description": "Stores data about schools, categorized by district, focusing on special facilities related to children with special needs, shift schools, and residential school types for the year 2023-24.",
    "columns": {
      "sector_name": "Name of the sector to which the school belongs.",
      "focus_area": "Specifies the area of focus for the data collection (e.g., education).",
      "year": "The year for which the data is recorded (2023-24).",
      "state_name": "Name of the state where the schools are located.",
      "district_name": "Name of the district where the schools are located.",
      "block_name": "Name of the block where the schools are located.",
      "number_of_school_having_children_with_special_need": "Number of schools that accommodate children with special needs.",
      "number_of_school_not_having_children_with_special_need": "Number of schools that do not accommodate children with special needs.",
      "number_of_school_having_shift_school": "Number of schools that operate in shifts.",
      "number_of_school_not_having_shift_school": "Number of schools that do not operate in shifts.",
      "number_of_non_residential_school": "Number of schools that are non-residential (day schools).",
      "number_of_partially_residential_school": "Number of schools that are partially residential.",
      "number_of_completely_residential_school": "Number of schools that are completely residential (boarding schools)."
    }
  },
  "district_wise_school_streams": {
    "description": "Stores data on the availability of different academic streams (Arts, Science, Commerce, Vocational, and Other) in schools, aggregated by district, for the year 2023-24.",
    "columns": {
      "sector_name": "The sector to which the data belongs.",
      "focus_area": "The specific focus area or department responsible for the data.",
      "year": "The year to which the data pertains (2023-24).",
      "state_name": "The name of the state.",
      "district_name": "The name of the district.",
      "block_name": "The name of the block.",
      "number_of_school_having_arts_stream": "The number of schools in the specified district and block that offer an Arts stream.",
      "number_of_school_not_having_arts_stream": "The number of schools in the specified district and block that do not offer an Arts stream.",
      "number_of_school_having_science_stream": "The number of schools in the specified district and block that offer a Science stream.",
      "number_of_school_not_having_science_stream": "The number of schools in the specified district and block that do not offer a Science stream.",
      "number_of_school_having_commerce_stream": "The number of schools in the specified district and block that offer a Commerce stream.",
      "number_of_school_not_having_commerce_stream": "The number of schools in the specified district and block that do not offer a Commerce stream.",
      "number_of_school_having_vocational_stream": "The number of schools in the specified district and block that offer a Vocational stream.",
      "number_of_school_not_having_vocational_stream": "The number of schools in the specified district and block that do not offer a Vocational stream.",
      "number_of_school_having_other_streams": "The number of schools in the specified district and block that offer other academic streams (streams other than Arts, Science, Commerce, and Vocational).",
      "number_of_school_not_having_other_streams": "The number of schools in the specified district and block that do not offer other academic streams."
    }
  },
  "district_wise_school_type": {
    "description": "Stores the number of co-educational, girls', and boys' schools, categorized by district, block, and other administrative divisions for the year 2023-24.",
    "columns": {
      "sector_name": "The sector the data belongs to (e.g., Education).",
      "focus_area": "The specific area or department under which the data was collected.",
      "year": "The year for which the data is recorded (2023-24).",
      "state_name": "Name of the state to which the school data belongs.",
      "district_name": "Name of the district to which the school data belongs.",
      "block_name": "Name of the block within the district to which the school data belongs.",
      "number_of_co_educational_school": "The number of co-educational schools in the specified location.",
      "number_of_girls_school": "The number of girls' schools in the specified location.",
      "number_of_boys_school": "The number of boys' schools in the specified location."
    }
  },
  "district_wise_sown_area": {
    "description": "Stores data on the net sown area as a percentage of total geographical area and the area insured as a percentage of the net sown area for various districts across Indian states.",
    "columns": {
      "id": "Unique identifier for the record.",
      "district_name": "Name of the district.",
      "district_lgd_code": "Local Government Directory (LGD) code for the district.",
      "state_name": "Name of the state.",
      "state_lgd_code": "Local Government Directory (LGD) code for the state.",
      "net_sown_area_as_percentage_of_total_geographical_area": "The net sown area as a percentage of the total geographical area of the district.",
      "area_insured_as_percentage_of_net_sown_area": "The area insured as a percentage of the net sown area in the district."
    }
  },
  "district_wise_start_up_bihar": {
    "description": "Stores data about the distribution, approval status (SMIC), and funding (first and second seed funding) of start-ups across districts in Bihar.",
    "columns": {
      "focus_area": "The department or sector under which the start-up data is categorized.",
      "state_name": "Name of the state where the start-ups are located (Bihar).",
      "year": "Year in which the start-up data was recorded.",
      "district_name": "Name of the district in Bihar where the start-up is located.",
      "smic_approved": "Count of start-ups approved by the State Level Sanctioning and Monitoring Committee (SMIC) in the district.",
      "first_seed_funding": "Amount of first seed funding provided to start-ups in the district.",
      "second_seed_funding": "Amount of second seed funding provided to start-ups in the district."
    }
  },
  "district_wise_student_dropout": {
    "description": "Stores district-level dropout rates for boys and girls at primary, upper primary, and secondary education levels across various Indian states.",
    "columns": {
      "id": "Unique identifier for the record.",
      "district_name": "Name of the district.",
      "district_lgd_code": "Local Government Directory (LGD) code for the district.",
      "state_name": "Name of the state.",
      "state_lgd_code": "Local Government Directory (LGD) code for the state.",
      "primary_dropout_rate_girls": "Dropout rate for girls at the primary education level (e.g., percentage).",
      "primary_dropout_rate_boys": "Dropout rate for boys at the primary education level (e.g., percentage).",
      "upper_primary_dropout_rate_girls": "Dropout rate for girls at the upper primary education level (e.g., percentage).",
      "upper_primary_dropout_rate_boys": "Dropout rate for boys at the upper primary education level (e.g., percentage).",
      "secondary_dropout_rate_girls": "Dropout rate for girls at the secondary education level (e.g., percentage).",
      "secondary_dropout_rate_boys": "Dropout rate for boys at the secondary education level (e.g., percentage)."
    }
  },
  "district_wise_subject_proficiency": {
    "description": "Stores district-wise subject proficiency levels for students in Classes 3, 5, and 8 across various Indian states, focusing on the percentage of students performing at basic or below basic levels in different subjects.",
    "columns": {
      "id": "Unique identifier for the record.",
      "district_name": "Name of the district.",
      "district_lgd_code": "Local Government Directory (LGD) code for the district.",
      "state_name": "Name of the state.",
      "state_lgd_code": "Local Government Directory (LGD) code for the state.",
      "proficiency_basic_and_below_basic_language_class_three": "Percentage of students in Class 3 with basic or below basic proficiency in language.",
      "proficiency_basic_and_below_basic_mathematics_class_three": "Percentage of students in Class 3 with basic or below basic proficiency in mathematics.",
      "proficiency_basic_and_below_basic_evs_class_three": "Percentage of students in Class 3 with basic or below basic proficiency in environmental studies (EVS).",
      "proficiency_basic_and_below_basic_language_class_five": "Percentage of students in Class 5 with basic or below basic proficiency in language.",
      "proficiency_basic_and_below_basic_mathematics_class_five": "Percentage of students in Class 5 with basic or below basic proficiency in mathematics.",
      "proficiency_basic_and_below_basic_evs_class_five": "Percentage of students in Class 5 with basic or below basic proficiency in environmental studies (EVS).",
      "proficiency_basic_and_below_basic_language_class_eight": "Percentage of students in Class 8 with basic or below basic proficiency in language.",
      "proficiency_basic_and_below_basic_science_class_eight": "Percentage of students in Class 8 with basic or below basic proficiency in science.",
      "proficiency_basic_and_below_basic_mathematics_class_eight": "Percentage of students in Class 8 with basic or below basic proficiency in mathematics.",
      "proficiency_basic_and_below_basic_social_science_class_eight": "Percentage of students in Class 8 with basic or below basic proficiency in social science."
    }
  },
  "district_wise_type_of_school_management_2023_24": {
    "description": "Stores information about different types of educational institutions, categorized by district and management type, including government, private, and other specialized schools, for the year 2023-24.",
    "columns": {
      "sector_name": "Name of the sector to which the educational data belongs.",
      "focus_area": "Department or area of focus for the data collection (e.g., Education).",
      "year": "The academic year for which the data is recorded (2023-24).",
      "state_name": "Name of the state where the educational institutions are located.",
      "district_name": "Name of the district where the educational institutions are located.",
      "block_name": "Name of the block where the educational institutions are located.",
      "department_of_education": "Count or data related to schools managed or overseen by the Department of Education.",
      "private_unaided_recognized": "Count or data related to private unaided recognized schools.",
      "school_college_affiliated": "Count or data related to schools or colleges that are affiliated.",
      "unrecognized": "Count or data related to unrecognized schools.",
      "constituent_college": "Count or data related to constituent colleges.",
      "local_body": "Count or data related to schools managed by local bodies.",
      "buniyadi_school": "Count or data related to Buniyadi schools.",
      "recognized_aided_sanskrit_school": "Count or data related to recognized aided Sanskrit schools.",
      "madrasa_unaided_recognized": "Count or data related to unaided recognized Madrasas.",
      "project_girls_high_school": "Count or data related to Project Girls' High Schools.",
      "rajkiya_high_school": "Count or data related to Rajkiya High Schools.",
      "madarsa_unrecognized": "Count or data related to unrecognized Madrasas.",
      "social_welfare_department": "Count or data related to schools managed by the Social Welfare Department.",
      "madrasa_aided_recognized": "Count or data related to aided recognized Madrasas.",
      "recognized_government_unaided_sanskrit_school": "Count or data related to recognized government unaided Sanskrit schools.",
      "tribal_welfare_department": "Count or data related to schools managed by the Tribal Welfare Department.",
      "sainik_school": "Count or data related to Sainik Schools.",
      "railway_school": "Count or data related to Railway Schools.",
      "partially_govt_aided": "Count or data related to partially government aided schools."
    }
  },
  "drone_arrests_and_seizures_district_wise_year_wise": {
    "description": "Stores detailed data about drone-based enforcement activities by the Prohibition and Excise department in Bihar, covering arrests, seizures of illegal liquor and vehicles, organized by district and year from 2022 to 2024.",
    "columns": {
      "state_name": "Name of the state where the enforcement activity took place (Bihar).",
      "focus_area": "The department or agency responsible for the enforcement (Prohibition and Excise).",
      "year": "Year in which the enforcement activity occurred.",
      "type_of_raid": "Type or purpose of the raid conducted.",
      "district_name": "Name of the district where the raid was conducted.",
      "total_raids_conducted": "Total number of raids conducted in the specified district and year.",
      "total_cases_registered": "Total number of cases registered as a result of the raids.",
      "total_arrested_people": "Total number of people arrested during the raids.",
      "total_people_taken_for_custody": "Total number of people taken into custody during the raids.",
      "seized_illegal_country_made_liquor_in_litres": "Amount of illegal country-made liquor seized in litres.",
      "seized_illegal_foreign_made_liquor_in_litres": "Amount of illegal foreign-made liquor seized in litres.",
      "seized_illegal_total_liquor_in_litres": "Total amount of illegal liquor seized in litres (sum of country-made and foreign-made).",
      "seized_java_jaggery_solution_and_other_items_in_kgs": "Amount of java jaggery solution and other related items seized in kilograms.",
      "seized_two_wheeler_vehicles": "Number of two-wheeler vehicles seized during the raids.",
      "seized_three_wheeler_vehicles": "Number of three-wheeler vehicles seized during the raids.",
      "seized_four_wheeler_vehicles": "Number of four-wheeler vehicles seized during the raids.",
      "seized_trucks": "Number of trucks seized during the raids.",
      "total_seized_vehicles": "Total number of all types of vehicles seized during the raids."
    }
  },
  "educational_schemes_under_udise_year_wise": {
    "description": "Contains UDISE data for Bihar, covering various educational schemes from 2020-21 to 2023-24, including beneficiary counts, transferred amounts, successful beneficiaries, refunded amounts, and scheme details.",
    "columns": {
      "focus_area": "The department or area of focus for the educational scheme.",
      "state_name": "The name of the state where the scheme is implemented (Bihar).",
      "scheme_name": "The name of the specific educational scheme.",
      "year": "The year for which the data is recorded (e.g., 2020-21, 2023-24).",
      "total_beneficiary_count": "The total number of beneficiaries for the scheme in the given year.",
      "total_transferred_amount_in_rupees": "The total amount of money transferred under the scheme in Rupees.",
      "successful_beneficiary_count": "The number of beneficiaries who successfully received the transferred amount.",
      "successful_transferred_amount_in_rupees": "The total amount successfully transferred to beneficiaries in Rupees.",
      "refunded_beneficiary_count": "The number of beneficiaries whose amounts were refunded.",
      "refunded_amount_in_rupees": "The total amount refunded in Rupees."
    }
  },
  "elabharthi_beneficiaries_scheme_wise": {
    "description": "Stores data on beneficiaries and amounts disbursed under various pension schemes within Bihar's e-Labharthi program.",
    "columns": {
      "pension_scheme": "Name of the pension scheme (e.g., Mukhyamantri Vridhjan Pension Yojna (MVPY), Disabled Pension, Old Age Pensions).",
      "total_beneficiaries": "Total number of beneficiaries enrolled in the specified pension scheme.",
      "total_amount": "Total amount disbursed under the specified pension scheme.",
      "focus_area": "The department or sector under which the data is collected and stored (likely Social Welfare or a related department).",
      "state_name": "Name of the state (Bihar)."
    }
  },
  "elabharthi_pension_beneficiaries_category_wise": {
    "description": "Stores data on pension beneficiaries in Bihar under the e-Labharthi program, categorized by different social categories, along with the total number of beneficiaries and the total amount disbursed.",
    "columns": {
      "category_name": "Name of the beneficiary category (e.g., BC, EBC, General, Minority, SC, ST).",
      "total_beneficiaries": "Total number of beneficiaries belonging to the specified category.",
      "total_amount_in_rupees": "Total amount disbursed to beneficiaries of the specified category in Indian Rupees.",
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or sector focus, likely related to social welfare or pensions."
    }
  },
  "electricity_board_financial_performance_transaction_year_wise": {
    "description": "Stores data on the financial performance of electricity boards, tracking transactions over different years, categorized by focus area, state, transaction type, and specific particulars.",
    "columns": {
      "focus_area": "Broad area of focus within the electricity sector (e.g., Generation, Transmission, Distribution).",
      "state_name": "Name of the state to which the financial data pertains.",
      "transaction_type": "Type of financial transaction recorded (e.g., Revenue, Expenditure, Subsidy).",
      "particulars": "Specific description of the financial item or sub-category within the transaction type (e.g., Fuel Cost, Salary Expenses).",
      "year": "Year for which the financial transaction data is recorded.",
      "rupees_in_crore": "Financial value of the transaction recorded in crore rupees."
    }
  },
  "engineering_college_students_district_branch_year_wise": {
    "description": "Stores data about student admissions in engineering colleges, categorized by district, branch, and year, including regular and lateral entry admissions.",
    "columns": {
      "state_name": "Name of the state where the engineering college is located.",
      "focus_area": "Indicates the focus area or department responsible for the data.",
      "year": "Academic year for which the admission data is recorded.",
      "college_name": "Name of the engineering college.",
      "district_name": "Name of the district where the engineering college is located.",
      "branch_name": "Name of the engineering branch (e.g., Computer Science, Mechanical Engineering).",
      "admissions_via_regular_entry": "Number of students admitted through the regular admission process.",
      "admissions_via_lateral_entry": "Number of students admitted through lateral entry (direct admission to a higher semester)."
    }
  },
  "engineering_polytechnic_faculty_strength_post_wise_branch_wise": {
    "description": "Stores data about faculty strength in engineering and polytechnic institutions in Bihar, categorized by faculty posts, academic branches, and institution types.",
    "columns": {
      "focus_area": "The department or area to which the data pertains.",
      "state_name": "Name of the state (Bihar).",
      "year": "The year for which the faculty strength data is recorded.",
      "education_type": "Type of educational institution (e.g., Engineering, Polytechnic).",
      "post_name": "Designation or position of the faculty member (e.g., Professor, Lecturer).",
      "branch_name": "Academic branch or department of the faculty member (e.g., Computer Science, Civil Engineering).",
      "strength": "Number representing the faculty strength for the given post, branch, and institution type."
    }
  },
  "enrollment_of_students_category_wise_year_wise": {
    "description": "Stores school enrollment data for Bihar from 2022-2024, broken down by social category, gender, and class level, for each school.",
    "columns": {
      "year": "Academic year for the enrollment data (2022-2024).",
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or sector focus.",
      "district_name": "Name of the district.",
      "block_name": "Name of the block.",
      "school_name": "Name of the school.",
      "school_management": "Type of school management (e.g., government, private).",
      "social_category": "Social category of the students (e.g., General, SC, ST, OBC).",
      "pre_primary_three_boys": "Number of boys enrolled in Pre-Primary Three.",
      "pre_primary_three_girls": "Number of girls enrolled in Pre-Primary Three.",
      "pre_primary_two_boys": "Number of boys enrolled in Pre-Primary Two.",
      "pre_primary_two_girls": "Number of girls enrolled in Pre-Primary Two.",
      "pre_primary_one_boys": "Number of boys enrolled in Pre-Primary One.",
      "class_one_boys": "Number of boys enrolled in Class One.",
      "class_one_girls": "Number of girls enrolled in Class One.",
      "class_two_boys": "Number of boys enrolled in Class Two.",
      "class_two_girls": "Number of girls enrolled in Class Two.",
      "class_three_boys": "Number of boys enrolled in Class Three.",
      "class_three_girls": "Number of girls enrolled in Class Three.",
      "class_four_boys": "Number of boys enrolled in Class Four.",
      "class_four_girls": "Number of girls enrolled in Class Four.",
      "class_five_boys": "Number of boys enrolled in Class Five.",
      "class_five_girls": "Number of girls enrolled in Class Five.",
      "class_six_boys": "Number of boys enrolled in Class Six.",
      "class_six_girls": "Number of girls enrolled in Class Six.",
      "class_seven_boys": "Number of boys enrolled in Class Seven.",
      "class_seven_girls": "Number of girls enrolled in Class Seven.",
      "class_eight_boys": "Number of boys enrolled in Class Eight.",
      "class_eight_girls": "Number of girls enrolled in Class Eight.",
      "class_nine_boys": "Number of boys enrolled in Class Nine.",
      "class_nine_girls": "Number of girls enrolled in Class Nine.",
      "class_ten_boys": "Number of boys enrolled in Class Ten.",
      "class_ten_girls": "Number of girls enrolled in Class Ten.",
      "class_eleven_boys": "Number of boys enrolled in Class Eleven.",
      "class_eleven_girls": "Number of girls enrolled in Class Eleven.",
      "class_twelve_boys": "Number of boys enrolled in Class Twelve.",
      "class_twelve_girls": "Number of girls enrolled in Class Twelve."
    }
  },
  "expected_area_of_crop_irrigation_yearwise": {
    "description": "Stores the expected area under irrigation for Kharif and Rabi crops, measured in hectares per cusec, on a yearly basis from 2015-21.",
    "columns": {
      "sector_name": "Name of the sector to which the data belongs.",
      "sector_id": "Unique identifier for the sector.",
      "focus_area": "The specific area of focus for the data collection (e.g., Irrigation Department).",
      "crop_name": "Name of the crop for which irrigation data is recorded.",
      "year": "Year for which the irrigation data is recorded (2015-21).",
      "duty_of_crop": "Expected area of irrigation for a specific crop, measured in hectare per cubic meter.",
      "crop_unit": "Unit of measurement for the crop irrigation duty (Hectare per Cubic meters).",
      "source": "Source of the data, likely the department or organization providing the information (Water Resources Department, Government of Bihar)."
    }
  },
  "faculty_attendees_course_wise_details": {
    "description": "Contains information about faculty members who have conducted courses at the Bihar Institute of Public Administration and Rural Development (BIPARD), providing insights into course details, faculty involvement, and training distribution.",
    "columns": {
      "course_name": "Name of the course conducted.",
      "course_start_date": "Date when the course started.",
      "course_end_date": "Date when the course ended.",
      "subject_name": "Name of the subject taught in the course.",
      "faculty_name": "Name of the faculty member who conducted the course.",
      "state_name": "Name of the state where the training was conducted (likely Bihar).",
      "focus_area": "Department or area of focus for the course.",
      "course_duration_days": "Duration of the course in days."
    }
  },
  "faculty_feedback_course_wise_details": {
    "description": "Stores faculty performance feedback data for courses conducted at the Bihar Institute of Public Administration and Rural Development (BIPARD).",
    "columns": {
      "course_name": "Name of the course for which feedback was collected.",
      "course_start_date": "Starting date of the course.",
      "course_end_date": "Ending date of the course.",
      "group_name": "Name of the group participating in the course.",
      "faculty_name": "Name of the faculty member who taught the course.",
      "subject_name": "Name of the subject taught by the faculty.",
      "session_handled": "Rating or feedback on the faculty's handling of session.",
      "subject_knowledge": "Rating or feedback on the faculty's subject knowledge.",
      "communication": "Rating or feedback on the faculty's communication skills.",
      "methodology": "Rating or feedback on the faculty's teaching methodology.",
      "interaction": "Rating or feedback on the faculty's interaction with students.",
      "question_handling": "Rating or feedback on the faculty's ability to handle questions.",
      "overall_ratings": "Overall rating of the faculty's performance.",
      "course_duration_days": "Duration of the course in days.",
      "focus_area": "Department or sector focus of the data collection.",
      "Feedback_date": "Date when the feedback was submitted.",
      "state_name": "Name of the state where the feedback was collected (Bihar)."
    }
  },
  "farmers_under_vegfed_scheme_block_wise_category_wise": {
    "description": "Stores data about the number of farmers registered under the VEGFED Scheme in Bihar for the year 2024-25, categorized by district, block, and social category (SC, ST, BC, EBC).",
    "columns": {
      "focus_area": "Indicates the specific area or department to which the data relates (likely related to Agriculture or Farmer welfare).",
      "year": "The year for which the data is recorded, specifically 2024-25.",
      "state_name": "The name of the state, which is Bihar in this dataset.",
      "block_name": "The name of the block where the farmers are registered.",
      "district_name": "The name of the district where the farmers are registered.",
      "category_name": "The social category of the registered farmers (e.g., SC, ST, BC, EBC).",
      "number_of_registred_farmers": "The number of farmers registered under the VEGFED scheme for the given block, district, and category."
    }
  },
  "fertilizer_consumption_year_wise": {
    "description": "Stores annual fertilizer consumption data for Bihar, detailing the quantity of various fertilizers used from 2018 to 2023 and fertilizer consumption per hectare.",
    "columns": {
      "year": "Year of fertilizer consumption data (from 2018 to 2023).",
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or sector focus (Agriculture/Fertilizer Consumption).",
      "urea_metric_tons": "Quantity of urea fertilizer consumed in metric tons.",
      "dap_metric_tons": "Quantity of DAP (Diammonium Phosphate) fertilizer consumed in metric tons.",
      "mop_metric_tons": "Quantity of MOP (Muriate of Potash) fertilizer consumed in metric tons.",
      "ssp_metric_tons": "Quantity of SSP (Single Super Phosphate) fertilizer consumed in metric tons.",
      "ammonium_sulphate_metric_tons": "Quantity of ammonium sulphate fertilizer consumed in metric tons.",
      "total_metric_tons": "Total quantity of all fertilizers consumed in metric tons.",
      "fertilizer_consumption_per_hectare_in_kg": "Fertilizer consumption per hectare in kilograms."
    }
  },
  "fisheries_water_bodies_district_wise_year_wise": {
    "description": "Stores information about fisheries water bodies, organized by district and year, including owner and entity names.",
    "columns": {
      "state_name": "Name of the state where the fisheries water body is located.",
      "focus_area": "Department or sector focus (e.g., Fisheries).",
      "year": "Year the data was recorded.",
      "district": "Name of the district where the fisheries water body is located.",
      "name_of_owner": "Name of the owner of the fisheries water body.",
      "name_of_entity": "Name of the entity associated with the fisheries water body."
    }
  },
  "flood_preparedness_scorecard_block_wise_district_wise": {
    "description": "Contains the flood preparedness scorecard data for districts and blocks in Bihar, detailing the availability and condition of resources, infrastructure, and personnel crucial for flood response and mitigation.",
    "columns": {
      "state": "Name of the state (Bihar).",
      "focus_area": "Department or sector focus area (e.g., Disaster Management).",
      "year": "Year for which the flood preparedness data is recorded.",
      "district_name": "Name of the district.",
      "block_name": "Name of the block within the district.",
      "total_panchayats_in_the_block": "Total number of panchayats in the block.",
      "total_flood_prone_panchayats_in_the_block": "Number of panchayats in the block that are prone to flooding.",
      "total_villages_in_the_block": "Total number of villages in the block.",
      "total_flood_prone_villages_in_the_block": "Number of villages in the block that are prone to flooding.",
      "total_no_of_urban_bodies_in_the_block": "Total number of urban local bodies in the block.",
      "total_flood_prone_urban_bodies_in_the_block": "Number of urban local bodies in the block that are prone to flooding.",
      "total_no_of_urban_wards_in_the_block": "Total number of urban wards in the block.",
      "total_flood_prone_urban_wards_in_the_block": "Number of urban wards in the block that are prone to flooding.",
      "number_of_rain_gauge_machines_available_in_the_block": "Number of rain gauge machines available in the block.",
      "number_of_rain_gauge_machines_that_need_repair_in_the_block": "Number of rain gauge machines in the block that require repair.",
      "percentage_of_rain_gauge_machines_that_are_functional": "Percentage of rain gauge machines in the block that are functional.",
      "number_of_boats_required_in_the_block": "Number of boats required in the block for flood response.",
      "number_of_boats_with_private_boat_owners_in_the_block": "Number of boats available with private owners in the block.",
      "number_of_government_boats_available_in_the_block": "Number of government-owned boats available in the block.",
      "number_of_government_boats_to_be_repaired_in_the_block": "Number of government-owned boats in the block that need repair.",
      "number_of_government_and_private_boats_ready_for_the_deployment": "Number of government and private boats ready for deployment.",
      "percentage_of_government_and_private_boats_available": "Percentage of the required number of boats that are actually available.",
      "number_of_boat_owners_in_the_blocks_with_outstanding_payments": "Number of boat owners with outstanding payments.",
      "number_of_generator_sets_available": "Number of generator sets available in the block.",
      "number_of_government_supplied_life_jackets_in_the_block": "Number of government-supplied life jackets available in the block.",
      "number_of_government_supplied_life_jackets_in_in_the_block": "Number of government-supplied life jackets available in the block. (Duplicate column - likely an error).",
      "number_of_government_supplied_mahajals_available_in_the_block": "Number of government-supplied 'mahajals' (large nets) available in the block.",
      "number_of_government_supplied_tents_available_in_the_block": "Number of government-supplied tents available in the block.",
      "number_of_government_supplied_tents_in_the_block": "Number of government-supplied tents available in the block. (Duplicate column - likely an error).",
      "number_of_sites_setting_up_cattle_camps": "Number of sites designated for setting up cattle camps.",
      "identification_of_localized_godowns": "Status of identification of localized godowns (storage facilities).",
      "number_of_teams_constituted_in_the_blocks_for_search_and_rescue": "Number of search and rescue teams constituted in the block.",
      "number_of_trained_divers_gotakhor_available_in_the_block": "Number of trained divers ('gotakhor') available in the block.",
      "number_of_sites_in_the_block_use_as_safe_shelter": "Number of sites in the block that can be used as safe shelters.",
      "safe_shelter_sites_having_lights_potable_water_separate_toilets": "Description of safe shelter sites and availability of basic amenities.",
      "number_of_sites_in_the_block_for_setting_up_mega_camps": "Number of sites identified for setting up mega camps.",
      "number_of_sites_setting_up_community_kitchen": "Number of sites designated for setting up community kitchens.",
      "locations_in_the_block_deployment_of_boats_life_jackets": "Locations in the block designated for deployment of boats and life jackets.",
      "people_trained_in_search_rescue_relief_operations": "Number of people trained in search, rescue, and relief operations.",
      "percentage_of_household_list_verified_by_designated_officers": "Percentage of household lists verified by designated officers.",
      "percentage_of_aadhar_card_seeding_completed_against_household": "Percentage of Aadhaar card seeding completed against households.",
      "number_of_households_as_per_the_updated_list": "Number of households as per the updated list."
    }
  },
  "flood_preparedness_scorecard_district_wise": {
    "description": "Contains district-wise flood preparedness assessment data for Bihar, covering resource availability, condition, and preparedness activities over different years.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or area of focus for the data.",
      "year": "Year of the assessment.",
      "district_name": "Name of the district.",
      "government_supplied_inflatable_lighting_system": "Number of government-supplied inflatable lighting systems available.",
      "government_supplied_inflatable_lighting_system_need_repairing": "Number of government-supplied inflatable lighting systems that need repairing.",
      "government_supplied_inflatable_lighting_system_for_deployment": "Number of government-supplied inflatable lighting systems available for deployment.",
      "government_supplied_gps_sets": "Number of government-supplied GPS sets available.",
      "government_supplied_satellite_phone": "Number of government-supplied satellite phones available.",
      "government_supplied_functional_satellite_phone": "Number of government-supplied functional satellite phones.",
      "places_identified_for_packaging_dry_ration_packets": "Number of places identified for packaging dry ration packets.",
      "total_estimated_polythene_sheets_required": "Total estimated number of polythene sheets required.",
      "total_polythene_sheets_available": "Total number of polythene sheets available.",
      "polythene_sheets_available_in_good_condition_in_the_district": "Number of polythene sheets available in good condition in the district.",
      "percentage_of_polythene_sheets_in_good_condition": "Percentage of polythene sheets available in good condition.",
      "whether_ndrf_sdrf_has_been_deployed_in_the_district": "Indicates whether NDRF/SDRF has been deployed in the district (e.g., Yes/No).",
      "awareness_campaign_mock_drills_conducted_by_ndrf_sdrf": "Number of awareness campaigns/mock drills conducted by NDRF/SDRF.",
      "government_supplied_gps_sets_need_repairing": "Number of government-supplied GPS sets that need repairing.",
      "sites_identified_for_setting_up_cattle_camps_and_arrangement": "Number of sites identified for setting up cattle camps and arrangements.",
      "updated_household_list_verified_by_officers": "Indicates whether the updated household list has been verified by officers (e.g., Yes/No or a count).",
      "percentage_of_aadhar_card_number_seeding_completed": "Percentage of Aadhaar card number seeding completed.",
      "places_identified_for_packaging_of_dry_ration_packets": "Number of places identified for packaging of dry ration packets.",
      "boats_for_which_agreement_with_private_boat_owners_has_been_made": "Number of boats for which agreements with private boat owners have been made.",
      "percentage_of_boats_government_private_available": "Percentage of boats (government and private) available.",
      "satellite_phone_need_repairing": "Number of satellite phones that need repairing."
    }
  },
  "ganja_bhang_seized_arrests_made_district_wise_year_wise": {
    "description": "Contains district-wise and year-wise statistics on prohibition and excise enforcement in Bihar from 2016 to 2024, detailing reported cases, arrests, and the quantity of seized contraband substances.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Indicates the department or area of focus for the data collection (e.g., Prohibition and Excise).",
      "district_name": "Name of the district in Bihar.",
      "year": "Year of the reported data (from 2016 to 2024).",
      "cases_reported": "Number of cases reported related to drug prohibition.",
      "number_of_arrests": "Number of arrests made in connection with the reported cases.",
      "seized_ganja_in_kgs": "Quantity of ganja seized, measured in kilograms.",
      "seized_charas_in_kgs": "Quantity of charas seized, measured in kilograms.",
      "seized_afeem_in_kgs": "Quantity of afeem (opium) seized, measured in kilograms.",
      "seized_heroine_in_kgs": "Quantity of heroine seized, measured in kilograms.",
      "seized_bhaang_in_kgs": "Quantity of bhaang seized, measured in kilograms.",
      "seized_cough_syrup_in_kgs": "Quantity of cough syrup seized, measured in kilograms."
    }
  },
  "gap_in_entry_target_pmay_scheme": {
    "description": "Stores data on the gaps in entering target information for the Pradhan Mantri Awas Yojana (PMAY) scheme, specifically tracking the total number of targets and the number of targets yet to be entered at the district, block, and state levels.",
    "columns": {
      "district_name": "Name of the district.",
      "year": "Year for which the target data is recorded.",
      "block_name": "Name of the block.",
      "total_number_of_targets": "Total number of targets assigned.",
      "number_of_targets_yet_to_be_entered": "Number of targets for which data has not yet been entered.",
      "state_name": "Name of the state.",
      "focus_area": "Department or sector focus."
    }
  },
  "gramin_tola_sampark_nischay_yojana_targets_and_achievements": {
    "description": "Stores target and achievement data for the Gramin Tola Sampark Nischay Yojana, a scheme focused on connecting rural settlements with all-weather roads. Includes project targets, planned road lengths, existing infrastructure, ongoing projects, and completed works.",
    "columns": {
      "state_name": "Name of the state implementing the scheme.",
      "year": "Year for which the targets and achievements are recorded.",
      "district_name": "Name of the district where the scheme is being implemented.",
      "focus_area": "Department or sector focus area for the scheme.",
      "scheme_name": "Name of the scheme (Gramin Tola Sampark Nischay Yojana).",
      "target_number_of_projects_for_connecting_settlement_to_roads": "The planned number of projects aimed at connecting settlements to roads.",
      "target_length_for_connecting_settlement_to_roads_in_kms": "The planned length of roads (in kilometers) to connect settlements.",
      "existing_number_of_projects_connecting_settlement_to_roads": "The existing number of projects already connecting settlements to roads.",
      "length_of_existing_roads_connecting_to_settlements_in_kms": "The length (in kilometers) of existing roads connecting to settlements.",
      "number_of_projects_in_process_to_connect_settlement_to_roads": "Number of ongoing projects aimed at connecting settlements to roads.",
      "length_of_roads_in_process_to_connect_to_settlements_in_kms": "Length (in kilometers) of roads currently under construction to connect to settlements.",
      "target_number_of_projects_for_connecting_settlement_to_roads.1": "This appears to be a duplicate or possibly revised target number of projects for connecting settlements to roads. Needs further investigation to confirm.",
      "target_length_of_roads_for_connecting_to_settlements_in_kms": "This appears to be a duplicate or possibly revised target road length (in kilometers) for connecting settlements to roads. Needs further investigation to confirm.",
      "total_number_of_achieved_projects": "The total number of projects successfully completed under the scheme.",
      "road_length_achieved_in_km": "The total length (in kilometers) of roads constructed under the scheme."
    }
  },
  "growth_in_per_capita_electricity_year_wise": {
    "description": "Tracks the per capita electricity consumption across different states over the years, providing insights into energy usage trends and regional development.",
    "columns": {
      "focus_area": "The department or sector that the data pertains to (e.g., Energy Department).",
      "state": "The name of the state for which the electricity consumption data is recorded.",
      "year": "The year for which the per capita electricity consumption is recorded.",
      "per_capita_consumption_in_unit": "The per capita electricity consumption for the given state and year, measured in units (e.g., kWh)."
    }
  },
  "growth_of_electricity_consumers_year_wise": {
    "description": "Contains data on the growth of electricity consumers in different states over the years, measured in lakhs (hundreds of thousands).",
    "columns": {
      "focus_area": "The department or sector under which the data is categorized (e.g., energy, power).",
      "state": "Name of the state for which the electricity consumer data is recorded.",
      "year": "Year for which the number of electricity consumers is recorded.",
      "number_of_consumer_in_lakhs": "Number of electricity consumers in the specified state and year, measured in lakhs."
    }
  },
  "handpumps_in_bihar_year_wise_district_wise_division_wise": {
    "description": "Stores details of handpumps across districts and divisions in Bihar for the year 2024-25, including information on geotagged, repaired, and different types of handpumps.",
    "columns": {
      "focus_area": "Indicates the department or sector under which the data falls.",
      "state_name": "Name of the state (Bihar).",
      "year": "Year for which the handpump data is recorded (2024-25).",
      "division_name": "Name of the division in Bihar.",
      "district_name": "Name of the district in Bihar.",
      "number_of_geotagged_handpumps": "Number of handpumps that have been geotagged.",
      "number_of_handpumps_repaired": "Number of handpumps that have been repaired.",
      "number_of_other_handpumps_repaired": "Number of other types of handpumps that have been repaired.",
      "number_of_india_mark_handpumps": "Number of India Mark handpumps.",
      "number_of_special_handpumps": "Number of special type handpumps.",
      "number_of_ordinary_handpumps": "Number of ordinary type handpumps."
    }
  },
  "har_ghar_nal_ka_jal_district_wise_block_wise_year_wise": {
    "description": "Stores data on the Har Ghar Nal Ka Jal Yojana in Bihar from 2016 to 2023, detailing annual administrative sanction amounts for water tank installations per ward, organized by panchayat and village.",
    "columns": {
      "focus_area": "Department or sector focus for the data (likely Public Health Engineering Department or similar).",
      "state": "Name of the state (Bihar).",
      "year": "Year of the administrative sanction.",
      "district_name": "Name of the district in Bihar.",
      "block_name": "Name of the block within the district.",
      "panchayat_name": "Name of the panchayat within the block.",
      "village_name": "Name of the village within the panchayat.",
      "administrative_sanction_amount": "Amount of the administrative sanction for water tank installations in the ward, likely in Rupees."
    }
  },
  "hierarchy_division_designation_officers": {
    "description": "Contains information about the officers and their hierarchical structure within various divisions of Bihar's government. It includes details about officer names, designations, and divisions they belong to, potentially used for organizational charts or reporting structures.",
    "columns": {
      "focus_area": "The department or sector the officer belongs to.",
      "year": "The year the data pertains to.",
      "state_name": "The name of the state (Bihar).",
      "division": "The specific division within the state government where the officer is assigned.",
      "designation": "The job title or position of the officer.",
      "officer_name": "The name of the officer."
    }
  },
  "highways_major_district_roads_year_wise_district_wise": {
    "description": "Stores data on road network distribution, specifically the lengths of different types of roads (National Highways, State Highways, and Major District Roads) across various districts in Bihar, on a yearly basis.",
    "columns": {
      "focus_area": "Indicates the department or sector responsible for the data collection (e.g., Highways Department).",
      "state_name": "Name of the state where the road data is recorded (Bihar).",
      "district_name": "Name of the district in Bihar.",
      "year": "The year for which the road length data is recorded (e.g., 2000-01).",
      "type_of_road": "The type of road (e.g., National Highway, State Highway, Major District Road).",
      "road_length_in_kilometers": "Length of the road in kilometers."
    }
  },
  "hostel_grant_scheme_ec_ebc_beneficiary_details_district_wise": {
    "description": "Stores district-wise details of the Hostel Grant Scheme (EC/EBC) in Bihar, including the number of beneficiaries and the total amount approved from the state in rupees for each district and year.",
    "columns": {
      "state_name": "Name of the state (Bihar in this case).",
      "focus_area": "The specific area or department under which the data falls.",
      "year": "Year for which the hostel grant scheme data is recorded.",
      "district_name": "Name of the district in Bihar.",
      "number_of_beneficiary": "Number of beneficiaries under the Hostel Grant Scheme in the district.",
      "total_amount_approved_from_state_in_rupee": "Total amount approved from the state in rupees for the Hostel Grant Scheme in the district."
    }
  },
  "hostel_grant_scheme_ec_ebc_gender_wise_details_block_wise": {
    "description": "Stores data about the Hostel Grant Scheme (BC/EBC) in Bihar, detailing hostel information, student demographics (gender and category), organized by district and block.",
    "columns": {
      "state_name": "Name of the state where the hostel grant scheme is implemented (Bihar).",
      "focus_area": "Indicates the department or area of focus for the data collection (e.g., Social Welfare).",
      "district_name": "Name of the district where the hostel is located.",
      "block_name": "Name of the block where the hostel is located.",
      "hostel_name": "Name of the hostel.",
      "number_of_male_students": "Number of male students residing in the hostel.",
      "number_of_female_students": "Number of female students residing in the hostel.",
      "number_of_students_from_backward_category": "Number of students from Backward Classes (BC) residing in the hostel.",
      "number_of_students_from_extremely_backward_category": "Number of students from Extremely Backward Classes (EBC) residing in the hostel."
    }
  },
  "house_completion_year_wise_pmay_scheme": {
    "description": "Stores data about housing construction under the Pradhan Mantri Awas Yojana (PMAY) scheme, detailing the number of houses completed across different administrative levels (state, district, block, panchayat) and years.",
    "columns": {
      "state_name": "Name of the state where the housing construction is taking place.",
      "district_name": "Name of the district where the housing construction is taking place.",
      "block_name": "Name of the block where the housing construction is taking place.",
      "panchayat_name": "Name of the panchayat where the housing construction is taking place.",
      "scheme_name": "Name of the housing scheme, likely PMAY (Pradhan Mantri Awas Yojana).",
      "focus_area": "Specific area or component within the housing scheme being tracked.",
      "year": "Year in which the houses were completed.",
      "number_of_house_completed": "The number of houses completed in the specified location and year."
    }
  },

  "house_progress_in_pmay_scheme": {
    "description": "Stores data related to the progress of house construction under the Pradhan Mantri Awas Yojana (PMAY) scheme, including sanction details, installment disbursement, and completion status, across different districts, blocks and years.",
    "columns": {
      "district_name": "Name of the district where the houses are being constructed.",
      "scheme_name": "Name of the housing scheme (likely PMAY).",
      "block_name": "Name of the block within the district.",
      "sanctions_out_of_geo_tagged": "Number of sanctions that are outside of geo-tagged locations.",
      "sanctions_with_verified_accounts": "Number of sanctions where the beneficiary accounts are verified.",
      "first_installment": "Number of houses for which the first installment has been released.",
      "second_installment": "Number of houses for which the second installment has been released.",
      "third_installment": "Number of houses for which the third installment has been released.",
      "fourth_installment": "Number of houses for which the fourth installment has been released.",
      "completed_with_verified": "Number of houses completed and verified.",
      "completed": "Total number of houses completed.",
      "year": "Year in which the data was recorded.",
      "state_name": "Name of the state."
    }
  },
  "indira_gandhi_disability_pension_district_wise_year_wise": {
    "description": "Stores district-wise and year-wise data on the Indira Gandhi Disability Pension scheme in Bihar, detailing benefit transfers, amounts disbursed, and beneficiary transaction counts.",
    "columns": {
      "state_name": "Name of the state where the pension scheme is implemented (Bihar).",
      "focus_area": "Department or sector under which the scheme operates (e-labharthi scheme).",
      "year": "Year for which the pension data is recorded.",
      "scheme_name": "Name of the pension scheme (Indira Gandhi Disability Pension).",
      "district_name": "Name of the district where beneficiaries reside.",
      "block_name": "Name of the block where beneficiaries reside.",
      "panchayat_name": "Name of the panchayat where beneficiaries reside.",
      "village_name": "Name of the village where beneficiaries reside.",
      "benefit_transfer_mode": "Method used to transfer pension benefits to beneficiaries.",
      "amount": "Amount of pension disbursed to beneficiaries.",
      "no_of_beneficiaries_transactions": "Number of transactions related to beneficiaries receiving pension."
    }
  },
  "indira_gandhi_national_disability_pension_progress_report": {
    "description": "Provides an overview of the progress of the Indira Gandhi National Disability Pension scheme, including application status and pending cases across districts.",
    "columns": {
      "year": "The year for which the data is reported.",
      "state_name": "The name of the state (Bihar).",
      "focus_area": "The department or area of focus for the data.",
      "scheme_name": "The name of the scheme (Indira Gandhi National Disability Pension).",
      "district_name": "The name of the district.",
      "total_number_of_applications_received": "The total number of applications received for the pension scheme in the district.",
      "pending_applications_with_deo": "The number of applications that are currently pending with the District Education Officer.",
      "pending_applications_for_panchayat_verification": "The number of applications pending verification at the Panchayat level.",
      "pending_applications_for_provisional_verification": "The number of applications pending provisional verification.",
      "new_pending_applications_within_district": "The number of new applications currently pending within the district.",
      "pending_applications_for_error_correction": "The number of applications pending due to errors that need correction.",
      "new_and_error_correction_pending_applications_within_district": "The total number of new applications and those requiring error correction that are pending within the district.",
      "pending_applications_for_approval": "The number of applications that are pending final approval.",
      "approved_applications": "The number of applications that have been approved for the pension scheme.",
      "rejected_applications": "The number of applications that have been rejected for the pension scheme."
    }
  },
  "indira_gandhi_national_old_age_pension_progress_report": {
    "description": "This table tracks the progress of the Indira Gandhi National Old Age Pension scheme, detailing application status from receipt to approval or rejection, including pending stages and error correction.",
    "columns": {
      "year": "The year for which the pension application data is reported.",
      "state_name": "The name of the state to which the data pertains.",
      "focus_area": "The department or sector under which the data has been collected and stored.",
      "scheme_name": "The name of the pension scheme, specifically Indira Gandhi National Old Age Pension.",
      "district_name": "The name of the district to which the application data pertains.",
      "total_number_of_applications_received": "The total number of pension applications received in the given year and district.",
      "pending_applications_with_deo": "Number of applications currently pending verification with the District Education Officer (DEO).",
      "pending_applications_for_panchayat_verification": "Number of applications pending verification at the Panchayat level.",
      "pending_applications_for_provisional_verification": "Number of applications pending provisional verification.",
      "pending_applications_with_assistant_director": "Number of applications pending review with the Assistant Director.",
      "pending_applications_for_error_correction_within_district": "Number of applications within the district that are pending error correction.",
      "new_and_error_correction_pending_applications_within_district": "Total of new applications and those requiring error correction that are pending within the district.",
      "approved_applications": "The number of pension applications that have been approved.",
      "rejected_applications": "The number of pension applications that have been rejected."
    }
  },
  "indira_gandhi_national_widow_pension_progress_report": {
    "description": "Stores data about the progress of the Indira Gandhi National Widow Pension scheme, including application status at various stages, approvals, and rejections.",
    "columns": {
      "year": "The year the data pertains to.",
      "state_name": "The name of the state.",
      "focus_area": "The department or area of focus for the data.",
      "scheme_name": "The name of the scheme, which is Indira Gandhi National Widow Pension.",
      "district_name": "The name of the district.",
      "total_number_of_applications_received": "The total number of applications received for the pension scheme.",
      "pending_applications_with_deo": "The number of applications currently pending with the District Education Officer.",
      "pending_applications_for_panchayat_verification": "The number of applications pending for verification at the Panchayat level.",
      "pending_applications_for_provisional_verification": "The number of applications pending for provisional verification.",
      "pending_applications_with_assistant_director": "The number of applications pending with the Assistant Director.",
      "new_pending_applications_within_district": "The number of newly pending applications within the district.",
      "pending_applications_for_error_correction": "The number of applications that are pending due to errors requiring correction.",
      "new_and_error_correction_pending_applications_within_district": "The number of new applications combined with error correction pending applications within the district.",
      "approved_applications": "The number of applications that have been approved for the pension scheme.",
      "rejected_applications": "The number of applications that have been rejected for the pension scheme."
    }
  },
  "indira_gandhi_widow_pension_district_wise_year_wise": {
    "description": "Stores district-wise and year-wise data related to the Indira Gandhi Widow Pension scheme in Bihar, including beneficiary details, benefit transfer information, and amounts disbursed.",
    "columns": {
      "state_name": "Name of the state where the scheme is implemented (Bihar).",
      "focus_area": "Department or sector under which the scheme operates (e-labharthi).",
      "year": "Year for which the pension data is recorded.",
      "scheme_name": "Name of the pension scheme (Indira Gandhi Widow Pension).",
      "district_name": "Name of the district where the beneficiaries reside.",
      "block_name": "Name of the block where the beneficiaries reside.",
      "panchayat_name": "Name of the panchayat where the beneficiaries reside.",
      "village_name": "Name of the village where the beneficiaries reside.",
      "benefit_transfer_mode": "Method used for transferring pension benefits to beneficiaries.",
      "amount": "Amount of pension disbursed.",
      "no_of_beneficiaries_transactions": "Number of transactions made to beneficiaries."
    }
  },
  "industrial_employment_sector_wise_year_wise": {
    "description": "Stores data regarding industrial employment in Bihar, categorized by sector and year, from 2017-18 to 2024-25.",
    "columns": {
      "focus_area": "The specific area or initiative under which employment data is categorized.",
      "state_name": "Name of the state (Bihar in this case).",
      "sector_name": "The name of the industrial sector for which employment data is recorded.",
      "number_of_person_employed": "The number of people employed in the specified sector.",
      "year": "The year for which the employment data is recorded (e.g., 2017-18)."
    }
  },
  "industrial_investment_sector_wise_year_wise": {
    "description": "Stores data on industrial investments in Bihar, categorized by focus area, sector, and year, detailing the capital invested in each category.",
    "columns": {
      "focus_area": "The specific area of focus or department under which the investment data is categorized.",
      "state_name": "Name of the state where the investment is made (Bihar).",
      "sector_name": "The specific industrial sector receiving investment (e.g., food processing, healthcare).",
      "capital_invested_in_lakh_rupee": "The amount of capital invested in the sector, measured in lakh rupees.",
      "year": "The year in which the investment was made."
    }
  },
  "industries_application_department_wise": {
    "description": "Stores data about the status of license applications required for industrial and business operations in Bihar, categorized by department and including application processing times.",
    "columns": {
      "focus_area": "The department or sector to which the license application pertains.",
      "state_name": "Name of the state where the license is being applied for (Bihar).",
      "department_name": "Name of the specific department responsible for processing the license.",
      "license_name": "Name or type of the license being applied for.",
      "license_id": "Unique identifier for the specific license application.",
      "total_application_received": "Total number of applications received for the license.",
      "approved_application": "Number of applications approved for the license.",
      "rejected_application": "Number of applications rejected for the license.",
      "total_in_progress_application": "Number of applications currently being processed for the license.",
      "pending_department_application": "Number of applications pending with the department.",
      "pending_investor": "Number of applications pending with the investor, presumably for further action or information.",
      "average_time_for_approval": "Average time taken for approval of the license applications.",
      "median_time_for_approval": "Median time taken for approval of the license applications.",
      "minimum_time_for_approval": "Minimum time taken for approval of the license applications.",
      "maximum_time_for_approval": "Maximum time taken for approval of the license applications."
    }
  },
  "irrigation_scheme_block_wise_district_wise_year_wise": {
    "description": "Stores information about irrigation schemes, categorized by block, district, and year, including details on scheme type, funding, tender, and work status.",
    "columns": {
      "focus_area": "The specific area or department responsible for the irrigation scheme.",
      "state_name": "The name of the state where the irrigation scheme is located.",
      "scheme_name": "The name or identifier of the specific irrigation scheme.",
      "district_name": "The name of the district where the irrigation scheme is located.",
      "block_name": "The name of the block within the district where the irrigation scheme is located.",
      "panchayat_name": "The name of the panchayat where the irrigation scheme is located.",
      "type_of_scheme": "The type or category of irrigation scheme (e.g., surface irrigation, groundwater irrigation).",
      "fund_type": "The source or type of funding for the irrigation scheme (e.g., central government, state government).",
      "year": "The year in which the data regarding the irrigation scheme was recorded or implemented.",
      "tender_status": "The current status of the tender process for the irrigation scheme.",
      "work_status": "The current status of the work or construction progress of the irrigation scheme."
    }
  },
  "irrigation_schemes_bihar_2022_culturable_command_area_data": {
    "description": "Contains data on irrigation schemes in Bihar as of 2022, detailing scheme names, benefited districts, and various area measurements related to irrigation potential and utilization.",
    "columns": {
      "name_of_scheme": "Name of the irrigation scheme.",
      "benefited_districts": "List of districts that benefit from the irrigation scheme.",
      "culturable_command_area_in_thousand_hectare_cca": "The total cultivable area that can be irrigated by the scheme, measured in thousands of hectares.",
      "ultimate_irrigation_potential_in_thousand_hectare(uip)": "The maximum irrigation potential that the scheme can achieve, measured in thousands of hectares.",
      "developed_cca_in_thousand_hectare": "The culturable command area that has been developed for irrigation, measured in thousands of hectares.",
      "irrigation_potential_created_in_thousand_hectare(ipc)": "The irrigation potential that has been created by the scheme, measured in thousands of hectares.",
      "irrigation_potential_utilized_in_thousand_hectare(ipu)": "The irrigation potential that is currently being utilized, measured in thousands of hectares.",
      "year": "The year to which the data refers (2022 in this case)."
    }
  },
  "jamabandi_land_record_circle_wise": {
    "description": "Stores Jamabandi land record details from Bihar, including owner information, land area, and tax amounts, organized by district, circle, halka, and mauja.",
    "columns": {
      "focus_area": "Indicates the department or sector under which the data is categorized.",
      "state_name": "Name of the state where the land record is located (Bihar).",
      "district_name": "Name of the district where the land is located.",
      "sub_division_name": "Name of the sub-division where the land is located.",
      "circle_name": "Name of the circle where the land is located.",
      "halka_name": "Name of the halka where the land is located.",
      "mauja_name": "Name of the mauja where the land is located.",
      "owner_name": "Name of the landowner.",
      "area_in_acer_decimal": "Area of the land in acres and decimals.",
      "tax_amount_in_rupees": "Tax amount due for the land in Indian Rupees."
    }
  },
  "jeevika_groups_and_linkage_amount_yearwise": {
    "description": "Stores data related to the progress of the Jeevika initiative, specifically the formation and credit linkage of Self Help Groups (SHGs), Village Organizations (VOs), and Cluster Level Federations (CLFs) from 2017-18 to 2022-23.",
    "columns": {
      "sector_id": "ID of the sector to which the data belongs.",
      "sector_name": "Name of the sector to which the data belongs.",
      "focus_area": "The specific area of focus within the Jeevika initiative.",
      "state": "The state where the Jeevika initiative is being implemented (presumably Bihar).",
      "year": "The year for which the data is recorded (e.g., 2017-18, 2022-23).",
      "cumulative_number_of_self_help_groups_formed_at_year_ending": "Total number of self-help groups formed up to the end of the specified year.",
      "yearwise_self_help_groups_formation": "Number of self-help groups formed in the specified year.",
      "cumulative_number_of_village_organizations_formed": "Total number of village organizations formed cumulatively.",
      "cumulative_cluster_level_fedrations_formed": "Total number of cluster level federations formed cumulatively.",
      "year_wise_cluster_level_fedrations_formation": "Number of cluster level federations formed in the specified year.",
      "cumulative_self_help_groups_saving_accounts_opened": "Total number of SHG saving accounts opened cumulatively.",
      "year_wise_self_help_groups_saving_accounts_opened": "Number of SHG saving accounts opened in the specified year.",
      "total_number_of_house_holds_endorsed": "Total number of households endorsed by the program up to the year.",
      "yearwise_achievement_of_house_holds_endorsed": "Number of households endorsed by the program in the specified year.",
      "cumulative_self_help_groups_credit_linked": "Total number of self-help groups that have been credit-linked cumulatively.",
      "yearwise_self_help_groups_credit_linkages_achievement": "Number of self-help groups that achieved credit linkages in the specified year.",
      "cumulative_credit_linkage_amount_in_crores": "Total credit linkage amount in crores of rupees cumulatively.",
      "yearwise_credit_linkage_amount_in_crores": "Credit linkage amount in crores of rupees achieved in the specified year.",
      "yearwise_village_organization_formation": "Number of village organizations formed in the specified year."
    }
  },
  "khatian_land_registration_details": {
    "description": "Stores the annual number of khatian plot registrations under the Registrations Department in Bihar, covering financial years from 2008-09 to 2023-24.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or sector focus (Registrations Department).",
      "year": "Financial year for which the registration data is recorded (e.g., 2008-09).",
      "number_of_khatian_plot_registrations": "The number of khatian plot registrations during the specified year."
    }
  },
  "labour_resources_learner_details_year_district_gender_wise": {
    "description": "Stores detailed information about learners enrolled in skill development programs under the Labour Resources Department, focusing on the Bihar Skill Development Mission, categorized by year, district, and gender.",
    "columns": {
      "state_name": "Name of the state where the skill development program is implemented (Bihar).",
      "year": "Year of enrollment or data collection (2016-2025).",
      "focus_area": "Specific focus area or department within the Labour Resources Department.",
      "district_name": "Name of the district where the learner is enrolled.",
      "block_name": "Name of the block within the district where the learner is enrolled.",
      "learner_name": "Name of the learner enrolled in the program.",
      "gender": "Gender of the learner.",
      "center_name": "Name of the training center where the learner is enrolled.",
      "center_code": "Unique code or identifier for the training center.",
      "scheme_name": "Name of the skill development scheme under which the learner is enrolled (e.g., Kushal Yuva Program, Self Help Allowance).",
      "course_name": "Name of the course the learner is undertaking.",
      "social_category": "Social category of the learner."
    }
  },
  "land_deed_registration_data": {
    "description": "Stores the annual number of land deed registrations in Bihar under the Registrations Department from 2007 to 2024.",
    "columns": {
      "state_name": "Name of the state where the land deed registrations occurred (Bihar).",
      "focus_area": "Indicates the department responsible for the data (Registrations Department).",
      "land_deed_registration_year": "Year in which the land deed registrations were recorded.",
      "number_of_land_deed_registrations": "The number of land deed registrations for the given year."
    }
  },
  "land_holdings_in_bihar_for_agriculture": {
    "description": "Stores data on different land holding sizes in Bihar used for agriculture, categorized by holding type, for the year 2021, expressed as percentages.",
    "columns": {
      "sector_name": "Name of the sector.",
      "sector_id": "ID of the sector.",
      "focus_area": "Specific area of focus (e.g., Agriculture).",
      "holding_name": "Name of the land holding category (e.g., Marginal, Small, Medium, Large).",
      "year": "Year for which the data is recorded (2021).",
      "holding_value": "Percentage value representing the proportion of land holdings in the specific category.",
      "holding_unit": "Unit of measurement for the holding value (Percentage).",
      "source": "Source of the data (Bihar Through Figures 2021, Directorate of Economics and Statistics Bihar, Patna)."
    }
  },
  "land_utilization_yearwise": {
    "description": "Stores detailed year-wise data on land utilization across various districts, categorizing land into different types such as forest, agriculture, and barren land. The data pertains to the time period of 2022-23.",
    "columns": {
      "district_name": "Name of the district for which land utilization data is recorded.",
      "total_land_area": "Total land area of the district.",
      "forest_land_area": "Area of land classified as forest.",
      "non_agriculture_land_area": "Area of land used for non-agricultural purposes.",
      "non_agriculture_perennial_waterbody_area": "Area of land occupied by perennial (year-round) water bodies used for non-agricultural purposes.",
      "non_agriculture_temporary_waterbody_area": "Area of land occupied by temporary water bodies used for non-agricultural purposes.",
      "barren_unculturable_land_area": "Area of land that is barren and unculturable.",
      "land_area_for_permanent_pastures_and_grazing": "Area of land designated for permanent pastures and grazing.",
      "land_area_for_under_misc_tree_crop_and_groves_not_included": "Area of land under miscellaneous tree crops and groves, not included elsewhere.",
      "culturable_waste_land_area": "Area of land that is cultivable but currently unused (waste land).",
      "other_fallow_land_area": "Area of land that is temporarily uncultivated for a period longer than one year (other fallow land).",
      "current_fallow_land_area": "Area of land that is temporarily uncultivated during the current year (current fallow land).",
      "total_fallow_land_area": "Total area of fallow land, combining current and other fallow lands.",
      "total_non_agricultural_land": "Total area of land used for non-agricultural purposes.",
      "net_sown_area": "Area of land on which crops are sown at least once during the year.",
      "total_cropped_land_area": "Total area of land under crops, including areas sown more than once.",
      "land_area_sown_more_than_once": "Area of land that is sown with crops more than once during the year.",
      "year": "Year for which the land utilization data is recorded (2022-23).",
      "state": "Name of the state.",
      "focus_area": "Indicates the department or sector responsible for collecting the data.",
      "land_utilization_unit": "Unit of measurement for the land areas (e.g., hectares, acres).",
      "sector_name": "Name of the sector to which the data belongs."
    }
  },
  "laxmi_bai_social_security_pension_district_wise_year_wise": {
    "description": "Stores district-wise and year-wise data on the Laxmi Bai Social Security Pension scheme in Bihar, detailing benefit transfer modes, amounts disbursed, and beneficiary transaction counts across different administrative levels.",
    "columns": {
      "state_name": "Name of the state where the scheme is implemented (Bihar).",
      "focus_area": "Department or sector under which the scheme operates (e-labharthi scheme).",
      "year": "Year for which the pension data is recorded.",
      "scheme_name": "Name of the social security pension scheme (Laxmi Bai Social Security Pension).",
      "district_name": "Name of the district where beneficiaries reside.",
      "block_name": "Name of the block where beneficiaries reside.",
      "panchayat_name": "Name of the panchayat where beneficiaries reside.",
      "village_name": "Name of the village where beneficiaries reside.",
      "benefit_transfer_mode": "Method used to transfer pension benefits to beneficiaries.",
      "amount": "Amount of pension disbursed.",
      "no_of_beneficiaries_transactions": "Number of transactions related to beneficiaries."
    }
  },
  "manrega_yearwise_all_over_india_details": {
    "description": "Stores year-wise and district-wise details of MGNREGA implementation across India, including budget, wages, employment, participation of marginalized groups, work progress, and expenditure.",
    "columns": {
      "year": "The year for which the MGNREGA data is recorded.",
      "state_name": "The name of the state.",
      "district_name": "The name of the district.",
      "approved_labour_budget_in_rupee": "The approved labor budget in Rupees for the year.",
      "average_wage_per_day_per_person_in_rupee": "The average wage paid per day per person in Rupees.",
      "average_days_of_employment_provided_per_household": "The average number of employment days provided per household.",
      "differently_abled_person_worked": "Number of differently-abled persons who worked under MGNREGA.",
      "material_and_skilled_wages_in_lakh_rupees": "Expenditure on material and skilled wages in Lakh Rupees.",
      "number_of_completed_works": "The number of works completed under MGNREGA.",
      "number_of_gram_panchayat_with_nil_experience": "The number of Gram Panchayats with nil work experience.",
      "number_of_ongoing_works": "The number of ongoing works under MGNREGA.",
      "persondays_of_central_liability_so_far": "The number of persondays of central liability.",
      "scheduled_caste_persondays": "The number of persondays worked by Scheduled Caste individuals.",
      "scheduled_caste_workers_against_active_workers": "Ratio of Scheduled Caste workers to total active workers.",
      "scheduled_tribe_persondays": "The number of persondays worked by Scheduled Tribe individuals.",
      "scheduled_tribe_workers_against_active_workers": "Ratio of Scheduled Tribe workers to total active workers.",
      "total_administrative_expenditure_in_lakh_rupees": "Total administrative expenditure in Lakh Rupees.",
      "total_expenditure_in_lakhs_rupees": "Total expenditure in Lakh Rupees.",
      "total_households_worked": "The total number of households who worked under MGNREGA.",
      "total_individuals_worked": "The total number of individuals who worked under MGNREGA.",
      "total_number_of_active_job_cards": "The total number of active job cards.",
      "total_number_of_active_workers": "The total number of active workers.",
      "total_households_completed_100_days_wage_employment": "The total number of households who completed 100 days of wage employment.",
      "total_number_of_jobcard_issued": "The total number of job cards issued.",
      "total_number_of_workers": "The total number of workers registered under MGNREGA.",
      "total_number_of_works_takenup": "The total number of works taken up under MGNREGA.",
      "total_wages_in_lakh_rupees": "Total wages paid in Lakh Rupees.",
      "women_persondays": "The number of persondays worked by women.",
      "pecent_of_category_B_workers": "Percentage of category B workers.",
      "percent_expenditure_on_agriculture_allied_works": "Percentage of expenditure on agriculture and allied works.",
      "percent_of_natural_resource_management_expenditure": "Percentage of expenditure on natural resource management."
    }
  },
  "mid_day_meal_distribution_district_wise_year_wise": {
    "description": "Stores year-wise and district-wise data on the Mid-Day Meal program in Bihar from 2020 to 2025, tracking the allotment, release order, and dispatch of food resources to schools and agencies.",
    "columns": {
      "month": "Month for which the mid-day meal distribution data is recorded.",
      "year": "Year for which the mid-day meal distribution data is recorded (2020-2025).",
      "district_name": "Name of the district in Bihar.",
      "total_number_of_schools": "Total number of schools in the district.",
      "total_number_of_agencies": "Total number of agencies involved in the mid-day meal program in the district.",
      "allotment_number_of_schools": "Number of schools included in the allotment stage.",
      "allotment_total_rice_to_schools_kg": "Total quantity of rice allotted to schools in kilograms.",
      "allotment_total_fortified_rice_to_schools_kg": "Total quantity of fortified rice allotted to schools in kilograms.",
      "allotment_total_wheat_to_schools_kg": "Total quantity of wheat allotted to schools in kilograms.",
      "allotment_number_of_agencies": "Number of agencies included in the allotment stage.",
      "allotment_total_rice_to_agencies_kg": "Total quantity of rice allotted to agencies in kilograms.",
      "allotment_total_fortified_rice_to_agencies_kg": "Total quantity of fortified rice allotted to agencies in kilograms.",
      "allotment_total_wheat_to_agencies_kg": "Total quantity of wheat allotted to agencies in kilograms.",
      "release_order_number_of_schools": "Number of schools for which release orders were issued.",
      "release_order_total_rice_to_schools_kg": "Total quantity of rice for which release orders were issued to schools in kilograms.",
      "release_order_total_fortified_rice_to_schools_kg": "Total quantity of fortified rice for which release orders were issued to schools in kilograms.",
      "release_order_total_wheat_to_schools_kg": "Total quantity of wheat for which release orders were issued to schools in kilograms.",
      "release_order_number_of_agencies": "Number of agencies for which release orders were issued.",
      "release_order_total_rice_to_agencies_kg": "Total quantity of rice for which release orders were issued to agencies in kilograms.",
      "release_order_total_fortified_rice_to_agencies_kg": "Total quantity of fortified rice for which release orders were issued to agencies in kilograms.",
      "release_order_total_wheat_to_agencies_kg": "Total quantity of wheat for which release orders were issued to agencies in kilograms.",
      "dispatch_number_of_schools": "Number of schools for which food grains were dispatched.",
      "dispatch_total_rice_to_schools_kg": "Total quantity of rice dispatched to schools in kilograms.",
      "dispatch_total_fortified_rice_to_schools_kg": "Total quantity of fortified rice dispatched to schools in kilograms.",
      "dispatch_total_wheat_to_schools_kg": "Total quantity of wheat dispatched to schools in kilograms.",
      "dispatch_number_of_agencies": "Number of agencies to which food grains were dispatched.",
      "dispatch_total_rice_to_agencies_kg": "Total quantity of rice dispatched to agencies in kilograms.",
      "dispatch_total_fortified_rice_to_agencies_kg": "Total quantity of fortified rice dispatched to agencies in kilograms.",
      "dispatch_total_wheat_to_agencies_kg": "Total quantity of wheat dispatched to agencies in kilograms.",
      "state_name": "Name of the state (Bihar)."
    }
  },
  "milk_particulars_year_wise": {
    "description": "Stores annual statistics related to the dairy sector in Bihar, specifically data from the Bihar State Milk Co-operative Federation Ltd, including details on Dairy Cooperative Societies (DCS), membership, milk procurement, marketing, retailers, and milk booths, from 2020-21 to 2024-25.",
    "columns": {
      "particulars": "The specific metric or detail being tracked (e.g., Number of DCS Organized, Membership, Milk Procurement).",
      "unit": "The unit of measurement for the particulars (e.g., Lakhs, Lakh kgs/litres per day).",
      "year": "The year for which the data is recorded (e.g., 2020-21, 2024-25).",
      "value_of_particulars": "The numerical value associated with the particular metric for the given year.",
      "state_name": "The name of the state (Bihar).",
      "focus_area": "The specific department or organization responsible for collecting the data (Bihar State Milk Co-operative Federation Ltd)."
    }
  },
  "milk_price_and_composition": {
    "description": "Stores data on milk pricing and composition, specifically focusing on cow and buffalo milk under the Bihar State Milk Co-operative Federation Ltd.",
    "columns": {
      "state_name": "Name of the state where the milk pricing and composition data is recorded.",
      "focus_area": "The area or organization responsible for the data collection (e.g., Bihar State Milk Co-operative Federation Ltd.).",
      "type_of_milk": "Type of milk being priced and analyzed (e.g., cow milk, buffalo milk).",
      "milk_price_in_rupees_per_kg": "Price of the milk in Indian Rupees per kilogram.",
      "milk_fat_percentage": "Percentage of fat content in the milk.",
      "milk_snf_percentage": "Percentage of Solids-Not-Fat (SNF) content in the milk."
    }
  },
  "motorboat_based_arrests_seized_liquor_district_wise_year_wise": {
    "description": "Stores data on motorboat-based raids conducted by the Prohibitions and Excise department in Bihar, detailing arrests and liquor seizures by district and year, from 2022 to 2024.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "The department under which the data has been collected (Prohibitions and Excise).",
      "type_of_raid": "Type of raid conducted (motorboat based).",
      "year": "Year in which the raid was conducted (2022 to 2024).",
      "district_name": "Name of the district where the raid was conducted.",
      "number_of_raids": "Number of motorboat-based raids conducted.",
      "total_registered_cases": "Total number of cases registered as a result of the raids.",
      "total_arrests": "Total number of arrests made during the raids.",
      "seized_illegal_country_made_liquor_in_litres": "Amount of seized illegal country-made liquor in litres.",
      "seized_illegal_foreign_made_liquor_in_litres": "Amount of seized illegal foreign-made liquor in litres.",
      "total_seized_illegal_liquor_in_litres": "Total amount of seized illegal liquor in litres.",
      "seized_illegal_java_mahua_in_lakhs_kgs": "Amount of seized illegal Java Mahua liquor in lakhs of kilograms."
    }
  },
  "mukhya_mantri_gram_sampark_yojana_targets_and_achievements": {
    "description": "Stores data related to the Mukhya Mantri Gram Sampark Yojana (MMGSY), focusing on targets and achievements in connecting habitations to road networks, including planned, ongoing, and completed projects, along with road lengths.",
    "columns": {
      "state_name": "Name of the state implementing the MMGSY scheme.",
      "year": "Year for which the targets and achievements are recorded.",
      "district_name": "Name of the district where the road construction projects are taking place.",
      "focus_area": "Department or sector under which the scheme operates.",
      "scheme_name": "Name of the scheme (Mukhya Mantri Gram Sampark Yojana).",
      "target_number_of_projects_for_connecting_settlement_to_roads": "Planned number of projects for connecting settlements to roads.",
      "target_length_for_connecting_settlement_to_roads_in_kms": "Planned road length in kilometers for connecting settlements to roads.",
      "existing_number_of_projects_connecting_settlement_to_roads": "Number of existing projects connecting settlements to roads.",
      "length_of_existing_roads_connecting_to_settlements_in_kms": "Length of existing roads connecting to settlements in kilometers.",
      "number_of_projects_in_process_to_connect_settlement_to_roads": "Number of projects currently in progress to connect settlements to roads.",
      "length_of_roads_in_process_to_connect_to_settlements_in_kms": "Length of roads currently in progress to connect to settlements in kilometers.",
      "target_number_of_projects_for_connecting_settlement_to_roads.1": "Another target number of projects (likely a duplicate column or a different target type, needs clarification).",
      "target_length_of_roads_for_connecting_to_settlements_in_kms": "Target road length in kilometers for connecting settlements to roads.",
      "total_number_of_achieved_projects": "Total number of projects completed.",
      "road_length_achieved_in_km": "Total length of roads constructed/achieved in kilometers."
    }
  },
  "mukhyamantri_kanya_utthaan_intermediate_beneficiaries": {
    "description": "Stores district-wise data on the number of girl beneficiaries and the total amount disbursed under the Mukhyamantri Kanya Utthaan Yojana for intermediate graduates in Bihar.",
    "columns": {
      "sector_name": "Name of the sector to which the scheme belongs.",
      "scheme_name": "Name of the scheme (Mukhyamantri Kanya Utthaan Yojana Intermediate).",
      "year": "Year in which the benefits were disbursed.",
      "district_name": "Name of the district where the beneficiaries reside.",
      "number_of_beneficiaries": "Number of girl beneficiaries who received benefits.",
      "total_amount": "Total amount disbursed to beneficiaries in the district.",
      "focus_area": "Department or sector focus of the scheme."
    }
  },
  "mukhyamantri_kanya_utthaan_snatak_beneficiaries": {
    "description": "Stores block-wise data on the number of female beneficiaries and the total amount disbursed under the Mukhyamantri Kanya Utthaan Yojana Snatak scheme, which promotes higher education for women in Bihar.",
    "columns": {
      "state": "Name of the state where the scheme is implemented (Bihar).",
      "scheme_name": "Name of the specific scheme (Mukhyamantri Kanya Utthaan Yojana Snatak).",
      "gender": "Gender of the beneficiaries (Female).",
      "year": "Year in which the benefits were disbursed.",
      "district_name": "Name of the district where the beneficiaries reside.",
      "block_name": "Name of the block where the beneficiaries reside.",
      "number_of_beneficiaries": "Number of female beneficiaries in the specified block.",
      "total_amount": "Total amount disbursed to the beneficiaries in the specified block.",
      "sector_name": "Sector to which the scheme belongs (Education).",
      "focus_area": "Specific area of focus (Higher education for women)."
    }
  },
  "mukhyamantri_peyjal_nishchay_yojana_year_wise": {
    "description": "Stores year-wise data on the Mukhyamantri Shahri Peyjal Nishchay Yojana, including objectives, achievements, project details, infrastructure, funding, and monitoring related to ensuring pure drinking water supply to urban households in Bihar.",
    "columns": {
      "focus_area": "The department or sector under which the data is collected (e.g., Urban Development and Housing Department).",
      "state_name": "Name of the state (Bihar).",
      "scheme_name": "Name of the scheme (Mukhyamantri Shahri Peyjal Nishchay Yojana).",
      "year": "Year for which the data is recorded.",
      "key_details": "Specific details or aspects of the scheme being tracked (e.g., population coverage projections, overhead water tank construction).",
      "value": "Numerical value or measurement associated with the key detail.",
      "unit": "Unit of measurement for the 'value' (e.g., number of households, amount in Rupees)."
    }
  },
  "mukhyamantri_shahar_gali_nali_pakikaran_yojana_year_wise": {
    "description": "Stores year-wise data related to the Mukhyamantri Shahar Gali-Nali Pakikaran Nischay Yojana, focusing on paved streets and drainage systems in urban Bihar, including population coverage, road paving targets, and budget information.",
    "columns": {
      "focus_area": "The specific area or department to which the data relates (e.g., Urban Development and Housing Department).",
      "state_name": "Name of the state where the scheme is implemented (Bihar).",
      "scheme_name": "Name of the scheme: Mukhyamantri Shahar Gali-Nali Pakikaran Nischay Yojana.",
      "year": "The year to which the data pertains (e.g., 2024-25).",
      "key_details": "Specific details or metrics related to the scheme (e.g., population coverage as per 2011, roads targeted for paving, budget allocations).",
      "value": "The numerical value or descriptive text associated with the key detail.",
      "unit": "The unit of measurement for the value (e.g., percentage, number of roads, Rupees)."
    }
  },
  "multi_storied_housing_schemes_year_wise": {
    "description": "Stores year-wise details of the Multi-Storied Housing Scheme initiated by the Urban Development and Housing Department in Bihar, focusing on providing housing for urban poor families, specifically for the year 2024-25 initially in Patna, and later expanding to other districts.",
    "columns": {
      "focus_area": "The department or sector under which the data has been collected and stored (e.g., Urban Development and Housing Department).",
      "state_name": "Name of the state where the scheme is being implemented (Bihar).",
      "scheme_name": "Name of the housing scheme (Multi-Storied Housing Scheme).",
      "year": "Year for which the scheme details are recorded (e.g., 2024-25).",
      "key_points": "Important details or highlights of the scheme for the given year.",
      "value": "Numerical value associated with the scheme, depending on the context of the row (e.g., number of families targeted, cost).",
      "unit": "Unit of measurement for the 'value' column (e.g., number of families, Rupees)."
    }
  },
  "municipal_corporation_buildings_district_wise_year_wise": {
    "description": "Stores details about urban development and housing projects in Bihar, including information on municipal corporations, district names, contact persons, ownership type, building area specifications, room and facility descriptions, manpower utilization, and project status for the year 2024-25.",
    "columns": {
      "focus_area": "The specific department or sector under which the project/data falls.",
      "state_name": "Name of the state where the project is located (Bihar).",
      "year": "The year the data pertains to (2024-25).",
      "municipal_corporation_name": "Name of the municipal corporation involved in the project.",
      "district_name": "Name of the district where the building is located.",
      "contact_person": "Name of the contact person for the project.",
      "ownership_type": "Type of ownership of the building (e.g., government, private).",
      "building_area_in_sq_ft": "Area of the building in square feet.",
      "rooms_and_facilities_description": "Description of the rooms and facilities available in the building.",
      "manpower_utilization": "Details on how manpower is being utilized in the building/project.",
      "status": "Current status of the project (e.g., tender submitted, completed, pending, or not initiated)."
    }
  },
  "nali_gali_pakkikaran_yojana_district_wise_block_wise_year_wise": {
    "description": "Stores data about the Nali Gali Pakkiraran Yojana in Bihar from 2015 to 2024, detailing drainage construction (nali) per ward, organized by district, block, and panchayat, along with administrative sanction amounts.",
    "columns": {
      "focus_area": "The department responsible for the data collection related to the scheme.",
      "state": "The state where the scheme is implemented (Bihar).",
      "year": "The year the data pertains to, ranging from 2015 to 2024.",
      "district_name": "Name of the district where the drainage construction took place.",
      "block_name": "Name of the block within the district where the drainage construction took place.",
      "panchayat_name": "Name of the panchayat within the block where the drainage construction took place.",
      "administrative_sanction_amount": "The amount of administrative sanction for the drainage construction project."
    }
  },
  "nali_gali_report_district_wise_year_wise": {
    "description": "Stores district-wise and year-wise data related to the implementation and progress of the Nali-Gali scheme, focused on developing paved drains and streets in urban areas of Bihar.",
    "columns": {
      "focus_area": "The department or sector under which the data is collected (e.g., Urban Development).",
      "state_name": "Name of the state where the scheme is being implemented (Bihar).",
      "urban_local_body_name": "Name of the urban local body (ULB) where the work is being carried out.",
      "district_name": "Name of the district where the ULB is located.",
      "total_urban_wards": "Total number of urban wards in the specific ULB.",
      "wards_covered_by_central_govt_or_other_institutes": "Number of wards covered by central government or other institutions outside of this specific scheme.",
      "targeted_wards": "Number of wards targeted for development under the Nali-Gali scheme.",
      "total_households": "Total number of households in the ULB.",
      "year": "Year in which the data was recorded or the scheme was implemented.",
      "targeted_households_under_scheme_2019_20": "Number of households targeted under the scheme during the year 2019-20.",
      "wards_with_tenders_issued": "Number of wards where tenders have been issued for the work.",
      "wards_where_work_started": "Number of wards where construction work has commenced.",
      "wards_fully_covered_with_paved_drains_and_streets": "Number of wards that are completely covered with paved drains and streets.",
      "total_plans_for_paved_drains_and_streets": "Total number of plans formulated for paved drains and streets.",
      "plans_where_work_started": "Number of plans where construction work has started.",
      "completed_plans": "Number of plans that have been fully completed.",
      "plans_in_progress": "Number of plans that are currently under construction.",
      "plans_in_tendering_process": "Number of plans that are currently in the tendering process.",
      "households_covered_with_completed_paved_drains_and_streets": "Number of households that are currently covered with completed paved drains and streets."
    }
  },
  "national_highways_number_wise": {
    "description": "Stores information on the length of various national highways in Bihar for the year 2024-25.",
    "columns": {
      "focus_area": "The department or area of focus for the data collection (e.g., Roads and Transportation).",
      "state_name": "The name of the state where the national highway is located (Bihar).",
      "year": "The year for which the national highway data is recorded (2024-25).",
      "national_highway_number": "The unique number assigned to the national highway.",
      "length_in_kilometer": "The length of the national highway segment, measured in kilometers."
    }
  },
  "number_of_medhavriti_yojna_beneficiaries": {
    "description": "Stores district-wise data on the number of beneficiaries from Scheduled Caste (SC) and Scheduled Tribe (ST) communities who received scholarships under the Medhavriti Yojna scheme in Bihar.",
    "columns": {
      "sector_name": "Name of the sector to which the scheme belongs (e.g., education).",
      "focus_area": "Specifies the department under which the data is collected and stored (e.g., Education Department).",
      "scheme_name": "Name of the scholarship scheme (Medhavriti Yojna).",
      "district_name": "Name of the district in Bihar where the beneficiaries reside.",
      "number_of_scheduled_caste_beneficiaries": "The number of beneficiaries belonging to the Scheduled Caste (SC) category.",
      "number_of_scheduled_tribe_beneficiaries": "The number of beneficiaries belonging to the Scheduled Tribe (ST) category."
    }
  },
  "number_of_ration_cards_and_members_district_wise": {
    "description": "Stores data on the number of ration cards and associated members in each district of Bihar for the year 2024-25, broken down by rural and urban areas, and card types (Priority Household and Antyodaya Anna Yojana).",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or sector focus (e.g., Food and Civil Supplies).",
      "year": "Year for which the ration card data is recorded (2024-25).",
      "district_name": "Name of the district in Bihar.",
      "number_of_rural_ration_card": "Number of ration cards issued in rural areas of the district.",
      "number_of_urban_ration_card": "Number of ration cards issued in urban areas of the district.",
      "priority_household_cards": "Number of Priority Household (PHH) ration cards in the district.",
      "priority_household_members": "Number of members covered under Priority Household (PHH) ration cards in the district.",
      "antyodaya_anna_yojana_cards": "Number of Antyodaya Anna Yojana (AAY) ration cards in the district.",
      "antyodaya_anna_yojana_members": "Number of members covered under Antyodaya Anna Yojana (AAY) ration cards in the district.",
      "total_cards": "Total number of ration cards in the district (sum of all types).",
      "total_members": "Total number of members covered by all ration cards in the district."
    }
  },
  "number_of_services_year_wise_district_wise_block_wise": {
    "description": "Stores data on the number of services provided through the \"Service Plus\" platform in different blocks of various districts of Bihar, covering the period from 2019 to 2025.",
    "columns": {
      "year": "Year in which the services were provided.",
      "district_name": "Name of the district where the services were provided.",
      "block_name": "Name of the block within the district where the services were provided.",
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or sector focus area under which these services fall.",
      "number_of_services_provided": "The count of services provided in the specified block during the given year."
    }
  },
  "patna_smartcity_agencywise_summary_report": {
    "description": "Summarizes the progress and financial status of Patna Smart City projects for the year 2024-25, categorized by the executing agency.",
    "columns": {
      "state_name": "Name of the state where the projects are located (presumably Bihar).",
      "district_name": "Name of the district where the projects are located (Patna).",
      "year": "The year in which the project data was recorded (2024-25).",
      "focus_area": "The area or sector the project belongs to (e.g., infrastructure, civic amenities).",
      "agency_name": "Name of the agency responsible for executing the projects.",
      "number_of_projects": "Total number of projects being handled by the agency.",
      "completed": "Number of projects completed by the agency.",
      "ongoing": "Number of projects currently in progress by the agency.",
      "total_cost_in_crore": "Total cost of all projects handled by the agency, measured in crore rupees."
    }
  },
  "payment_to_mothers_under_mkuy_scheme": {
    "description": "Stores data related to payments made to mothers under the Mukhyamantri Kanya Utthan Yojana (MKUY) scheme.",
    "columns": {
      "state_name": "Name of the state where the payment was made.",
      "focus_area": "Indicates the specific department or area of focus related to the scheme.",
      "scheme_name": "Name of the scheme under which the payment was made (Mukhyamantri Kanya Utthan Yojana).",
      "total_amount": "The total amount of the payment made (likely in Rupees).",
      "year": "The year in which the payment was made.",
      "district_name": "The district in which the payment was made.",
      "category_name": "Category to which the beneficiary belongs."
    }
  },
  "polytechnic_college_students_district_branch_year_wise": {
    "description": "Stores details of admissions in Government Polytechnic institutes in Bihar from 2022-23 to 2024-25, categorized by district, branch, and year.",
    "columns": {
      "state_name": "Name of the state where the polytechnic college is located (Bihar).",
      "focus_area": "Department or sector under which the data falls.",
      "year": "Academic year for which the admission data is recorded (e.g., 2022-23).",
      "institute_name": "Name of the Government Polytechnic institute.",
      "district_name": "Name of the district where the polytechnic institute is located.",
      "branch_name": "Name of the engineering branch (e.g., Civil Engineering, Computer Science).",
      "admissions_via_regular_entry": "Number of admissions through the regular entry mode.",
      "admissions_via_lateral_entry": "Number of admissions through the lateral entry mode."
    }
  },
  "population_of_cattle_breed_gender_wise_in_bihar_yearly_trend": {
    "description": "Stores the population data of Exotic/Crossbred Cows, Indigenous Cows, and Buffaloes in Bihar, categorized by breed, gender, and age groups, from 2003 to 2019.",
    "columns": {
      "sector_name": "Name of the sector to which the data belongs.",
      "sector_id": "Unique identifier for the sector.",
      "focus_area": "Specific area of focus within the animal husbandry sector.",
      "cattle_type": "Type of cattle (e.g., Exotic/Crossbred Cows, Indigenous Cows, Buffaloes).",
      "year": "Year of the population data collection (2003-2019).",
      "male_count": "Number of male cattle.",
      "female_count": "Number of female cattle.",
      "under_1_year_count": "Number of cattle under 1 year of age.",
      "1_to_3_year_count": "Number of cattle between 1 and 3 years of age.",
      "in_milk_animal_count": "Number of animals currently producing milk.",
      "dry_count": "Number of animals that are not currently producing milk (dry).",
      "milch_animal_count": "Number of animals used for milk production.",
      "not_even_calved_once_count": "Number of female animals that have not yet given birth.",
      "others_count": "Number of cattle that do not fall into other specified categories.",
      "total_count": "Total number of cattle in the specified category.",
      "cattle_unit": "Unit of measurement for the cattle population (Number).",
      "source": "Source of the data (Directorate of Animal Husbandry, Animal & Fisheries, Resources Department, Govt. of Bihar).",
      "state_name": "Name of the state (Bihar)."
    }
  },
  "post_matric_scheme_student_benefecries_district_wise": {
    "description": "Stores district-wise data on beneficiaries of the Post Matric Scholarship scheme, including student demographics, scholarship amounts, and category breakdowns.",
    "columns": {
      "district_name": "Name of the district.",
      "block_name": "Name of the block within the district.",
      "year": "Year for which the data is recorded.",
      "number_of_student_stays_in_hostle": "Number of students residing in hostels.",
      "number_of_student_orphan": "Number of orphan students.",
      "number_of_disable_student": "Number of students with disabilities.",
      "total_scholarship_amount": "Total amount of scholarship disbursed.",
      "number_of_male_student": "Number of male students.",
      "number_of_female_student": "Number of female students.",
      "hindu_count": "Number of Hindu students.",
      "muslim_count": "Number of Muslim students.",
      "na_count": "Number of students for whom religion data is not available.",
      "buddhist_count": "Number of Buddhist students.",
      "sikh_count": "Number of Sikh students.",
      "others_count": "Number of students belonging to other religions.",
      "christian_count": "Number of Christian students.",
      "parsi_count": "Number of Parsi students.",
      "jain_count": "Number of Jain students.",
      "number_of_economically_backward_classes": "Number of students from Economically Backward Classes.",
      "number_of_general": "Number of students belonging to the General category.",
      "number_of_scheduled_caste": "Number of students belonging to the Scheduled Caste category.",
      "number_of_backward_class": "Number of students belonging to the Backward Class category.",
      "number_of_scheduled_tribe": "Number of students belonging to the Scheduled Tribe category.",
      "state_name": "Name of the state."
    }
  },
  "poultry_farming_animal_husbandry_year_wise_district_wise": {
    "description": "Stores data on poultry farming and animal husbandry in Bihar for the year 2024-25, specifically focusing on layer poultry capacity with and without feed mill facilities across districts.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or sector focus (Poultry Farming/Animal Husbandry).",
      "year": "Year of data collection (2024-25).",
      "district_name": "Name of the district in Bihar.",
      "layer_poultry_capacity": "Capacity of layer poultry farms (e.g., 5,000 or 10,000 layers).",
      "with_feed_mill": "Indicates the number of poultry farms with a feed mill.",
      "without_feed_mill": "Indicates the number of poultry farms without a feed mill."
    }
  },
  "pradhan_mantri_gram_sadak_yojana_i_targets_and_achievements": {
    "description": "Stores data related to targets and achievements under the Pradhan Mantri Gram Sadak Yojana (PMGSY-I), focusing on road projects aimed at connecting rural settlements, including approved targets, ongoing work, and achieved road lengths.",
    "columns": {
      "state_name": "Name of the state where the PMGSY-I scheme is being implemented.",
      "year": "Year for which the PMGSY-I data is recorded.",
      "focus_area": "Department or sector under which the PMGSY-I scheme operates.",
      "district_name": "Name of the district where road construction is taking place under PMGSY-I.",
      "scheme_name": "Name of the scheme, which is PMGSY-I.",
      "number_of_approved_target_of_connecting_road_and_settlements": "Number of approved targets for connecting roads and settlements.",
      "total_approved_targets_and_total_road_length_in_km": "Total approved targets and total road length in kilometers.",
      "total_number_of_settlements_with_ongoing_road_construction": "Total number of settlements where road construction is currently ongoing.",
      "total_number_of_settlements_and_length_of_road_in_kms": "Total number of settlements and the length of road in kilometers associated with them.",
      "no_of_settlements_of_connecting_roads": "Number of settlements connected by roads.",
      "ongoing_connection_road_length_in_km": "Length of roads currently under construction to connect settlements, measured in kilometers.",
      "physical_targets_and_total_number_of_settlements": "Physical targets set and total number of settlements to be connected.",
      "length_of_road": "Total length of road constructed or targeted, likely in kilometers.",
      "total_number_of_achieved_projects": "Total number of road construction projects successfully completed under PMGSY-I.",
      "road_length_achieved": "Length of road construction successfully completed, likely in kilometers."
    }
  },
  "pradhan_mantri_gram_sadak_yojana_ii_targets_and_achievements": {
    "description": "Stores data related to targets and achievements of road projects under the Pradhan Mantri Gram Sadak Yojana (PMGSY-II), tracking progress of previously approved projects, ongoing work, and completed road lengths.",
    "columns": {
      "state_name": "Name of the state where the PMGSY-II scheme is being implemented.",
      "year": "Year for which the data on targets and achievements is recorded.",
      "district_name": "Name of the district where road projects are being implemented.",
      "scheme_name": "Name of the scheme, which is Pradhan Mantri Gram Sadak Yojana II (PMGSY-II).",
      "total_approved_targets_and_total_projects": "Total number of projects approved under PMGSY-II.",
      "total_approved_targets_and_total_road_length_in_km": "Total approved road length in kilometers under PMGSY-II.",
      "total_number_of_previously_constructed_projects": "Number of road projects that were previously constructed.",
      "previously_completed_road_length_in_km": "Length of roads (in kilometers) that were previously completed.",
      "total_ongoing_road_connection_projects": "Number of road connection projects that are currently ongoing.",
      "ongoing_connection_road_length_in_km": "Length of ongoing road connection projects in kilometers.",
      "total_number_of_projects": "Total number of projects (likely including both ongoing and completed).",
      "achievement_of_road_length_in_km": "Total road length achieved in kilometers.",
      "total_number_of_achieved_projects": "Total number of road projects that have been completed.",
      "road_length_achieved_in_km": "The length of the road achieved (in Km)."
    }
  },
  "pradhan_mantri_gram_sadak_yojana_iii_targets_and_achievements": {
    "description": "Stores data regarding the targets and achievements of road construction projects under the Pradhan Mantri Gram Sadak Yojana (PMGSY-III) scheme, tracking planned projects, ongoing works, and completed road construction.",
    "columns": {
      "state_name": "Name of the state where the road construction project is being carried out.",
      "year": "Year in which the targets and achievements are recorded.",
      "district_name": "Name of the district where the road construction project is located.",
      "focus_area": "Department or sector under which the data has been collected and stored.",
      "scheme_name": "Name of the scheme under which the project is being executed (PMGSY-III).",
      "target_number_of_projects_for_connecting_settlement_to_roads": "Planned/Targeted number of road construction projects for connecting settlements.",
      "target_length_for_connecting_settlement_to_roads_in_kms": "Targeted road length in kilometers for connecting settlements.",
      "existing_number_of_projects_connecting_settlement_to_roads": "Number of road construction projects already existing that connect settlements.",
      "length_of_existing_roads_connecting_to_settlements_in_kms": "Length of existing roads in kilometers that connect to settlements.",
      "number_of_projects_in_process_to_connect_settlement_to_roads": "Number of road construction projects currently underway to connect settlements.",
      "length_of_roads_in_process_to_connect_to_settlements_in_kms": "Length of roads in kilometers currently under construction to connect settlements.",
      "target_number_of_projects_for_connecting_settlement_to_roads.1": "Duplicate column for the targeted number of road construction projects for connecting settlements. (Likely an error in the original schema).",
      "target_length_of_roads_for_connecting_to_settlements_in_kms": "Targetted road length in kilometers for connecting settlements.",
      "total_number_of_achieved_projects": "Total number of road construction projects that have been successfully completed.",
      "road_length_achieved_in_km": "Total length of roads in kilometers that have been constructed and completed."
    }
  },
  "production_import_npk_fertilizer_year_wise": {
    "description": "Stores annual data on the production and import of NPK fertilizers, focusing on optimizing fertilizer usage for soil health management from 1981-82 to 2021-22.",
    "columns": {
      "id": "Unique identifier for each record.",
      "focus_area": "Indicates the department or sector under which the data falls, related to fertilizer usage and soil health.",
      "indicator_name": "Specifies the type of indicator being measured, such as \"Production\" or \"Import\".",
      "indicator_item": "Describes the specific fertilizer type or component being tracked (NPK).",
      "year": "The year for which the data is recorded (e.g., 1981-82, 2021-22).",
      "indicator_value": "The value of the indicator (production or import) for the given year.",
      "indicator_value_unit": "Unit of measurement for the indicator value (e.g., lakh tonnes)."
    }
  },
  "public_health_housing_details_district_wise_year_wise": {
    "description": "Stores district-wise and year-wise data related to housing and public health schemes under the Urban Development and Housing Department in Bihar, including details on Panchayati Raj and Public Health Engineering Department schemes.",
    "columns": {
      "focus_area": "Indicates the department or sector to which the data pertains.",
      "state_name": "Name of the state (Bihar in this case).",
      "year": "Year for which the data is recorded (2024-25).",
      "district_name": "Name of the district in Bihar.",
      "name_of_municipal_body": "Name of the municipal body in the district.",
      "rural_wards_making_municipal_body": "Number of rural wards combined to form the municipal body.",
      "urban_wards_post_formation_of_municipal_body": "Number of urban wards after the formation of the municipal body.",
      "total_number_of_houses": "Total number of houses in the area.",
      "panchayati_raj_department_operated_total_schemes": "Total number of schemes operated by the Panchayati Raj Department.",
      "panchayati_raj_department_operated_functional_schemes": "Number of functional schemes operated by the Panchayati Raj Department.",
      "panchayati_raj_department_operated_non_functional_schemes": "Number of non-functional schemes operated by the Panchayati Raj Department.",
      "houses_covered_under_panchayati_raj_department": "Number of houses covered under schemes of the Panchayati Raj Department.",
      "public_health_engineering_department_operated_total_schemes": "Total number of schemes operated by the Public Health Engineering Department.",
      "public_health_engineering_department_operated_functional_schemes": "Number of functional schemes operated by the Public Health Engineering Department.",
      "department_operated_non_functional_schemes": "Number of non-functional schemes operated by the Public Health Engineering Department.",
      "houses_covered_under_public_health_engineering_department": "Number of houses covered under schemes of the Public Health Engineering Department."
    }
  },
  "quality_of_roads_year_wise_road_type_wise": {
    "description": "Stores data about the quality and condition of roads in Bihar for the year 2024-25, including road length, type, and condition.",
    "columns": {
      "focus_area": "Indicates the department or sector responsible for the data collection.",
      "state_name": "Name of the state where the roads are located (Bihar).",
      "year": "Year for which the road quality data is recorded (2024-25).",
      "road_name": "Name or identifier of the road.",
      "road_type": "Classification of the road (e.g., highway, rural road).",
      "total_road_length_in_kilometer": "Total length of the road segment in kilometers.",
      "wing_name": "Name of the wing or division responsible for the road.",
      "circle_name": "Name of the circle or regional office responsible for the road.",
      "division_name": "Name of the division or local office responsible for the road.",
      "length_of_roads_in_good_condition_in_kilometer": "Length of the road segment in good condition, measured in kilometers.",
      "length_of_roads_in_fair_condition_in_kilometer": "Length of the road segment in fair condition, measured in kilometers.",
      "length_of_roads_in_average_condition_in_kilometer": "Length of the road segment in average condition, measured in kilometers.",
      "length_of_roads_in_bad_condition_in_kilometer": "Length of the road segment in bad condition, measured in kilometers.",
      "length_of_single_lane_roads_in_kilometer": "Length of the road segment with a single lane, measured in kilometers.",
      "length_of_intermediate_lane_roads_in_kilometer": "Length of the road segment with an intermediate lane, measured in kilometers.",
      "length_of_two_lane_roads_in_kilometer": "Length of the road segment with two lanes, measured in kilometers.",
      "length_of_roads_with_more_than_seven_feet_width_in_kilometer": "Length of the road segment with a width greater than seven feet, measured in kilometers.",
      "updated_new_total_road_length_in_kilometer": "Updated or revised total length of the road segment in kilometers."
    }
  },
  "raids_fir_arrests_district_wise": {
    "description": "Stores district-level data on mining enforcement activities in Bihar for the year 2024-25, including the number of raids, FIRs, arrests, and revenue collected.",
    "columns": {
      "state_name": "Name of the state where the enforcement activities occurred (Bihar).",
      "focus_area": "Indicates the department or sector responsible for the enforcement activities (Mining Department).",
      "district_name": "Name of the district where the raids, FIRs, and arrests took place.",
      "number_of_raids": "The number of raids conducted in the district.",
      "number_of_FIR": "The number of First Information Reports (FIRs) filed in the district.",
      "number_of_arrests": "The number of arrests made in connection to mining violations in the district.",
      "total_amount_collected_in_lakh_rupees": "The total amount of revenue collected from mining enforcement activities in the district, measured in lakh rupees.",
      "year": "The year for which the data is recorded (2024-25)."
    }
  },
  "raids_fir_arrests_year_wise": {
    "description": "Stores statewide mining enforcement statistics in Bihar from 2021-22 to 2023-24, including the number of raids, FIRs, arrests, and revenue collected.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "The department or area of focus (Mining Enforcement).",
      "year": "The year for which the data is recorded (e.g., 2021-22, 2022-23, 2023-24).",
      "number_of_raids": "The total number of raids conducted.",
      "number_of_FIR": "The total number of First Information Reports (FIRs) filed.",
      "number_of_arrests": "The total number of arrests made.",
      "revenue_collected_in_crores_rupees": "The total revenue collected in crores of Indian Rupees (₹)."
    }
  },
  "rainfall_in_bihar_yearwise_districtwise_month_wise": {
    "description": "Stores monthly rainfall data for districts in Bihar, including normal and actual rainfall in millimeters, along with percentage deviations, from 2007-08 to 2024-25.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or sector focus (e.g., Agriculture, Climate).",
      "year": "Year for which the rainfall data is recorded (e.g., 2007-08).",
      "name_of_districts": "Name of the district in Bihar.",
      "june_normal_rainfall_in_millimeter": "Normal rainfall in June, measured in millimeters.",
      "june_actual_rainfall_in_millimeter": "Actual rainfall in June, measured in millimeters.",
      "june_deviation_in_percentage": "Percentage deviation of actual rainfall from normal rainfall in June.",
      "july_normal_rainfall_in_millimeter": "Normal rainfall in July, measured in millimeters.",
      "july_actual_rainfall_in_millimeter": "Actual rainfall in July, measured in millimeters.",
      "july_deviation_in_percentage": "Percentage deviation of actual rainfall from normal rainfall in July.",
      "august_normal_rainfall_in_millimeter": "Normal rainfall in August, measured in millimeters.",
      "august_actual_rainfall_in_millimeter": "Actual rainfall in August, measured in millimeters.",
      "august_deviation_in_percentage": "Percentage deviation of actual rainfall from normal rainfall in August.",
      "september_normal_rainfall_in_millimeter": "Normal rainfall in September, measured in millimeters.",
      "september_actual_rainfall_in_millimeter": "Actual rainfall in September, measured in millimeters.",
      "september_deviation_in_percentage": "Percentage deviation of actual rainfall from normal rainfall in September.",
      "june_to_september_normal_rainfall_in_millimeter": "Normal rainfall from June to September, measured in millimeters.",
      "june_to_september_actual_rainfall_in_millimeter": "Actual rainfall from June to September, measured in millimeters.",
      "june_to_september_deviation__in_percentage": "Percentage deviation of actual rainfall from normal rainfall from June to September.",
      "october_normal_rainfall_in_millimeter": "Normal rainfall in October, measured in millimeters.",
      "october_actual_rainfall_in_millimeter": "Actual rainfall in October, measured in millimeters.",
      "october_deviation_in_percentage": "Percentage deviation of actual rainfall from normal rainfall in October.",
      "november_normal_rainfall_in_millimeter": "Normal rainfall in November, measured in millimeters.",
      "november_actual_rainfall_in_millimeter": "Actual rainfall in November, measured in millimeters.",
      "november_deviation_in_percentage": "Percentage deviation of actual rainfall from normal rainfall in November.",
      "december_normal_rainfall_in_millimeter": "Normal rainfall in December, measured in millimeters.",
      "december_actual_rainfall_in_millimeter": "Actual rainfall in December, measured in millimeters.",
      "december_deviation_in_percentage": "Percentage deviation of actual rainfall from normal rainfall in December.",
      "october_to_december_normal_rainfall_in_millimeter": "Normal rainfall from October to December, measured in millimeters.",
      "october_to_december_actual_rainfall_in_millimeter": "Actual rainfall from October to December, measured in millimeters.",
      "october_to_december_deviation_in_percentage": "Percentage deviation of actual rainfall from normal rainfall from October to December."
    }
  },
  "registrar_office_details": {
    "description": "Stores the count of different types of registration offices under the Registrations Department in Bihar.",
    "columns": {
      "state_name": "Name of the state where the registration offices are located (Bihar).",
      "focus_area": "Indicates the department responsible for these offices (Registrations Department).",
      "office_type": "Type of registration office (e.g., District Registrar, Sub-Registrar).",
      "count_of_office_type": "Number of offices of the specified office type."
    }
  },
  "revenue_year_wise": {
    "description": "Stores year-wise revenue collection data for Bihar's Mining and Geology Department from various sources, specifically for the years 2022-23 and 2023-24.",
    "columns": {
      "state_name": "Name of the state for which the revenue data is recorded (Bihar).",
      "focus_area": "The department under which the data has been collected (Mining and Geology Department).",
      "revenue_in_crores_rupees": "Revenue amount in crores of Indian Rupees.",
      "year": "The financial year for which the revenue was collected (e.g., 2022-23, 2023-24).",
      "source_of_collection": "Source from which the revenue was collected (e.g., Sand mining, Penalties, Departmental collections).",
      "type_of_collection": "Type of collection (e.g., minor minerals, major minerals)."
    }
  },
  "road_category_with_their_lengths_year_wise": {
    "description": "Stores information about the lengths of different road categories in Bihar for each year from 2015-16 to 2024-25.",
    "columns": {
      "focus_area": "Indicates the department or sector responsible for the data collection.",
      "state_name": "Name of the state (Bihar).",
      "categor_of_road": "Category of the road (e.g., Single Lane, Double Lane).",
      "year": "Year for which the road length data is recorded (e.g., 2015-16).",
      "length_in_kilometer": "Length of the road segment in kilometers."
    }
  },
  "road_construction_overview_year_wise_road_category_type_wise": {
    "description": "Provides an overview of road construction in Bihar for the year 2024-25, categorized by road types (Single Lane, Intermediate Lane, Double Lane, etc.) and highlighting the length and percentage share of National Highways, State Highways, and Major District Roads. Includes information on missing links and greenfield projects.",
    "columns": {
      "focus_area": "The department or sector under which the road construction data is categorized.",
      "state_name": "Name of the state for which the road construction data is recorded (Bihar in this case).",
      "year": "The year for which the road construction data is recorded (2024-25).",
      "category_of_road": "Type or category of road (e.g., Single Lane, Intermediate Lane, Double Lane, Missing Links, Greenfield Projects).",
      "national_highways_length_in_kilometer": "Length of National Highways for the specified road category, measured in kilometers.",
      "national_ highways_percentage_share": "Percentage share of National Highways length relative to the total length for the specified road category.",
      "state_highways_length_in_kilometer": "Length of State Highways for the specified road category, measured in kilometers.",
      "state_highways_percentage_share": "Percentage share of State Highways length relative to the total length for the specified road category.",
      "major_district_roads_length_in_kilometer": "Length of Major District Roads for the specified road category, measured in kilometers.",
      "major_district_roads_percentage_share": "Percentage share of Major District Roads length relative to the total length for the specified road category."
    }
  },
  "road_construction_projects_road_names_wise_project_cost_wise": {
    "description": "Contains information about road construction projects in Bihar, including the road names, project costs, lengths, and work status.",
    "columns": {
      "focus_area": "Department or sector under which the road construction project falls.",
      "state_name": "Name of the state where the road construction project is located (Bihar).",
      "name_of _road": "Name of the road being constructed or improved.",
      "length_in_kilometer": "Length of the road project in kilometers.",
      "project_cost_in_crore_rupee": "Cost of the road construction project in crore rupees.",
      "status_of_work": "Current status of the road construction project (e.g., completed, ongoing, upcoming)."
    }
  },
  "road_construction_schemes_year_wise": {
    "description": "Stores details of various road construction schemes in Bihar for the year 2023-24, including the amount spent, cumulative expenditure, and the type of scheme.",
    "columns": {
      "focus_area": "The department or sector under which the road construction scheme falls.",
      "state_name": "The name of the state where the scheme is implemented (Bihar).",
      "year": "The year in which the scheme data is recorded (2023-24).",
      "name_of_scheme": "The name of the specific road construction scheme.",
      "amount_spent_in_crore_rupee": "The amount of money spent on the scheme in crore rupees.",
      "actual_cumulative_expenditure_in_crore_rupee": "The actual cumulative expenditure on the scheme in crore rupees.",
      "scheme_type": "The type of scheme (e.g., state, centrally sponsored, Nischay, EAP, or RIDF)."
    }
  },
  "road_projects_bharatmala_pariyojana_year_wise": {
    "description": "Stores details of road projects under the Bharatmala Pariyojana in Bihar, including cost, length, and construction status, spanning multiple years.",
    "columns": {
      "focus_area": "The specific area or department within the project framework to which the project belongs.",
      "state_name": "Name of the state where the road project is located (Bihar).",
      "year": "Year in which the project was initiated or data was recorded.",
      "project_name": "Name or identifier of the road project.",
      "allotted_cost_in_crore_rupees": "The total cost allocated to the project in crore rupees.",
      "length_in_kilometer": "Length of the road being constructed in kilometers.",
      "construction_status": "Current status of the road construction project (e.g., 'Under construction', 'Work Awarded', 'Work Completed')."
    }
  },
  "roads_under_rwd_district_wise_block_wise_year_wise": {
    "description": "Contains information about road infrastructure projects under the Rural Works Department (RWD) in Bihar, detailing roads across districts and blocks, their lengths, associated schemes, work statuses, and the year of activity from 2001-02 to 2024-25.",
    "columns": {
      "focus_area": "Department or sector under which the data is collected (Rural Works Department).",
      "state_name": "Name of the state (Bihar).",
      "circle_name": "Name of the road construction circle.",
      "division_name": "Name of the road construction division.",
      "district_name": "Name of the district where the road is located.",
      "block_name": "Name of the block where the road is located.",
      "road_name": "Name or identifier of the road.",
      "length_in_kilometers": "Length of the road in kilometers.",
      "scheme_name": "Name of the scheme under which the road construction/repair is being carried out (e.g., MMGSY, PMGSY).",
      "work_status": "Current status of the road work (e.g., completed, ongoing, for billing).",
      "year": "Year in which the road work was undertaken."
    }
  },
  "sand_ghats_district_wise": {
    "description": "Stores the number of sand ghats in each district of Bihar, categorized by focus area (Mining and Geology).",
    "columns": {
      "state_name": "Name of the state where the sand ghats are located (Bihar).",
      "focus_area": "Department or sector responsible for the sand ghats (Mining and Geology).",
      "district_name": "Name of the district in Bihar.",
      "number_of_sand_ghats": "The number of sand ghats located in the corresponding district."
    }
  },
  "school_aanganwadi_household_water_quality_testing_yearwise": {
    "description": "Stores data on water quality testing in schools, Aanganwadi centers, and households in Bihar, providing details on registration, testing numbers, and percentages at various levels (schools, Aanganwadi centers, and households), broken down year-wise.",
    "columns": {
      "focus_area": "The department or sector responsible for the data collection (e.g., Public Health Engineering Department).",
      "state_name": "The name of the state where the water quality testing is conducted (Bihar).",
      "district_name": "The name of the district within Bihar where the water quality testing is conducted.",
      "year": "The year for which the water quality testing data is recorded (e.g., 2022-23).",
      "schools_registered_for_water_testing": "Number of schools registered for water quality testing.",
      "number_of_schools_tested": "Number of schools that were tested for water quality.",
      "percentage_of_schools_tested": "Percentage of registered schools that were actually tested for water quality.",
      "aanganwadi_centres_registered_for_water_testing": "Number of Aanganwadi centers registered for water quality testing.",
      "number_of_aanganwadi_centres_tested": "Number of Aanganwadi centers that were tested for water quality.",
      "percentage_of_aanganwadi_centres_tested": "Percentage of registered Aanganwadi centers that were actually tested for water quality.",
      "villages_registered_for_water_testing": "Number of villages registered for water quality testing.",
      "villages_where_water_samples_not_tested_at_household": "Number of villages where water samples were not tested at the household level.",
      "villages_where_water_samples_not_tested_at_household_percentage": "Percentage of villages where water samples were not tested at the household level.",
      "villages_where_water_samples_tested_in_one_household": "Number of villages where water samples were tested in one household.",
      "villages_where_water_samples_tested_in_one_household_percentage": "Percentage of villages where water samples were tested in one household.",
      "villages_where_water_samples_tested_in_two_household": "Number of villages where water samples were tested in two households.",
      "villages_where_water_samples_tested_in_two_household_pecentage": "Percentage of villages where water samples were tested in two households.",
      "villages_where_water_samples_tested_in_three_or_more_household": "Number of villages where water samples were tested in three or more households.",
      "villages_water_tested_in_three_or_more_household_percentage": "Percentage of villages where water samples were tested in three or more households."
    }
  },
  "sector_wise_start_up_bihar": {
    "description": "Stores data about sector-wise start-up activities in Bihar, including SMIC approvals and seed funding details.",
    "columns": {
      "focus_name": "Indicates the focus area or department responsible for the data.",
      "state_name": "Name of the state (Bihar).",
      "year": "Year for which the start-up data is recorded.",
      "sector_name": "Name of the sector the start-up belongs to.",
      "smic_approved": "Number of start-ups approved by the Start-up Monitoring and Implementation Committee (SMIC).",
      "first_seed_funding": "Amount of first seed funding provided to start-ups in the sector.",
      "second_seed_funding": "Amount of second seed funding provided to start-ups in the sector."
    }
  },
  "seed_analysis_report_year_wise": {
    "description": "Stores year-wise data on seed analysis in Bihar, including the number of targeted, collected, analyzed, standard, and non-standard samples.",
    "columns": {
      "focus_area": "The department or area of focus for the seed analysis program.",
      "state_name": "The name of the state where the seed analysis was conducted (Bihar).",
      "product_name": "The name of the seed product being analyzed.",
      "year": "The year in which the seed analysis was conducted.",
      "targeted_samples": "The number of seed samples targeted for analysis.",
      "collected_samples": "The number of seed samples actually collected for analysis.",
      "analyzed_samples": "The number of seed samples that were successfully analyzed.",
      "standard": "The number of seed samples that met the required quality standards.",
      "non-standard": "The number of seed samples that did not meet the required quality standards."
    }
  },
  "seed_distribution_year_wise": {
    "description": "Stores year-wise data on seed distribution targets and achievements in Bihar for various crops.",
    "columns": {
      "state_name": "Name of the state where the seed distribution occurred (Bihar).",
      "year": "Year in which the seed distribution data was recorded.",
      "focus_area": "Department or sector under which the data has been collected and stored.",
      "crop_name": "Name of the crop for which seeds were distributed (e.g., wheat, paddy, maize).",
      "target_in_metric_tonnes": "The planned or intended amount of seed distribution in metric tonnes.",
      "achievement_in_metric_tonnes": "The actual amount of seed distribution achieved in metric tonnes."
    }
  },
  "seed_production_bihar_yearwise": {
    "description": "Stores year-wise data on annual seed production in Bihar from 2018-19 to 2021-22, including annual targets, stored seeds, distributed seeds, certified seeds, and seeds meeting the Manak standard.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or sector focus (Seed Production).",
      "year": "Year of data collection (e.g., 2018-19, 2019-20).",
      "annual_target_metric tonnes": "Annual target for seed production in metric tonnes.",
      "stored_seeds_metric_tonnes": "Amount of seeds stored in metric tonnes.",
      "distributed_seeds_metric tonnes": "Amount of seeds distributed in metric tonnes.",
      "certified_seeds_metric_tonnes": "Amount of certified seeds produced in metric tonnes.",
      "manak_standard": "Data or information related to seeds that meet the Manak standard."
    }
  },
  "service_application_details_year_wise_district_wise_block_wise": {
    "description": "Stores details of service applications processed under the 'Service Plus' platform, categorized by year, district, and block, including the number of applications received, approved (within and after timeline), rejected (within and after timeline), pending, and expired.",
    "columns": {
      "year": "Year in which the service applications were processed (2019-2025).",
      "district_name": "Name of the district where the service applications were processed.",
      "block_name": "Name of the block where the service applications were processed.",
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or sector focus of the service applications.",
      "total_received_applications": "Total number of service applications received.",
      "total_approved_applications": "Total number of service applications approved.",
      "total_approved_withintimeline_applications": "Total number of service applications approved within the specified timeline.",
      "total_approved_aftertimeline_applications": "Total number of service applications approved after the specified timeline.",
      "total_rejected_applications": "Total number of service applications rejected.",
      "total_rejected_withintimeline_applications": "Total number of service applications rejected within the specified timeline.",
      "total_rejected_aftertimeline_applications": "Total number of service applications rejected after the specified timeline.",
      "total_pending_applications": "Total number of service applications currently pending.",
      "total_expired_applications": "Total number of service applications that have expired."
    }
  },
  "soil_testing_year_wise": {
    "description": "Stores soil testing data for Bihar from 2018 to 2021, including the number of soil samples collected, tested, and soil health cards distributed each year.",
    "columns": {
      "state_name": "Name of the state where soil testing is conducted (Bihar).",
      "focus_area": "Department or sector focus (likely Agriculture or related).",
      "year": "Year of data collection for soil testing activities.",
      "soil_samples_collected": "Number of soil samples collected for testing in the given year.",
      "soil_samples_tested": "Number of soil samples tested in the given year.",
      "soil_health_cards_distributed": "Number of soil health cards distributed to farmers in the given year."
    }
  },
  "state_wise_district_wise_child_birth_issues": {
    "description": "Stores health and nutrition statistics for children under five years of age, and maternal healthcare data across various districts in India.",
    "columns": {
      "id": "Unique identifier for the record.",
      "district_name": "Name of the district.",
      "district_lgd_code": "LGD (Local Government Directory) code of the district.",
      "state_name": "Name of the state.",
      "state_lgd_code": "LGD (Local Government Directory) code of the state.",
      "children_under_five_years_stunted_height_for_age": "Percentage of children under five years with stunted growth (height-for-age).",
      "children_under_five_years_anaemic": "Percentage of children under five years who are anaemic.",
      "children_under_five_years_stunted": "Percentage of children under five years who are stunted.",
      "children_under_five_years_wasted": "Percentage of children under five years who are wasted.",
      "children_under_five_years_severely_wasted": "Percentage of children under five years who are severely wasted.",
      "children_under_five_years_underweight": "Percentage of children under five years who are underweight.",
      "children_under_five_years_overweight": "Percentage of children under five years who are overweight.",
      "mothers_with_minimum_four_antenatal_care_visits": "Percentage of mothers with at least four antenatal care visits.",
      "institutional_births_in_public_facility": "Percentage of institutional births occurring in public facilities."
    }
  },
  "stone_kilns_district_wise": {
    "description": "Stores the number of stone kilns in specific districts of Bihar, focusing on data related to Mining and Geology.",
    "columns": {
      "state_name": "Name of the state where the stone kilns are located.",
      "focus_area": "The department or sector to which this data belongs, specifically Mining and Geology.",
      "district_name": "Name of the district where the stone kilns are located.",
      "number_of_stone_kilns": "Number of stone kilns present in the specified district."
    }
  },
  "students_block_wise_genderwise_class_wise_yearwise": {
    "description": "Stores student enrollment data, broken down by block, gender, class, and year, sourced from the UDISE portal for the years 2022-23 and 2023-24.",
    "columns": {
      "state_name": "Name of the state.",
      "sector_name": "Name of the sector (e.g., Education).",
      "source": "Source of the data (UDISE portal).",
      "focus_area": "Focus area or department responsible for the data.",
      "year": "Academic year for the data (2022-23 or 2023-24).",
      "district_name": "Name of the district.",
      "block_name": "Name of the block.",
      "school_name": "Name of the school.",
      "school_type": "Type of school (e.g., Government, Private).",
      "school_category": "Category of the school.",
      "pre_primary_three_boys": "Number of male students in pre-primary class three.",
      "pre_primary_three_girls": "Number of female students in pre-primary class three.",
      "pre_primary_three_transgender": "Number of transgender students in pre-primary class three.",
      "pre_primary_three_total": "Total number of students in pre-primary class three.",
      "pre_primary_two_boys": "Number of male students in pre-primary class two.",
      "pre_primary_two_girls": "Number of female students in pre-primary class two.",
      "pre_primary_two_transgender": "Number of transgender students in pre-primary class two.",
      "pre_primary_two_total": "Total number of students in pre-primary class two.",
      "pre_primary_one_boys": "Number of male students in pre-primary class one.",
      "pre_primary_one_girls": "Number of female students in pre-primary class one.",
      "pre_primary_one_transgender": "Number of transgender students in pre-primary class one.",
      "pre_primary_one_total": "Total number of students in pre-primary class one.",
      "class_one_boys": "Number of male students in class one.",
      "class_one_girls": "Number of female students in class one.",
      "class_one_transgender": "Number of transgender students in class one.",
      "class_one_total": "Total number of students in class one.",
      "class_two_boys": "Number of male students in class two.",
      "class_two_girls": "Number of female students in class two.",
      "class_two_transgender": "Number of transgender students in class two.",
      "class_two_total": "Total number of students in class two.",
      "class_three_boys": "Number of male students in class three.",
      "class_three_girls": "Number of female students in class three.",
      "class_three_transgender": "Number of transgender students in class three.",
      "class_three_total": "Total number of students in class three.",
      "class_four_boys": "Number of male students in class four.",
      "class_four_girls": "Number of female students in class four.",
      "class_four_transgender": "Number of transgender students in class four.",
      "class_four_total": "Total number of students in class four.",
      "class_five_boys": "Number of male students in class five.",
      "class_five_girls": "Number of female students in class five.",
      "class_five_transgender": "Number of transgender students in class five.",
      "class_five_total": "Total number of students in class five.",
      "class_six_boys": "Number of male students in class six.",
      "class_six_girls": "Number of female students in class six.",
      "class_six_transgender": "Number of transgender students in class six.",
      "class_six_total": "Total number of students in class six.",
      "class_seven_boys": "Number of male students in class seven.",
      "class_seven_girls": "Number of female students in class seven.",
      "class_seven_transgender": "Number of transgender students in class seven.",
      "class_seven_total": "Total number of students in class seven.",
      "class_eight_boys": "Number of male students in class eight.",
      "class_eight_girls": "Number of female students in class eight.",
      "class_eight_transgender": "Number of transgender students in class eight.",
      "class_eight_total": "Total number of students in class eight.",
      "class_nine_boys": "Number of male students in class nine.",
      "class_nine_girls": "Number of female students in class nine.",
      "class_nine_transgender": "Number of transgender students in class nine.",
      "class_nine_total": "Total number of students in class nine.",
      "class_ten_boys": "Number of male students in class ten.",
      "class_ten_girls": "Number of female students in class ten.",
      "class_ten_transgender": "Number of transgender students in class ten.",
      "class_ten_total": "Total number of students in class ten.",
      "class_eleven_boys": "Number of male students in class eleven.",
      "class_eleven_girls": "Number of female students in class eleven.",
      "class_eleven_transgender": "Number of transgender students in class eleven.",
      "class_eleven_total": "Total number of students in class eleven.",
      "class_twelve_boys": "Number of male students in class twelve.",
      "class_twelve_girls": "Number of female students in class twelve.",
      "class_twelve_transgender": "Number of transgender students in class twelve.",
      "class_twelve_total": "Total number of students in class twelve.",
      "total": "Total number of students across all classes."
    }
  },
  "sugarcane_incentive_program_yearwise": {
    "description": "Stores year-wise data from 2020 to 2024 for the sugarcane incentive program in Bihar, including program details, goals, and achievements.",
    "columns": {
      "year": "Year for which the sugarcane incentive program data is recorded (2020-2024).",
      "state_name": "Name of the state where the sugarcane incentive program is implemented (Bihar).",
      "program_type": "Type of program under the sugarcane incentive initiative.",
      "program_name": "Specific name of the program within the sugarcane incentive initiative.",
      "unit": "Unit of measurement for the physical goals and material achievements.",
      "physical_goals": "Targeted physical goals set for the program in the specified unit.",
      "financial_goals_in_lakh_rupees": "Targeted financial goals set for the program, measured in lakh rupees.",
      "material_achievement": "Actual material achievements of the program in the specified unit.",
      "financial_achievement_in_lakh_rupees": "Actual financial achievements of the program, measured in lakh rupees."
    }
  },
  "total_revenue_vs_target_year_wise": {
    "description": "Stores the year-wise revenue targets and actual revenue collected by Bihar's Mining and Geology department from 2019-20 to 2023-24, along with the percentage achievement against the set target.",
    "columns": {
      "state_name": "Name of the state (Bihar in this case).",
      "focus_area": "Department or sector focus (Mining and Geology department).",
      "year": "Fiscal year for which the revenue data is recorded (e.g., 2019-20).",
      "revenue_target_in_crores_rupees": "Revenue target set for the year, measured in crores of Indian Rupees.",
      "revenue_collected_in_crores_rupees": "Actual revenue collected during the year, measured in crores of Indian Rupees.",
      "percentage_achievement": "Percentage of the revenue target that was achieved during the year."
    }
  },
  "total_students_teachers_districtwise_non_genderwise": {
    "description": "Stores the total number of students in each class (1-12) and the total number of teachers, aggregated by district. The data is not separated by gender.",
    "columns": {
      "sector_name": "Name of the sector (e.g., Education Department).",
      "focus_area": "Specific area of focus within the sector.",
      "district_name": "Name of the district for which the data is recorded.",
      "number_of_teachers_district_wise": "Total number of teachers in the specified district.",
      "year": "Year for which the data is recorded.",
      "source": "Source of the data.",
      "state_name": "Name of the state.",
      "class_one_students": "Total number of students in Class 1.",
      "class_two_students": "Total number of students in Class 2.",
      "class_three_students": "Total number of students in Class 3.",
      "class_four_students": "Total number of students in Class 4.",
      "class_five_students": "Total number of students in Class 5.",
      "class_six_students": "Total number of students in Class 6.",
      "class_seven_students": "Total number of students in Class 7.",
      "class_eight_students": "Total number of students in Class 8.",
      "class_nine_students": "Total number of students in Class 9.",
      "class_ten_students": "Total number of students in Class 10.",
      "class_eleven_students": "Total number of students in Class 11.",
      "class_twelve_students": "Total number of students in Class 12."
    }
  },
  "tourists_place_wise_district_wise_type_wise_year_wise": {
    "description": "Stores annual tourism statistics for various destinations in Bihar from 2001 to 2014, categorized by tourist place, district, tourist type (domestic/foreign), and year.",
    "columns": {
      "state_name": "Name of the state where the tourism data is recorded (Bihar).",
      "focus_area": "The department or entity responsible for collecting and reporting the tourism data.",
      "tourism_place": "Specific tourist destination or event (e.g., Patna, Gaya, Bodh Gaya, Nalanda, Shrawani Mela, Sonepur Mela, Rajgir).",
      "district_name": "District in Bihar where the tourist place is located.",
      "tourist_type": "Type of tourist, either 'Domestic' or 'Foreign'.",
      "year": "Year in which the tourism data was recorded (from 2001 to 2014).",
      "number_of_tourists": "Number of tourists who visited the specified place in the given year."
    }
  },
  "tourists_place_wise_type_wise_year_wise_month_wise": {
    "description": "Stores data about the number of tourists (domestic and foreign) visiting different tourist places in various districts of Bihar, organized by year and month, from 2015 to 2024.",
    "columns": {
      "state_name": "Name of the state where the tourist visit occurred (Bihar).",
      "focus_area": "Indicates the department or organization responsible for collecting the data.",
      "tourism_place": "Name of the tourist place visited.",
      "district_name": "Name of the district in Bihar where the tourist place is located.",
      "type_of_tourist": "Specifies the type of tourist, either domestic or foreign.",
      "year": "The year in which the tourist visit took place.",
      "month": "The month in which the tourist visit took place.",
      "number_of_tourists": "The number of tourists who visited the specified place in the given month and year."
    }
  },
  "tourists_type_wise_year_wise_month_wise": {
    "description": "Stores monthly tourism statistics for domestic and foreign tourists visiting Bihar from 2015 to 2024.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "The department under which the data has been collected and stored.",
      "type_of_tourist": "Type of tourist, either domestic or foreign.",
      "year": "Year of the tourist visit (2015-2024).",
      "month": "Month of the tourist visit.",
      "number_of_tourists": "Number of tourists visiting in the specified month and year."
    }
  },
  "trainee_course_wise_completion_details": {
    "description": "Stores details of trainees who have completed courses at Bihar Institute of Public Administration and Rural Development (BIPARD), including induction programs for government officials, capturing information about the course, trainee demographics, and posting details.",
    "columns": {
      "course_name": "Name of the course completed by the trainee.",
      "course_start_date": "Start date of the course.",
      "course_end_date": "End date of the course.",
      "group_name": "Name of the group the trainee belongs to.",
      "trainee_name": "Name of the trainee.",
      "date_of_birth": "Date of birth of the trainee.",
      "gender": "Gender of the trainee.",
      "mobile_number": "Mobile number of the trainee.",
      "place_of_posting": "Place where the trainee is currently posted.",
      "district": "District where the trainee is currently posted.",
      "designation": "Current job designation of the trainee.",
      "course_duration_days": "Duration of the course in days.",
      "focus_area": "The focus area or subject of the course.",
      "state_name": "Name of the state (Bihar in this case).",
      "education_qualification": "Highest educational qualification of the trainee."
    }
  },
  "training_programme_details": {
    "description": "Stores details about various training programs, including schedules, participants, venue, and administrative information, spanning multiple years.",
    "columns": {
      "name_of_the_training_programme": "Name of the training program.",
      "training_start_date": "Start date of the training program.",
      "training_end_date": "End date of the training program.",
      "number_of_trainees": "Number of trainees participating in the program.",
      "group_type_of_trainee": "Type or category of the trainee group.",
      "training_days": "Number of days the training program spans.",
      "is_trainee_residential_or_non_residential": "Indicates whether the training is residential or non-residential.",
      "venue_of_training": "Location or venue where the training program is held.",
      "course_coordinator_of_training_programme": "Name of the course coordinator for the training program.",
      "department_of_trainees": "Department to which the trainees belong.",
      "year": "Year in which the training program took place.",
      "focus_area": "Focus area or subject of the training program.",
      "state_name": "Name of the state where the training program is conducted."
    }
  },
  "types_of_milk_resource": {
    "description": "Contains information about the number of different types of milk resources (milk unions, dairy plants, artificial insemination centres, and cattle feed plants) under the Bihar State Milk Co-operative Federation Ltd.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "The area of focus, likely related to dairy development or animal husbandry.",
      "type_of_milk_resources": "Type of milk resource, e.g., milk unions, dairy plants, artificial insemination centres, cattle feed plants.",
      "number_of_resources": "Number of resources of the specified type."
    }
  },
  "urban_development_schemes_and_financial_details_year_wise": {
    "description": "Stores year-wise financial and key details related to various urban development schemes under the Urban Development and Housing Department in Bihar for the year 2024-25.",
    "columns": {
      "focus_area": "Department or sector under which the data has been collected and stored (Urban Development and Housing Department).",
      "state_name": "Name of the state (Bihar).",
      "particulars": "Specific name or type of the urban development scheme or financial detail.",
      "year": "Year for which the data is recorded (2024-25).",
      "key_details": "Important information or specifics related to the scheme or financial aspect.",
      "value": "Numerical value or data associated with the scheme or financial detail, likely in lakhs."
    }
  },
  "urban_water_supply_guidelines": {
    "description": "Stores directives and guidelines for the operation, maintenance, and supervision of urban water supply projects in Bihar, including details on responsibilities, grievance redressal, maintenance protocols, and water quality checks for the year 2024-25.",
    "columns": {
      "focus_area": "The department or organization responsible for the guidelines (e.g., Urban Development and Housing Department).",
      "state_name": "The state to which the guidelines apply (Bihar).",
      "year": "The year for which the guidelines are applicable (2024-25).",
      "directive": "Specific directive or guideline related to water supply projects.",
      "key_details": "Detailed information, specifications, or procedures associated with the directive."
    }
  },
  "vehicles_auctioned_district_wise": {
    "description": "Stores data on the number of vehicles auctioned and the revenue generated from those auctions in various districts of Bihar from 2016 to 2024.",
    "columns": {
      "state_name": "Name of the state where the vehicle auctions took place (Bihar).",
      "focus_area": "Indicates the department or area under which the data was collected.",
      "year": "Year in which the vehicles were auctioned (2016-2024).",
      "district_name": "Name of the district in Bihar where the vehicle auctions took place.",
      "number_of_auctioned_vehicles": "The number of vehicles auctioned in the specified district and year.",
      "revenue_generated_from_auctioned_vehicles_in_rupees": "Revenue generated in Indian Rupees from the auctioned vehicles in the specified district and year."
    }
  },
  "veterinary_infrastructure_year_wise": {
    "description": "Stores data regarding veterinary infrastructure under the Agriculture and Allied Sectors for various years (2008-09 to 2015-16). It includes details on the number of Veterinary Hospitals, Veterinary Dispensaries, and Veterinary Institutes, along with their infrastructure values (in numbers).",
    "columns": {
      "sector_name": "Name of the sector (Agriculture and Allied Sectors).",
      "sector_id": "Unique identifier for the sector.",
      "focus_area": "Sub-division or specific area within the sector.",
      "infrastructure_name": "Name of the specific veterinary infrastructure (e.g., Veterinary Hospitals, Veterinary Dispensaries, Veterinary Institutes).",
      "year": "Year for which the infrastructure data is recorded (e.g., 2008-09, 2015-16).",
      "infrastructure_value": "The value or count of the specific infrastructure in numbers.",
      "infrastructure_unit": "Unit of measurement for the infrastructure value (likely 'numbers').",
      "source": "Source of the data (Ministry of Statistics and Programme Implementation, GOI)."
    }
  },
  "villages_tested_for_water_quality_district_wise_block_wise": {
    "description": "Stores data on water quality testing in villages of Bihar, categorized by district and block. It includes the number and percentage of villages tested chemically and bacteriologically, both pre and post-monsoon.",
    "columns": {
      "focus_area": "Indicates the department or area of focus for the data collection.",
      "state_name": "Name of the state (Bihar).",
      "block_name": "Name of the block where the village is located.",
      "village_tested": "Number of villages tested for water quality.",
      "village_to_be_tested": "Number of villages that are yet to be tested for water quality.",
      "village_tested_chemically": "Number of villages tested chemically for water quality.",
      "village_tested_chemically_percentage": "Percentage of villages tested chemically for water quality.",
      "village_tested_bacteriologically_pre_monsoon": "Number of villages tested bacteriologically before the monsoon season.",
      "village_tested_bacteriologically_pre_monsoon_percentage": "Percentage of villages tested bacteriologically before the monsoon season.",
      "village_tested_bacteriologically_post_monsoon": "Number of villages tested bacteriologically after the monsoon season.",
      "district_name": "Name of the district where the village is located.",
      "tested_date": "Date on which the water quality testing was conducted.",
      "tested_month": "Month in which the water quality testing was conducted.",
      "tested_year": "Year in which the water quality testing was conducted."
    }
  },
  "water_level_in_river_stations_in_Bihar_agriculture": {
    "description": "Stores water level data measured at various river stations in Bihar. The data represents water levels as of August 12, 2024.",
    "columns": {
      "sector_name": "Name of the sector associated with the river station.",
      "sector_id": "Unique identifier for the sector.",
      "focus_area": "The area of focus or department responsible for the data (e.g., Agriculture).",
      "station_name": "Name of the river station where the water level is measured.",
      "level_type": "Type of water level being measured (e.g., water height).",
      "date": "Date of the water level measurement (August 12, 2024).",
      "station_value": "Numerical value of the water level measurement.",
      "station_unit": "Unit of measurement for the water level (Meters).",
      "source": "Source of the data (Water Resources Department, Government of Bihar).",
      "Cell": "Additional cell information or comments related to the measurement."
    }
  },
  "water_quality_lab_testing_district_wise_block_wise": {
    "description": "Stores data on water quality lab testing, organized by district and block, including sample submission, testing results, contamination levels, and remedial measures.",
    "columns": {
      "district_name": "Name of the district where the water quality testing is conducted.",
      "block_name": "Name of the block within the district where the water quality testing is conducted.",
      "year": "Year in which the water quality testing was performed.",
      "village_name": "Name of the village where the water sample was collected.",
      "samples_submitted_total": "Total number of water samples submitted for testing.",
      "samples_submitted_not_received": "Number of submitted samples that were not received by the lab.",
      "samples_received_total": "Total number of water samples received for testing.",
      "samples_received_not_tested": "Number of received samples that were not tested.",
      "samples_tested_total": "Total number of water samples tested.",
      "samples_tested_chemical": "Number of samples tested for chemical parameters.",
      "samples_tested_bacteriological": "Number of samples tested for bacteriological parameters.",
      "samples_inconclusive_results": "Number of samples with inconclusive test results.",
      "contaminated_total": "Total number of samples found to be contaminated.",
      "contaminated_chemical": "Number of samples contaminated due to chemical factors.",
      "contaminated_bacteriological": "Number of samples contaminated due to bacteriological factors.",
      "remedial_measures_total": "Total number of remedial measures taken.",
      "remedial_measures_chemical": "Number of remedial measures taken to address chemical contamination.",
      "remedial_measures_bacteriological": "Number of remedial measures taken to address bacteriological contamination.",
      "focus_area": "Department or sector focus related to data collection (e.g., Public Health Engineering Department).",
      "state_name": "Name of the state where the data was collected."
    }
  },
  "water_quality_testing_drinking_water_sources_wise_district_wise": {
    "description": "Stores district-wise data on water quality testing of drinking water sources, including details on the number of sources tested for chemicals and bacteria, along with the percentage of sources tested.",
    "columns": {
      "state_name": "Name of the state where the water quality testing is conducted.",
      "district_name": "Name of the district where the water quality testing is conducted.",
      "date": "Date of the water quality testing data.",
      "block_name": "Name of the block where the water quality testing is conducted.",
      "total_pws_sources": "Total number of PWS (Piped Water Supply) sources.",
      "pws_sources_yet_to_be_tested": "Number of PWS sources that are yet to be tested.",
      "pws_sources_tested_for_chemicals": "Number of PWS sources tested for chemicals.",
      "pws_sources_tested_for_chemicals_percentage": "Percentage of PWS sources tested for chemicals.",
      "pws_sources_tested_for_bacteria_premonsoon": "Number of PWS sources tested for bacteria before monsoon.",
      "pws_sources_tested_for_bacteria _premonsoon_percentage": "Percentage of PWS sources tested for bacteria before monsoon.",
      "pws_sources_tested_for_bacteria_postmonsoon": "Number of PWS sources tested for bacteria after monsoon.",
      "pws_sources_tested_for_bacteria_postmonsoon_percentage": "Percentage of PWS sources tested for bacteria after monsoon.",
      "total_drinking_water_sources": "Total number of drinking water sources.",
      "drinking_water_sources_yet_to_be_tested": "Number of drinking water sources that are yet to be tested.",
      "drinking_water_sources_tested_for_chemicals": "Number of drinking water sources tested for chemicals.",
      "drinking_water_sources_tested_for_chemicals_percentage": "Percentage of drinking water sources tested for chemicals.",
      "drinking_water_sources_bacteria_test_premonsoon": "Number of drinking water sources tested for bacteria before monsoon.",
      "drinking_water_sources_bacteria_test_premonsoon.1": "Likely a duplicate or misnamed column, intended to be percentage of drinking water sources tested for bacteria before monsoon.",
      "drinking_water_sources_bacteria_test_postmonsoon": "Number of drinking water sources tested for bacteria after monsoon.",
      "drinking_water_sources_bacteria_test_postmonsoon_percentage": "Percentage of drinking water sources tested for bacteria after monsoon.",
      "total_number_of_sources": "Total number of water sources.",
      "total_sources_to_be_tested": "Total number of water sources yet to be tested.",
      "sources_tested_for_chemicals": "Number of water sources tested for chemicals.",
      "sources_tested_for_chemicals_percentage": "Percentage of water sources tested for chemicals.",
      "sources_tested_for_bacteria_premonsoon": "Number of water sources tested for bacteria before monsoon.",
      "sources_tested_for_bacteria_premonsoon_percentage": "Percentage of water sources tested for bacteria before monsoon.",
      "sources_tested_for_bacteria_postmonsoon": "Number of water sources tested for bacteria after monsoon.",
      "sources_tested_for_bacteria_postmonsoon_percentage": "Percentage of water sources tested for bacteria after monsoon.",
      "focus_area": "Department or sector focus.",
      "year": "Year of the water quality testing data."
    }
  },
  "wetlands_in_bihar_district_wise_year_wise": {
    "description": "Stores data about wetlands in Bihar, organized by district and year, including the wetland's name, location coordinates, and area.",
    "columns": {
      "focus_area": "The department or organization responsible for collecting and reporting the wetland data.",
      "state_name": "The name of the state where the wetlands are located (Bihar).",
      "year": "The year the data was collected or is applicable to (2024-25).",
      "wetland_name": "The name of the specific wetland.",
      "district_name": "The name of the district in Bihar where the wetland is located.",
      "latitude": "The latitude coordinate of the wetland's location.",
      "longitude": "The longitude coordinate of the wetland's location.",
      "total_area_in_hectare": "The total area of the wetland measured in hectares."
    }
  },
  "year_wise_bihar_sports_culture_archaeology_schemes_details": {
    "description": "Stores details about various schemes related to sports, culture, and archaeology in Bihar for the financial year 2024-25.",
    "columns": {
      "focus_area": "The department or area of focus for the scheme (e.g., Sports, Culture, Archaeology).",
      "state_name": "Name of the state where the scheme is implemented (Bihar).",
      "year": "The financial year for which the scheme details are recorded (e.g., 2024-25).",
      "activity_name": "Name of the specific scheme or activity.",
      "activity_description": "A description of the scheme's objectives and details."
    }
  },
  "year_wise_block_wise_weather_data": {
    "description": "Stores weather data for districts and blocks in Bihar from May 2023 to September 2024, including rainfall, temperature, humidity, and wind speed.",
    "columns": {
      "month": "Month for which the weather data is recorded.",
      "year": "Year for which the weather data is recorded.",
      "district_name": "Name of the district in Bihar.",
      "block_name": "Name of the block within the district.",
      "rainfall_in_millimeter": "Amount of rainfall recorded in millimeters.",
      "maximum_temperature_recorded_in_celsius": "Maximum temperature recorded in Celsius.",
      "minimum_temperature_recorded_in_celsius": "Minimum temperature recorded in Celsius.",
      "minimum_relative_humidity_in_percentage": "Minimum relative humidity recorded in percentage.",
      "average_relative_humidity_in_percentage": "Average relative humidity recorded in percentage.",
      "maximum_wind_speed_in_meter_per_second": "Maximum wind speed recorded in meters per second.",
      "state_name": "Name of the state (Bihar in this case).",
      "focus_area": "The department or organization responsible for data collection (Mausam Kendra)."
    }
  },
  "year_wise_district_wise_block_wise_cold_wave_details": {
    "description": "Stores cold wave response data for all blocks of Bihar, including information on bonfire setups, wood requirements, affected individuals, expenditures, night shelter establishments and usage, and blanket distribution.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "The department or agency responsible for collecting the data.",
      "year": "Year in which the cold wave response data was collected.",
      "district_name": "Name of the district where the cold wave response was implemented.",
      "block_name": "Name of the block within the district.",
      "number_of_bonfire_place": "Number of bonfire places established in the block.",
      "weight_of_wood_required_in_kg": "Weight of wood required for bonfires in kilograms.",
      "number_of_affected_person": "Number of people affected by the cold wave in the block.",
      "total_amount_spent_in_rupee": "Total amount of money spent on cold wave relief efforts in Indian Rupees.",
      "number_of_night_shelter_established": "Number of night shelters established in the block.",
      "total_number_of_night_shelter_required": "The total number of night shelters required in the block.",
      "number_of_person_in_night_shelter": "Number of people using night shelters in the block.",
      "capacity_of_night_shelter": "Total capacity of the night shelters in the block.",
      "number_of_blankets_distributed": "Number of blankets distributed to affected people in the block."
    }
  },
  "year_wise_district_wise_covid_payment": {
    "description": "Stores data about COVID-19 relief payments distributed across districts of Bihar, detailing the number of people who received ₹4 lakh and ₹50,000 financial assistance each year.",
    "columns": {
      "state": "Name of the state (Bihar).",
      "focus_area": "Indicates the department or area responsible for the data (e.g., Disaster Management, Health).",
      "year": "Year in which the COVID-19 relief payment was disbursed.",
      "district_name": "Name of the district where the relief payment was distributed.",
      "number_of_person_alloted_four_lakhs_rupees": "Number of people in the district who received ₹4 lakh in COVID-19 relief.",
      "number_of_person_alloted_fifty_thousand_rupees": "Number of people in the district who received ₹50,000 in COVID-19 relief."
    }
  },
  "year_wise_district_wise_ejanani_beneficiaries": {
    "description": "Stores data on e-Janani beneficiaries in Bihar, providing details on payments made to mothers for institutional delivery and complete immunization under the Mukhyamantri Kanya Utthan Yojna, broken down by year, district, block, and panchayat.",
    "columns": {
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Department or sector under which the data has been collected and stored (e.g., Health, Social Welfare).",
      "district_name": "Name of the district in Bihar.",
      "block_name": "Name of the block within the district.",
      "panchayat_name": "Name of the panchayat within the block.",
      "gender": "Gender of the beneficiary (all Female).",
      "category_type": "Caste category of the beneficiary (e.g., General, BC, EBC, SC, ST, OBC).",
      "total_amount": "Total amount disbursed to the beneficiary.",
      "year": "Year in which the payment was made."
    }
  },
  "year_wise_district_wise_flood_affected_data": {
    "description": "Stores year-wise and district-wise data detailing the impact of floods in Bihar, including affected populations, damage to property and agriculture, and relief efforts.",
    "columns": {
      "state_name": "Name of the state affected by floods (Bihar).",
      "focus_area": "The department or sector under which the data was collected.",
      "year": "Year in which the flood occurred.",
      "district_name": "Name of the district affected by floods.",
      "number_of_persons_affected": "Number of individuals affected by the floods.",
      "number_of_families_affected": "Number of families affected by the floods.",
      "total_migrated_population": "Total number of people who migrated due to the floods.",
      "affected_agricultural_land_in_acre": "Area of agricultural land affected by the floods, measured in acres.",
      "affected_non_agricultural_land_in_acre": "Area of non-agricultural land affected by the floods, measured in acres.",
      "damaged_crop_area_in_acre": "Area of crops damaged due to the floods, measured in acres.",
      "damaged_crop_value_in_rupees": "Monetary value of the crops damaged, in Rupees.",
      "number_of_fully_affected_kutcha_houses": "Number of temporary houses fully damaged by the floods.",
      "number_of_partly_affected_kutcha_houses": "Number of temporary houses partially damaged by the floods.",
      "number_of_fully_affected_pakka_houses": "Number of permanent houses fully damaged by the floods.",
      "number_of_partly_affected_pakka_houses": "Number of permanent houses partially damaged by the floods.",
      "number_of_affected_huts": "Number of huts affected by the floods.",
      "number_of_affected_animal_sheds": "Number of animal sheds affected by the floods.",
      "value_of_damaged_houses_in_rupees": "Monetary value of the houses damaged, in Rupees.",
      "value_of_damaged_public_property": "Monetary value of the public property damaged, in Rupees.",
      "number_of_water_encircled_villages": "Number of villages surrounded by floodwater.",
      "number_of_dead_persons": "Number of human fatalities caused by the floods.",
      "number_of_affected_animals": "Number of animals affected by the floods.",
      "number_of_animal_camps": "Number of animal camps established for flood relief.",
      "number_of_animals_treated": "Number of animals that received medical treatment in the animal camps.",
      "number_of_small_milch_animals": "Number of small milk-producing animals affected.",
      "number_of_big_milch_animals": "Number of large milk-producing animals affected.",
      "number_of_small_non_milch_animals": "Number of small non-milk-producing animals affected.",
      "number_of_big_non_milch_aimals": "Number of large non-milk-producing animals affected.",
      "number_of_damaged_fish_seed_farms": "Number of fish seed farms damaged by the floods.",
      "number_of_fully_damaged_boats": "Number of boats fully damaged by the floods.",
      "number_of_partly_damaged_boats": "Number of boats partially damaged by the floods.",
      "number_of_fully_damaged_nets": "Number of fishing nets fully damaged by the floods.",
      "number_of_partly_damaged_nets": "Number of fishing nets partially damaged by the floods.",
      "number_of_relief_centres_opened": "Number of relief centers opened to provide assistance to flood victims.",
      "number_of_relief_centres_closed": "Number of relief centers that were closed.",
      "number_of_active_relief_centres": "Number of relief centers that were active.",
      "number_of_person_registered": "Number of individuals registered at the relief centers.",
      "number_of_person_left_camp": "Number of individuals who left the relief camps.",
      "number_of_active_kitchens": "Number of active kitchens providing meals at relief centers.",
      "number_of_closed_kitchens": "Number of kitchens that were closed.",
      "number_of_person_provided_lunch": "Number of individuals provided with lunch at relief centers.",
      "number_of_person_provided_dinner": "Number of individuals provided with dinner at relief centers.",
      "number_of_person_treated": "Number of individuals who received medical treatment at relief centers or other medical facilities.",
      "number_of_dry_ration_packets_distributed": "Number of dry ration packets distributed to flood victims.",
      "number_of_food_packets_distributed": "Number of food packets distributed to flood victims."
    }
  },
  "year_wise_houses_sanctioned_under_pmay_scheme": {
    "description": "Stores the year-wise number of houses sanctioned under the Pradhan Mantri Awas Yojana (PMAY) scheme in each district of Bihar from 2016 to 2024.",
    "columns": {
      "sector_name": "The sector to which the scheme belongs, such as Rural Development.",
      "district_name": "Name of the district in Bihar where houses were sanctioned.",
      "year": "Year in which the houses were sanctioned under the PMAY scheme.",
      "number_of_house": "The number of houses sanctioned in the specified district and year.",
      "state_name": "Name of the state (Bihar).",
      "focus_area": "Indicates the specific focus area or department responsible for the data collection and implementation of the scheme.",
      "scheme_name": "Name of the scheme (Pradhan Mantri Awas Yojana - PMAY)."
    }
  }
}

