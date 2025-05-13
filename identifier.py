from typing import List, Dict, Any

def identify_relevant_tables(user_input: str, table_schemas: Dict[str, Any]) -> List[str]:
    """Identify relevant tables for the user question from table_schemas"""
    input_lower = user_input.lower()
    matched_tables = set()

    # Predefined keyword-to-table mapping for quick relevance
    KEYWORD_TABLE_MAP = {
    "police": "Bihar_police_station",
    "police station": "Bihar_police_station",
    "subdivision": "Bihar_police_station",
    "range": "Bihar_police_station",
    "thana": "Bihar_police_station",
    "district police": "Bihar_police_station",

    "pension": "Bihar_jp_senani_scheme_District_wise",
    "jp senani": "Bihar_jp_senani_scheme_District_wise",
    "freedom fighter": "Bihar_jp_senani_scheme_District_wise",
    "senani yojana": "Bihar_jp_senani_scheme_District_wise",

    "hydrant": "Bihar_district_wise_water_hydrant",
    "fire hydrant": "Bihar_district_wise_water_hydrant",
    "water hydrant": "Bihar_district_wise_water_hydrant",

    "fire vehicle": "Bihar_district_wise_fire_vehicle",
    "fire engine": "Bihar_district_wise_fire_vehicle",
    "fire tanker": "Bihar_district_wise_fire_vehicle",
    "fire truck": "Bihar_district_wise_fire_vehicle",
    "fire brigade": "Bihar_district_wise_fire_vehicle",

    "enrollment": "Block_wise_enrollment_of_students_gender_class_wise_year_wise",
    "student enrollment": "Block_wise_enrollment_of_students_gender_class_wise_year_wise",
    "block wise enrollment": "Block_wise_enrollment_of_students_gender_class_wise_year_wise",
    "class wise enrollment": "Block_wise_enrollment_of_students_gender_class_wise_year_wise",
    "gender wise enrollment": "Block_wise_enrollment_of_students_gender_class_wise_year_wise",
    "year wise enrollment": "Block_wise_enrollment_of_students_gender_class_wise_year_wise",
    "school enrollment": "Block_wise_enrollment_of_students_gender_class_wise_year_wise",
    "student data": "Block_wise_enrollment_of_students_gender_class_wise_year_wise",
    "pre primary enrollment": "Block_wise_enrollment_of_students_gender_class_wise_year_wise",
    "primary enrollment": "Block_wise_enrollment_of_students_gender_class_wise_year_wise",
    "secondary enrollment": "Block_wise_enrollment_of_students_gender_class_wise_year_wise",
    "higher secondary enrollment": "Block_wise_enrollment_of_students_gender_class_wise_year_wise",
    "boys enrollment": "Block_wise_enrollment_of_students_gender_class_wise_year_wise",
    "girls enrollment": "Block_wise_enrollment_of_students_gender_class_wise_year_wise",
    "transgender enrollment": "Block_wise_enrollment_of_students_gender_class_wise_year_wise",

    "school infrastructure": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "school facilities": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "block wise school infrastructure": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "district wise school infrastructure": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "school buildings": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "classrooms": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "toilet facilities": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "drinking water": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "electricity": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "library": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "playground": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "medical checkup": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "health records": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "first aid kit": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "ramp": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "handrails": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "kitchen garden": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "kitchen shed": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "furniture": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "boundary wall": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "water purifier": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "rainwater harvesting": "Bihar_District_block_wise_School_infrastructure_and_facilities",
    "solar panels": "Bihar_District_block_wise_School_infrastructure_and_facilities",

    
    "land dispute": "Cases_of_Land_dispute_in_bihar",
    "property dispute": "Cases_of_Land_dispute_in_bihar",
    "dispute cases": "Cases_of_Land_dispute_in_bihar",
    "police land case": "Cases_of_Land_dispute_in_bihar",
    "number of land disputes": "Cases_of_Land_dispute_in_bihar",

   
    "civil seva": "Civil_Seva_Protsahan_Yojna_for_bc_ebc_students",
    "protsahan yojna": "Civil_Seva_Protsahan_Yojna_for_bc_ebc_students",
    "upsc incentive": "Civil_Seva_Protsahan_Yojna_for_bc_ebc_students",
    "bpsc incentive": "Civil_Seva_Protsahan_Yojna_for_bc_ebc_students",
    "ebc student scheme": "Civil_Seva_Protsahan_Yojna_for_bc_ebc_students",
    "bc student scheme": "Civil_Seva_Protsahan_Yojna_for_bc_ebc_students",
    "student payment": "Civil_Seva_Protsahan_Yojna_for_bc_ebc_students",
    "financial assistance upsc": "Civil_Seva_Protsahan_Yojna_for_bc_ebc_students",
    "financial assistance bpsc": "Civil_Seva_Protsahan_Yojna_for_bc_ebc_students",

    # For Civil Seva Protsahan for female students
    "civil seva female": "Civil_Seva_Protsahan_Yojna_for_female_students",
    "female students upsc": "Civil_Seva_Protsahan_Yojna_for_female_students",
    "female students bpsc": "Civil_Seva_Protsahan_Yojna_for_female_students",
    "female incentive": "Civil_Seva_Protsahan_Yojna_for_female_students",
    "female payment scheme": "Civil_Seva_Protsahan_Yojna_for_female_students",
    "protsahan yojna female": "Civil_Seva_Protsahan_Yojna_for_female_students",
    "girls incentive": "Civil_Seva_Protsahan_Yojna_for_female_students",

    # For Digital India Land Records
    "digital india land records": "District_wise_Digital_India_Land_Records_Modernization_Programme",
    "land records modernization": "District_wise_Digital_India_Land_Records_Modernization_Programme",
    "digitized maps": "District_wise_Digital_India_Land_Records_Modernization_Programme",
    "computerized land records": "District_wise_Digital_India_Land_Records_Modernization_Programme",
    "sub registrar linked": "District_wise_Digital_India_Land_Records_Modernization_Programme",

    # For Direct Benefit Transfer
    "direct benefit transfer": "District_wise_Direct_Benefit_Transfer",
    "dbt": "District_wise_Direct_Benefit_Transfer",
    "benefit transfer data": "District_wise_Direct_Benefit_Transfer",
    "dbt beneficiaries": "District_wise_Direct_Benefit_Transfer",
    "dbt fund": "District_wise_Direct_Benefit_Transfer",
    "dbt transaction": "District_wise_Direct_Benefit_Transfer",

    # Fertilizer Stock and Supply
    "fertilizer stock": "District_wise_Fertilizer_Stock_Supply",
    "urea supply": "District_wise_Fertilizer_Stock_Supply",
    "non urea stock": "District_wise_Fertilizer_Stock_Supply",
    "fertilizer requirement": "District_wise_Fertilizer_Stock_Supply",
    
    # Horticulture Area and Production
    "horticulture production": "Horticulture_area_production_yearwise",
    "horticulture crops": "Horticulture_area_production_yearwise",
    "crop production data": "Horticulture_area_production_yearwise",
    "area under horticulture": "Horticulture_area_production_yearwise",
    
    # Hostel SC/ST Scheme
    "hostel grant sc st": "Hostel_grant_scheme_SCST_district_category_gender_wise",
    "sc st hostel": "Hostel_grant_scheme_SCST_district_category_gender_wise",
    "hostel scholarship": "Hostel_grant_scheme_SCST_district_category_gender_wise",
    "cm sc st hostel": "Hostel_grant_scheme_SCST_district_category_gender_wise",

    # JJHM Scheme
    "jjhm scheme": "JJHM_Scheme_structure_and_amount_allotment",
    "jjhm amount allotment": "JJHM_Scheme_structure_and_amount_allotment",
    "jjhm project": "JJHM_Scheme_structure_and_amount_allotment",
    "jjhm structure": "JJHM_Scheme_structure_and_amount_allotment",

    # JJHM Nursery
    "jjhm nursery": "JJHM_nursery_data",
    "nursery trees": "JJHM_nursery_data",
    "bihar nursery": "JJHM_nursery_data",
    "nursery area": "JJHM_nursery_data",

    # MMUY & BLUY Category-wise
    "mmuy category": "MMUY_BLUY_beneficiaries_category_wise",
    "bluy category": "MMUY_BLUY_beneficiaries_category_wise",
    "udyami yojna category": "MMUY_BLUY_beneficiaries_category_wise",

    # MMUY & BLUY District-wise
    "mmuy district": "MMUY_BLUY_beneficiaries_district_wise",
    "bluy district": "MMUY_BLUY_beneficiaries_district_wise",
    "udyami yojna district": "MMUY_BLUY_beneficiaries_district_wise",

    # MMUY & BLUY Project-wise
    "mmuy project": "MMUY_BLUY_beneficiaries_project_wise",
    "bluy project": "MMUY_BLUY_beneficiaries_project_wise",
    "udyami yojna business": "MMUY_BLUY_beneficiaries_project_wise",
    "udyami entrepreneurship": "MMUY_BLUY_beneficiaries_project_wise",

    # MMUY/BLUY year-wise
    "mmuy year": "MMUY_BLUY_beneficiaries_year_wise",
    "bluy year": "MMUY_BLUY_beneficiaries_year_wise",
    "udyami yojna year wise": "MMUY_BLUY_beneficiaries_year_wise",

    # Muzaffarpur Smart City
    "muzaffarpur smart city": "Muzaffarpur_smartcity_projectwise_progress_report",
    "muzaffarpur smartcity project": "Muzaffarpur_smartcity_projectwise_progress_report",
    "muzaffarpur smartcity progress": "Muzaffarpur_smartcity_projectwise_progress_report",

    # Paddy Procurement
    "paddy procurement": "Paddy_Procurement_districtwise_yearwise_in_Bihar",
    "paddy data": "Paddy_Procurement_districtwise_yearwise_in_Bihar",
    "district wise paddy": "Paddy_Procurement_districtwise_yearwise_in_Bihar",
    "paddy year wise": "Paddy_Procurement_districtwise_yearwise_in_Bihar",

    # Patna Smart City
    "patna smart city": "Patna_smartcity_projectwise_progress_report",
    "patna smartcity project": "Patna_smartcity_projectwise_progress_report",
    "patna project progress": "Patna_smartcity_projectwise_progress_report",

    # 1. Payment_given_to_farmers_for_crops_loss_blockwise_yearwise
    "payment_given_to_farmers_for_crops_loss_blockwise_yearwise": "Payment_given_to_farmers_for_crops_loss_blockwise_yearwise",
    "farmer crop loss payment": "Payment_given_to_farmers_for_crops_loss_blockwise_yearwise",
    "crop loss compensation": "Payment_given_to_farmers_for_crops_loss_blockwise_yearwise",
    "crop loss farmers blockwise": "Payment_given_to_farmers_for_crops_loss_blockwise_yearwise",
    "payment for agricultural damage": "Payment_given_to_farmers_for_crops_loss_blockwise_yearwise",
    "blockwise crop compensation": "Payment_given_to_farmers_for_crops_loss_blockwise_yearwise",
    "payment to farmers by block and year": "Payment_given_to_farmers_for_crops_loss_blockwise_yearwise",
    "scheme-wise crop loss support": "Payment_given_to_farmers_for_crops_loss_blockwise_yearwise",
    "crop failure payment": "Payment_given_to_farmers_for_crops_loss_blockwise_yearwise",

    # 2. Payment_students_for_basic_facilities_blockwise_in_Bihar
    "payment_students_for_basic_facilities_blockwise_in_Bihar": "Payment_students_for_basic_facilities_blockwise_in_Bihar",
    "student support payments": "Payment_students_for_basic_facilities_blockwise_in_Bihar",
    "basic facilities for students": "Payment_students_for_basic_facilities_blockwise_in_Bihar",
    "student welfare blockwise": "Payment_students_for_basic_facilities_blockwise_in_Bihar",
    "student scheme payments bihar": "Payment_students_for_basic_facilities_blockwise_in_Bihar",
    "blockwise student benefit disbursement": "Payment_students_for_basic_facilities_blockwise_in_Bihar",
    "payments to students by block": "Payment_students_for_basic_facilities_blockwise_in_Bihar",
    "education assistance to students": "Payment_students_for_basic_facilities_blockwise_in_Bihar",

    # 3. State_level_banker_Committee_loan_applied
    "state_level_banker_Committee_loan_applied": "State_level_banker_Committee_loan_applied",
    "slbc loan applications": "State_level_banker_Committee_loan_applied",
    "loan applications by block": "State_level_banker_Committee_loan_applied",
    "loan applied under government schemes": "State_level_banker_Committee_loan_applied",
    "state banker committee data": "State_level_banker_Committee_loan_applied",
    "department loan application data": "State_level_banker_Committee_loan_applied",
    "loan request status by district": "State_level_banker_Committee_loan_applied",
    "loan applied via state schemes": "State_level_banker_Committee_loan_applied",
    "loan submission statistics bihar": "State_level_banker_Committee_loan_applied",

    # 4. Temporary_shelters_during_winter_season
    "temporary_shelters_during_winter_season": "Temporary_shelters_during_winter_season",
    "winter shelters data": "Temporary_shelters_during_winter_season",
    "homeless shelters winter bihar": "Temporary_shelters_during_winter_season",
    "temporary night shelters": "Temporary_shelters_during_winter_season",
    "shelter bed availability 2024": "Temporary_shelters_during_winter_season",
    "cold season relief shelters": "Temporary_shelters_during_winter_season",
    "ulb shelter facility data": "Temporary_shelters_during_winter_season",
    "temporary accommodation during winter": "Temporary_shelters_during_winter_season",
    "beds in urban shelters bihar": "Temporary_shelters_during_winter_season",

    # 5. Tri_cycle_distribution_district_wise
    "tri_cycle_distribution_district_wise": "Tri_cycle_distribution_district_wise",
    "tricycle distribution for disabled": "Tri_cycle_distribution_district_wise",
    "tricycle scheme district wise": "Tri_cycle_distribution_district_wise",
    "tricycle support physically handicapped": "Tri_cycle_distribution_district_wise",
    "tricycle beneficiaries data": "Tri_cycle_distribution_district_wise",
    "assistive device distribution": "Tri_cycle_distribution_district_wise",
    "district-wise disability support": "Tri_cycle_distribution_district_wise",
    "tricycle distribution statistics": "Tri_cycle_distribution_district_wise",
    "tricycle allocation by district": "Tri_cycle_distribution_district_wise",

    "water_resource_in_bihar": "Water_resource_in_bihar",
    "irrigation schemes in Bihar": "Water_resource_in_bihar",
    "water resources district-wise": "Water_resource_in_bihar",
    "scheme infrastructure details": "Water_resource_in_bihar",
    "nalkup defect data": "Water_resource_in_bihar",
    "water distribution statistics": "Water_resource_in_bihar",
    "village level irrigation scheme": "Water_resource_in_bihar",
    "water scheme inspection": "Water_resource_in_bihar",
    "energy type irrigation": "Water_resource_in_bihar",
    "dam canal dimensions": "Water_resource_in_bihar",
    "agricultural water source": "Water_resource_in_bihar",

    "weather_shelters_under_day_nulm_scheme": "Weather_shelters_under_day_nulm_scheme",
    "DAY-NULM shelters": "Weather_shelters_under_day_nulm_scheme",
    "urban weather shelters": "Weather_shelters_under_day_nulm_scheme",
    "shelter homes Bihar": "Weather_shelters_under_day_nulm_scheme",
    "homeless shelters 2024": "Weather_shelters_under_day_nulm_scheme",
    "weather shelter capacity": "Weather_shelters_under_day_nulm_scheme",
    "DAY-NULM infrastructure": "Weather_shelters_under_day_nulm_scheme",
    "urban shelter statistics": "Weather_shelters_under_day_nulm_scheme",
    "district-wise shelter report": "Weather_shelters_under_day_nulm_scheme",
    "refurbished shelters DAY-NULM": "Weather_shelters_under_day_nulm_scheme",

    "wheat_procurement_districtwise_yearwise_in_bihar": "Wheat_Procurement_districtwise_yearwise_in_Bihar",
    "district-wise wheat procurement": "Wheat_Procurement_districtwise_yearwise_in_Bihar",
    "procurement year-wise wheat": "Wheat_Procurement_districtwise_yearwise_in_Bihar",
    "wheat procurement statistics": "Wheat_Procurement_districtwise_yearwise_in_Bihar",
    "farmers wheat supply data": "Wheat_Procurement_districtwise_yearwise_in_Bihar",
    "category-wise farmer data": "Wheat_Procurement_districtwise_yearwise_in_Bihar",
    "male vs female farmers wheat": "Wheat_Procurement_districtwise_yearwise_in_Bihar",
    "SC ST wheat procurement": "Wheat_Procurement_districtwise_yearwise_in_Bihar",
    "procured wheat quantity Bihar": "Wheat_Procurement_districtwise_yearwise_in_Bihar",
    "total amount paid to farmers": "Wheat_Procurement_districtwise_yearwise_in_Bihar",

    "abhiyan_basera_beneficiary_year_wise_district_wise_category_wise": "abhiyan_basera_beneficiary_year_wise_district_wise_category_wise",
    "Abhiyan Basera program data": "abhiyan_basera_beneficiary_year_wise_district_wise_category_wise",
    "category-wise beneficiaries": "abhiyan_basera_beneficiary_year_wise_district_wise_category_wise",
    "district-wise basera scheme": "abhiyan_basera_beneficiary_year_wise_district_wise_category_wise",
    "basera beneficiaries 2024-25": "abhiyan_basera_beneficiary_year_wise_district_wise_category_wise",
    "caste-wise basera stats": "abhiyan_basera_beneficiary_year_wise_district_wise_category_wise",
    "EBC SC ST beneficiaries basera": "abhiyan_basera_beneficiary_year_wise_district_wise_category_wise",
    "Basera caste-wise summary": "abhiyan_basera_beneficiary_year_wise_district_wise_category_wise",
    "Abhiyan Basera report": "abhiyan_basera_beneficiary_year_wise_district_wise_category_wise",
    "beneficiary caste data": "abhiyan_basera_beneficiary_year_wise_district_wise_category_wise",

    "age_wise_houses_sanctioned_under_pmay_scheme": "age_wise_houses_sanctioned_under_pmay_scheme",
    "PMAY age-wise housing data": "age_wise_houses_sanctioned_under_pmay_scheme",
    "sanctioned houses by age": "age_wise_houses_sanctioned_under_pmay_scheme",
    "age group housing scheme": "age_wise_houses_sanctioned_under_pmay_scheme",
    "district-wise PMAY housing": "age_wise_houses_sanctioned_under_pmay_scheme",
    "Pradhan Mantri Awas Yojana Bihar": "age_wise_houses_sanctioned_under_pmay_scheme",
    "2023 PMAY housing sanction": "age_wise_houses_sanctioned_under_pmay_scheme",
    "age distribution housing data": "age_wise_houses_sanctioned_under_pmay_scheme",
    "PMAY sanctioned report": "age_wise_houses_sanctioned_under_pmay_scheme",
    "youth and elderly housing stats": "age_wise_houses_sanctioned_under_pmay_scheme",

    "aggregate_technical_commercial_loss_year_wise": "aggregate_technical_commercial_loss_year_wise",
    "electricity loss percentage": "aggregate_technical_commercial_loss_year_wise",
    "technical commercial loss data": "aggregate_technical_commercial_loss_year_wise",
    "AT&C loss percentage": "aggregate_technical_commercial_loss_year_wise",
    "state-wise electricity loss": "aggregate_technical_commercial_loss_year_wise",
    "yearly power loss data": "aggregate_technical_commercial_loss_year_wise",
    "electricity distribution loss": "aggregate_technical_commercial_loss_year_wise",
    "power sector performance metrics": "aggregate_technical_commercial_loss_year_wise",
    "energy loss statistics": "aggregate_technical_commercial_loss_year_wise",
    "utility performance indicators": "aggregate_technical_commercial_loss_year_wise",

    "agricultural_administration_buildings_district_wise": "agricultural_administration_buildings_district_wise",
    "Bihar agriculture department buildings": "agricultural_administration_buildings_district_wise",
    "district-wise govt buildings": "agricultural_administration_buildings_district_wise",
    "panchayat administration infrastructure": "agricultural_administration_buildings_district_wise",
    "agriculture department facilities": "agricultural_administration_buildings_district_wise",
    "Bihar rented government buildings": "agricultural_administration_buildings_district_wise",
    "agricultural office infrastructure": "agricultural_administration_buildings_district_wise",
    "district administration buildings": "agricultural_administration_buildings_district_wise",
    "Bihar panchayat buildings": "agricultural_administration_buildings_district_wise",
    "agriculture department real estate": "agricultural_administration_buildings_district_wise",

    "agriculture_equipment_subsidy_bihar": "agriculture_equipment_subsidy_bihar",
    "Bihar farm equipment subsidies": "agriculture_equipment_subsidy_bihar",
    "agricultural machinery subsidy": "agriculture_equipment_subsidy_bihar",
    "SC/ST farming subsidies": "agriculture_equipment_subsidy_bihar",
    "farm equipment financial aid": "agriculture_equipment_subsidy_bihar",
    "agriculture subsidy rates": "agriculture_equipment_subsidy_bihar",
    "Bihar farmer support schemes": "agriculture_equipment_subsidy_bihar",
    "Happy Seeder subsidy": "agriculture_equipment_subsidy_bihar",
    "Chisel Cutter funding": "agriculture_equipment_subsidy_bihar",
    "agricultural mechanization support": "agriculture_equipment_subsidy_bihar",

    
    "allotment_of_grains_district_wise_year_wise": "allotment_of_grains_district_wise_year_wise",
    "Bihar grain distribution": "allotment_of_rains_district_wise_year_wise",
    "AAY PHH rice wheat allocation": "allotment_of_grains_district_wise_year_wise",
    "fortified rice distribution": "allotment_of_grains_district_wise_year_wise",
    "monthly grain allotment": "allotment_of_grains_district_wise_year_wise",
    "food security scheme data": "allotment_of_grains_district_wise_year_wise",
    "Bihar PDS grain records": "allotment_of_grains_district_wise_year_wise",
    "district-wise food allocation": "allotment_of_grains_district_wise_year_wise",
    "Antyodaya Anna Yojana grains": "allotment_of_grains_district_wise_year_wise",
    "Priority Household rations": "allotment_of_grains_district_wise_year_wise",
    "Bihar food subsidy distribution": "allotment_of_grains_district_wise_year_wise",

    "application_details_service_wise": "application_details_service_wise",
    "Bihar Service Plus metrics": "application_details_service_wise",
    "public service applications": "application_details_service_wise",
    "certificate approval stats": "application_details_service_wise",
    "government service pendency": "application_details_service_wise",
    "application processing timeline": "application_details_service_wise",
    "service rejection rates": "application_details_service_wise",
    "Bihar digital service performance": "application_details_service_wise",
    "e-governance application data": "application_details_service_wise",
    "birth registration applications": "application_details_service_wise",
    "caste certificate approvals": "application_details_service_wise",

    "area_of_crop_irrigation_yearwise_trend_Bihar": "area_of_crop_irrigation_yearwise_trend_Bihar",
    "Bihar irrigated crop area": "area_of_crop_irrigation_yearwise_trend_Bihar",
    "crop-wise irrigation data": "area_of_crop_irrigation_yearwise_trend_Bihar",
    "agricultural water use stats": "area_of_crop_irrigation_yearwise_trend_Bihar",
    "hectares under irrigation": "area_of_crop_irrigation_yearwise_trend_Bihar",
    "Bihar farming irrigation": "area_of_crop_irrigation_yearwise_trend_Bihar",
    "crop season irrigation": "area_of_crop_irrigation_yearwise_trend_Bihar",
    "agricultural land water coverage": "area_of_crop_irrigation_yearwise_trend_Bihar",
    "Patna agri statistics": "area_of_crop_irrigation_yearwise_trend_Bihar",
    "irrigated farmland records": "area_of_crop_irrigation_yearwise_trend_Bihar",

    "arrests_seized_liquor_seized_vehicles_district_wise_year_wise": "arrests_seized_liquor_seized_vehicles_district_wise_year_wise",
    "Bihar prohibition enforcement": "arrests_seized_liquor_seized_vehicles_district_wise_year_wise",
    "liquor raid statistics": "arrests_seized_liquor_seized_vehicles_district_wise_year_wise",
    "illegal alcohol seizures": "arrests_seized_liquor_seized_vehicles_district_wise_year_wise",
    "excise department cases": "arrests_seized_liquor_seized_vehicles_district_wise_year_wise",
    "confiscated vehicles Bihar": "arrests_seized_liquor_seized_vehicles_district_wise_year_wise",
    "country liquor seizures": "arrests_seized_liquor_seized_vehicles_district_wise_year_wise",
    "prohibition arrest records": "arrests_seized_liquor_seized_vehicles_district_wise_year_wise",
    "Bihar dry law enforcement": "arrests_seized_liquor_seized_vehicles_district_wise_year_wise",
    "illegal liquor trafficking": "arrests_seized_liquor_seized_vehicles_district_wise_year_wise",

    "art_culture_youth_department_bihar_organization_structure": "art_culture_youth_department_bihar_organization_structure",
    "Bihar culture department org": "art_culture_youth_department_bihar_organization_structure",
    "art department hierarchy": "art_culture_youth_department_bihar_organization_structure",
    "cultural affairs personnel": "art_culture_youth_department_bihar_organization_structure",
    "youth department structure": "art_culture_youth_department_bihar_organization_structure",
    "Bihar government cultural roles": "art_culture_youth_department_bihar_organization_structure",
    "art department officials": "art_culture_youth_department_bihar_organization_structure",
    "culture ministry Bihar": "art_culture_youth_department_bihar_organization_structure",
    "departmental organization chart": "art_culture_youth_department_bihar_organization_structure",
    "government cultural positions": "art_culture_youth_department_bihar_organization_structure",

    "art_culture_youth_department_events_timeline_year_wise": "art_culture_youth_department_events_timeline_year_wise",
    "Bihar cultural events": "art_culture_youth_department_events_timeline_year_wise",
    "art department calendar": "art_culture_youth_department_events_timeline_year_wise",
    "youth programs timeline": "art_culture_youth_department_events_timeline_year_wise",
    "cultural festival records": "art_culture_youth_department_events_timeline_year_wise",
    "Bihar event chronology": "art_culture_youth_department_events_timeline_year_wise",
    "government cultural activities": "art_culture_youth_department_events_timeline_year_wise",
    "art exhibition schedule": "art_culture_youth_department_events_timeline_year_wise",
    "departmental event log": "art_culture_youth_department_events_timeline_year_wise",
    "cultural program archive": "art_culture_youth_department_events_timeline_year_wise",

    "auctioned_or_seized_vehicle_or_land": "auctioned_or_seized_vehicle_or_land",
    "Bihar confiscated property": "auctioned_or_seized_vehicle_or_land",
    "government vehicle auctions": "auctioned_or_seized_vehicle_or_land",
    "seized land records": "auctioned_or_seized_vehicle_or_land",
    "penalty released vehicles": "auctioned_or_seized_vehicle_or_land",
    "property confiscation stats": "auctioned_or_seized_vehicle_or_land",
    "Bihar law enforcement seizures": "auctioned_or_seized_vehicle_or_land",
    "auctioned premises data": "auctioned_or_seized_vehicle_or_land",
    "government auction records": "auctioned_or_seized_vehicle_or_land",
    "revenue department seizures": "auctioned_or_seized_vehicle_or_land",

    "balak_balika_protsahan_yojan_number_of_beneficiaries": "balak_balika_protsahan_yojan_number_of_beneficiaries",
    "Bihar student scholarship": "balak_balika_protsahan_yojan_number_of_beneficiaries",
    "10th grade achievers": "balak_balika_protsahan_yojan_number_of_beneficiaries",
    "education incentive scheme": "balak_balika_protsahan_yojan_number_of_beneficiaries",
    "student merit rewards": "balak_balika_protsahan_yojan_number_of_beneficiaries",
    "gender-wise beneficiaries": "balak_balika_protsahan_yojan_number_of_beneficiaries",
    "caste-based education aid": "balak_balika_protsahan_yojan_number_of_beneficiaries",
    "Bihar youth incentives": "balak_balika_protsahan_yojan_number_of_beneficiaries",
    "academic achievement scheme": "balak_balika_protsahan_yojan_number_of_beneficiaries",
    "district scholarship data": "balak_balika_protsahan_yojan_number_of_beneficiaries",

    "beneficiary_of_Aapda_Sampoorti": "beneficiary_of_Aapda_Sampoorti",
    "Bihar disaster relief": "beneficiary_of_Aapda_Sampoorti",
    "Aapda Sampoorti scheme": "beneficiary_of_Aapda_Sampoorti",
    "rehabilitation beneficiaries": "beneficiary_of_Aapda_Sampoorti",
    "disaster assistance data": "beneficiary_of_Aapda_Sampoorti",
    "calamity relief records": "beneficiary_of_Aapda_Sampoorti",
    "village-wise aid recipients": "beneficiary_of_Aapda_Sampoorti",
    "emergency support scheme": "beneficiary_of_Aapda_Sampoorti",
    "Bihar disaster recovery": "beneficiary_of_Aapda_Sampoorti",
    "relief fund distribution": "beneficiary_of_Aapda_Sampoorti",

    "bihar_archaeological_sites_district_location_year_wise": "bihar_archaeological_sites_district_location_year_wise",
    "Bihar heritage sites": "bihar_archaeological_sites_district_location_year_wise",
    "historical monuments Bihar": "bihar_archaeological_sites_district_location_year_wise",
    "archaeology department records": "bihar_archaeological_sites_district_location_year_wise",
    "protected sites Bihar": "bihar_archaeological_sites_district_location_year_wise",
    "ancient site documentation": "bihar_archaeological_sites_district_location_year_wise",
    "cultural heritage locations": "bihar_archaeological_sites_district_location_year_wise",
    "Bihar historical places": "bihar_archaeological_sites_district_location_year_wise",
    "district-wise monuments": "bihar_archaeological_sites_district_location_year_wise",
    "archaeological survey data": "bihar_archaeological_sites_district_location_year_wise",

    "bihar_archaeology_and_museums_related_schemes_year_wise_budget": "bihar_archaeology_and_museums_related_schemes_year_wise_budget",
    "Bihar heritage budget": "bihar_archaeology_and_museums_related_schemes_year_wise_budget",
    "museum funding allocation": "bihar_archaeology_and_museums_related_schemes_year_wise_budget",
    "archaeology scheme finances": "bihar_archaeology_and_museums_related_schemes_year_wise_budget",
    "cultural preservation budget": "bihar_archaeology_and_museums_related_schemes_year_wise_budget",
    "museum development funds": "bihar_archaeology_and_museums_related_schemes_year_wise_budget",
    "Bihar culture budget": "bihar_archaeology_and_museums_related_schemes_year_wise_budget",
    "historical site funding": "bihar_archaeology_and_museums_related_schemes_year_wise_budget",
    "art conservation budget": "bihar_archaeology_and_museums_related_schemes_year_wise_budget",
    "government museum grants": "bihar_archaeology_and_museums_related_schemes_year_wise_budget",

    "bihar_climate_resilient_agriculture_data": "bihar_climate_resilient_agriculture_data",
    "Bihar climate agriculture": "bihar_climate_resilient_agriculture_data",
    "crop season production": "bihar_climate_resilient_agriculture_data",
    "agriculture target vs achievement": "bihar_climate_resilient_agriculture_data",
    "resilient farming stats": "bihar_climate_resilient_agriculture_data",
    "Kharif Rabi production": "bihar_climate_resilient_agriculture_data",
    "Bihar farming initiatives": "bihar_climate_resilient_agriculture_data",
    "climate-smart agriculture": "bihar_climate_resilient_agriculture_data",
    "district crop targets": "bihar_climate_resilient_agriculture_data",
    "agricultural performance metrics": "bihar_climate_resilient_agriculture_data",

    "bihar_dams_operational_information": "bihar_dams_operational_information",
    "Bihar dam specifications": "bihar_dams_operational_information",
    "reservoir capacity data": "bihar_dams_operational_information",
    "dam engineering details": "bihar_dams_operational_information",
    "water storage infrastructure": "bihar_dams_operational_information",
    "river dam records": "bihar_dams_operational_information",
    "Bihar water projects": "bihar_dams_operational_information",
    "dam safety parameters": "bihar_dams_operational_information",
    "hydrological structure data": "bihar_dams_operational_information",
    "irrigation dam metrics": "bihar_dams_operational_information",

    "bihar_district_wise_shooting_locations": "bihar_district_wise_shooting_locations",
    "Bihar film locations": "bihar_district_wise_shooting_locations",
    "movie shooting spots": "bihar_district_wise_shooting_locations",
    "photography sites Bihar": "bihar_district_wise_shooting_locations",
    "approved filming locations": "bihar_district_wise_shooting_locations",
    "cinematography venues": "bihar_district_wise_shooting_locations",
    "Bihar tourism filming": "bihar_district_wise_shooting_locations",
    "district shooting permits": "bihar_district_wise_shooting_locations",
    "cultural site filming": "bihar_district_wise_shooting_locations",
    "government approved shoots": "bihar_district_wise_shooting_locations",

    "bihar_electricity_board_operational_performance_year_wise": "bihar_electricity_board_operational_performance_year_wise",
    "BSEB performance metrics": "bihar_electricity_board_operational_performance_year_wise",
    "power generation stats": "bihar_electricity_board_operational_performance_year_wise",
    "electricity distribution data": "bihar_electricity_board_operational_performance_year_wise",
    "utility operational records": "bihar_electricity_board_operational_performance_year_wise",
    "Bihar power sector": "bihar_electricity_board_operational_performance_year_wise",
    "energy production Bihar": "bihar_electricity_board_operational_performance_year_wise",
    "electricity board KPIs": "bihar_electricity_board_operational_performance_year_wise",
    "power supply metrics": "bihar_electricity_board_operational_performance_year_wise",
    "BSEB annual report": "bihar_electricity_board_operational_performance_year_wise",

    "bihar_hall_art_gallery_reservation_details": "bihar_hall_art_gallery_reservation_details",
    "Bihar cultural venues": "bihar_hall_art_gallery_reservation_details",
    "art gallery bookings": "bihar_hall_art_gallery_reservation_details",
    "event space reservations": "bihar_hall_art_gallery_reservation_details",
    "government hall rental": "bihar_hall_art_gallery_reservation_details",
    "cultural facility fees": "bihar_hall_art_gallery_reservation_details",
    "Bihar exhibition spaces": "bihar_hall_art_gallery_reservation_details",
    "venue capacity details": "bihar_hall_art_gallery_reservation_details",
    "art department venues": "bihar_hall_art_gallery_reservation_details",
    "cultural event logistics": "bihar_hall_art_gallery_reservation_details",

    "bihar_irrigation_data": "bihar_irrigation_data",
    "Bihar water management": "bihar_irrigation_data",
    "irrigation season data": "bihar_irrigation_data",
    "Kharif Rabi irrigation": "bihar_irrigation_data",
    "agricultural water targets": "bihar_irrigation_data",
    "canal irrigation stats": "bihar_irrigation_data",
    "Bihar farming water": "bihar_irrigation_data",
    "irrigation department records": "bihar_irrigation_data",
    "water resource utilization": "bihar_irrigation_data",
    "historical irrigation trends": "bihar_irrigation_data",

    "bihar_monuments_district_wise_year_wise_details": "bihar_monuments_district_wise_year_wise_details",
    "Bihar protected monuments": "bihar_monuments_district_wise_year_wise_details",
    "ASI site records": "bihar_monuments_district_wise_year_wise_details",
    "historical site registry": "bihar_monuments_district_wise_year_wise_details",
    "yearly monument data": "bihar_monuments_district_wise_year_wise_details",
    "cultural heritage registry": "bihar_monuments_district_wise_year_wise_details",
    "Bihar ancient structures": "bihar_monuments_district_wise_year_wise_details",
    "government monument list": "bihar_monuments_district_wise_year_wise_details",
    "district heritage sites": "bihar_monuments_district_wise_year_wise_details",
    "protected structure database": "bihar_monuments_district_wise_year_wise_details",

    "bihar_museums_data_with_ownership_and_highlights": "bihar_museums_data_with_ownership_and_highlights",
    "Bihar museum directory": "bihar_museums_data_with_ownership_and_highlights",
    "cultural exhibits data": "bihar_museums_data_with_ownership_and_highlights",
    "museum ownership records": "bihar_museums_data_with_ownership_and_highlights",
    "art collection highlights": "bihar_museums_data_with_ownership_and_highlights",
    "Bihar gallery information": "bihar_museums_data_with_ownership_and_highlights",
    "museum establishment years": "bihar_museums_data_with_ownership_and_highlights",
    "government museum assets": "bihar_museums_data_with_ownership_and_highlights",
    "cultural repository data": "bihar_museums_data_with_ownership_and_highlights",
    "historical collection records": "bihar_museums_data_with_ownership_and_highlights",

    "bihar_state_disability_pension_district_wise_year_wise": "bihar_state_disability_pension_district_wise_year_wise",
    "Bihar disability benefits": "bihar_state_disability_pension_district_wise_year_wise",
    "e-labharti pension": "bihar_state_disability_pension_district_wise_year_wise",
    "village-wise disability aid": "bihar_state_disability_pension_district_wise_year_wise",
    "direct benefit transfer": "bihar_state_disability_pension_district_wise_year_wise",
    "handicapped pension scheme": "bihar_state_disability_pension_district_wise_year_wise",
    "Bihar social welfare": "bihar_state_disability_pension_district_wise_year_wise",
    "disability support payments": "bihar_state_disability_pension_district_wise_year_wise",
    "block-wise pensioners": "bihar_state_disability_pension_district_wise_year_wise",
    "government assistance records": "bihar_state_disability_pension_district_wise_year_wise",

    "bihar_state_disability_pension_progress_report": "bihar_state_disability_pension_progress_report",
    "pension application status": "bihar_state_disability_pension_progress_report",
    "disability scheme pendency": "bihar_state_disability_pension_progress_report",
    "Bihar approval rates": "bihar_state_disability_pension_progress_report",
    "verification process metrics": "bihar_state_disability_pension_progress_report",
    "DEO processing stats": "bihar_state_disability_pension_progress_report",
    "panchayat verification data": "bihar_state_disability_pension_progress_report",
    "error correction applications": "bihar_state_disability_pension_progress_report",
    "rejected pension cases": "bihar_state_disability_pension_progress_report",
    "disability scheme performance": "bihar_state_disability_pension_progress_report",

    "block_wise_panchayat_wise_damaged_crops": "block_wise_panchayat_wise_damaged_crops",
    "Bihar crop damage": "block_wise_panchayat_wise_damaged_crops",
    "agricultural loss records": "block_wise_panchayat_wise_damaged_crops",
    "revenue thana crop data": "block_wise_panchayat_wise_damaged_crops",
    "affected farmland area": "block_wise_panchayat_wise_damaged_crops",
    "panchayat-wise damage": "block_wise_panchayat_wise_damaged_crops",
    "Bihar farming losses": "block_wise_panchayat_wise_damaged_crops",
    "block-level crop failure": "block_wise_panchayat_wise_damaged_crops",
    "agriculture disaster data": "block_wise_panchayat_wise_damaged_crops",
    "acreage damage reports": "block_wise_panchayat_wise_damaged_crops",

    "blocks_ghats_kilns_mineral_wise": "blocks_ghats_kilns_mineral_wise",
    "Bihar mining operations": "blocks_ghats_kilns_mineral_wise",
    "mineral extraction sites": "blocks_ghats_kilns_mineral_wise",
    "sand mining records": "blocks_ghats_kilns_mineral_wise",
    "kiln distribution data": "blocks_ghats_kilns_mineral_wise",
    "river ghat mining": "blocks_ghats_kilns_mineral_wise",
    "minor minerals Bihar": "blocks_ghats_kilns_mineral_wise",
    "mining infrastructure stats": "blocks_ghats_kilns_mineral_wise",
    "district mineral resources": "blocks_ghats_kilns_mineral_wise",
    "Bihar quarry operations": "blocks_ghats_kilns_mineral_wise",

    "brick_kilns_district_wise": "brick_kilns_district_wise",
    "Bihar brick industry": "brick_kilns_district_wise",
    "clay kiln distribution": "brick_kilns_district_wise",
    "construction material production": "brick_kilns_district_wise",
    "district-wise kilns": "brick_kilns_district_wise",
    "brick manufacturing units": "brick_kilns_district_wise",
    "Bihar kiln census": "brick_kilns_district_wise",
    "building material stats": "brick_kilns_district_wise",
    "red brick production": "brick_kilns_district_wise",
    "clay product industry": "brick_kilns_district_wise",

    "building_construction_measurement_book_records_year_wise": "building_construction_measurement_book_records_year_wise",
    "Bihar construction records": "building_construction_measurement_book_records_year_wise",
    "measurement book entries": "building_construction_measurement_book_records_year_wise",
    "project work accounting": "building_construction_measurement_book_records_year_wise",
    "construction department logs": "building_construction_measurement_book_records_year_wise",
    "building project measurements": "building_construction_measurement_book_records_year_wise",
    "MB register data": "building_construction_measurement_book_records_year_wise",
    "government construction docs": "building_construction_measurement_book_records_year_wise",
    "infrastructure measurement": "building_construction_measurement_book_records_year_wise",
    "public works accounting": "building_construction_measurement_book_records_year_wise",

    "building_project_funding_records_departmentwise": "building_project_funding_records_departmentwise",
    "Bihar construction funding": "building_project_funding_records_departmentwise",
    "departmental building budgets": "building_project_funding_records_departmentwise",
    "infrastructure allocation": "building_project_funding_records_departmentwise",
    "government project finance": "building_project_funding_records_departmentwise",
    "approved vs allocated": "building_project_funding_records_departmentwise",
    "construction payment status": "building_project_funding_records_departmentwise",
    "public works funding": "building_project_funding_records_departmentwise",
    "department building projects": "building_project_funding_records_departmentwise",
    "Bihar infrastructure spend": "building_project_funding_records_departmentwise",

    "business_overview_of_vegfed_district_wise_year_wise": "business_overview_of_vegfed_district_wise_year_wise",
    "Bihar vegetable sales": "business_overview_of_vegfed_district_wise_year_wise",
    "VEGFED revenue": "business_overview_of_vegfed_district_wise_year_wise",
    "produce marketing data": "business_overview_of_vegfed_district_wise_year_wise",
    "agricultural sales metrics": "business_overview_of_vegfed_district_wise_year_wise",
    "vegetable distribution stats": "business_overview_of_vegfed_district_wise_year_wise",
    "Bihar agri-business": "business_overview_of_vegfed_district_wise_year_wise",
    "metric ton sales": "business_overview_of_vegfed_district_wise_year_wise",
    "farm produce revenue": "business_overview_of_vegfed_district_wise_year_wise",
    "VEGFED performance": "business_overview_of_vegfed_district_wise_year_wise",
    
    # Call Center Raids and Arrests
    "call center": "call_center_based_raids_arrests_district_wise_year_wise",
    "prohibition": "call_center_based_raids_arrests_district_wise_year_wise",
    "excise": "call_center_based_raids_arrests_district_wise_year_wise",
    "raids": "call_center_based_raids_arrests_district_wise_year_wise",
    "arrests": "call_center_based_raids_arrests_district_wise_year_wise",
    "complaints": "call_center_based_raids_arrests_district_wise_year_wise",
    
    # Cattle Breed Population
    "cattle": "cattle_breed_population_district_wise_in_bihar",
    "livestock": "cattle_breed_population_district_wise_in_bihar",
    "breed": "cattle_breed_population_district_wise_in_bihar",
    "bachaur": "cattle_breed_population_district_wise_in_bihar",
    "hairana": "cattle_breed_population_district_wise_in_bihar",
    "holstein": "cattle_breed_population_district_wise_in_bihar",
    "murrah": "cattle_breed_population_district_wise_in_bihar",
    "sahiwal": "cattle_breed_population_district_wise_in_bihar",
    "surti": "cattle_breed_population_district_wise_in_bihar",
    
    # Cattle Milk Production
    "milk": "cattle_milk_production_district_wise_bihar",
    "dairy": "cattle_milk_production_district_wise_bihar",
    "bovine": "cattle_milk_production_district_wise_bihar",
    "buffalo": "cattle_milk_production_district_wise_bihar",
    "crossbreed": "cattle_milk_production_district_wise_bihar",
    "indigenous": "cattle_milk_production_district_wise_bihar",
    
    # Census 2011 Industrial Category (Age-wise)
    "main workers": "census_2011_industrial_category_main_workers_age_wise_details",
    "age group workers": "census_2011_industrial_category_main_workers_age_wise_details",
    "cultivators": "census_2011_industrial_category_main_workers_age_wise_details",
    "agricultural laborers": "census_2011_industrial_category_main_workers_age_wise_details",
    "mining": "census_2011_industrial_category_main_workers_age_wise_details",
    "manufacturing": "census_2011_industrial_category_main_workers_age_wise_details",
    "construction": "census_2011_industrial_category_main_workers_age_wise_details",
    "trade": "census_2011_industrial_category_main_workers_age_wise_details",
    "transportation": "census_2011_industrial_category_main_workers_age_wise_details",
    
    # Census 2011 Industrial Category (Education-wise)
    "literate workers": "census_2011_industrial_category_main_workers_educational_wise",
    "illiterate workers": "census_2011_industrial_category_main_workers_educational_wise",
    "education workers": "census_2011_industrial_category_main_workers_educational_wise",
    
    # Census 2011 Marginal Workers
    "marginal workers": "census_2011_industrial_category_marginal_workers_age_wise",
    "seasonal workers": "census_2011_industrial_category_marginal_workers_age_wise",
    "part-time workers": "census_2011_industrial_category_marginal_workers_age_wise",
    
    # Census 2011 Literacy
    "literacy": "census_2011_literacy_district_wise_age_wise",
    "illiterate": "census_2011_literacy_district_wise_age_wise",
    "literate": "census_2011_literacy_district_wise_age_wise",
    "education": "census_2011_literacy_district_wise_age_wise",
    
    # Census 2011 Mother Tongue
    "language": "census_2011_population_state_wise_by_mother_tongue",
    "mother tongue": "census_2011_population_state_wise_by_mother_tongue",
    "linguistic": "census_2011_population_state_wise_by_mother_tongue",
    
    # Census 2011 Religion
    "religion": "census_2011_religion_wise_population",
    "hindu": "census_2011_religion_wise_population",
    "muslim": "census_2011_religion_wise_population",
    "christian": "census_2011_religion_wise_population",
    "sikh": "census_2011_religion_wise_population",
    "buddhist": "census_2011_religion_wise_population",
    "jain": "census_2011_religion_wise_population",
    
    # Census 2011 Villages and Towns Population
    "village population": "census_2011_villages_towns_population_above_below_five_thousand",
    "town population": "census_2011_villages_towns_population_above_below_five_thousand",
    "rural population": "census_2011_villages_towns_population_above_below_five_thousand",
    "urban population": "census_2011_villages_towns_population_above_below_five_thousand",
    
    # Census 2011 Population Area
    "population density": "census_2011_villages_towns_population_area_state_wise",
    "households": "census_2011_villages_towns_population_area_state_wise",
    "inhabited villages": "census_2011_villages_towns_population_area_state_wise",
    "area": "census_2011_villages_towns_population_area_state_wise",
    
    # Census 2011 Village Population Size
    "village size": "census_2011_villages_wise_population_size_and_class",
    "population class": "census_2011_villages_wise_population_size_and_class",
    "village classification": "census_2011_villages_wise_population_size_and_class",
    
    # Census 2011 Employment Industry-wise
    "industry": "census_india_2011_employment_statewise_industry_wise",
    "employment": "census_india_2011_employment_statewise_industry_wise",
    "industrial classification": "census_india_2011_employment_statewise_industry_wise",
    "workforce": "census_india_2011_employment_statewise_industry_wise",
    
    # Census 2011 Marital Status
    "marital status": "census_india_2011_marital_status_state_wise",
    "married": "census_india_2011_marital_status_state_wise",
    "widowed": "census_india_2011_marital_status_state_wise",
    "divorced": "census_india_2011_marital_status_state_wise",
    "never married": "census_india_2011_marital_status_state_wise",


    # Census 2011 Occupation Classification
    "occupation": "census_india_2011_occupation_classification_statewise",
    "employment type": "census_india_2011_occupation_classification_statewise",
    "employers": "census_india_2011_occupation_classification_statewise",
    "employees": "census_india_2011_occupation_classification_statewise",
    "single workers": "census_india_2011_occupation_classification_statewise",
    "NCO": "census_india_2011_occupation_classification_statewise",
    
    # Census 2011 Workforce
    "workforce": "census_india_2011_workforce_statewise",
    "labor force": "census_india_2011_workforce_statewise",
    "main workers": "census_india_2011_workforce_statewise",
    "marginal workers": "census_india_2011_workforce_statewise",
    "non-working": "census_india_2011_workforce_statewise",
    "job seekers": "census_india_2011_workforce_statewise",
    
    # Financial Accounting Trainees
    "BS-CFA": "certificate_financial_accounting_trainees_district_wise",
    "accounting trainees": "certificate_financial_accounting_trainees_district_wise",
    "skill development": "certificate_financial_accounting_trainees_district_wise",
    "training centers": "certificate_financial_accounting_trainees_district_wise",
    
    # Checkpost Arrests and Seizures
    "checkpost": "checkpost_arrests_seized_liquor_seized_vehicles_district_wise",
    "liquor seizure": "checkpost_arrests_seized_liquor_seized_vehicles_district_wise",
    "vehicle seizure": "checkpost_arrests_seized_liquor_seized_vehicles_district_wise",
    "excise enforcement": "checkpost_arrests_seized_liquor_seized_vehicles_district_wise",
    
    # Aanganwadi Children
    "Aanganwadi": "children_details_year_wise_district_wise_aangan_mandey",
    "child care": "children_details_year_wise_district_wise_aangan_mandey",
    "registered children": "children_details_year_wise_district_wise_aangan_mandey",
    "ICDS": "children_details_year_wise_district_wise_aangan_mandey",
    
    # Civil Seva Protsahan Yojana
    "SC/ST": "civil_seva_protsahan_yojana_scst",
    "scheduled caste": "civil_seva_protsahan_yojana_scst",
    "scheduled tribe": "civil_seva_protsahan_yojana_scst",
    "beneficiaries": "civil_seva_protsahan_yojana_scst",
    "welfare scheme": "civil_seva_protsahan_yojana_scst",
    
    # Commercial Taxes - GST Collection
    "GST": "commercial_taxes_department_collection_state_wise_year_wise",
    "tax revenue": "commercial_taxes_department_collection_state_wise_year_wise",
    "CGST": "commercial_taxes_department_collection_state_wise_year_wise",
    "SGST": "commercial_taxes_department_collection_state_wise_year_wise",
    "IGST": "commercial_taxes_department_collection_state_wise_year_wise",
    "CESS": "commercial_taxes_department_collection_state_wise_year_wise",
    
    # Commercial Taxes - Refunds
    "tax refunds": "commercial_taxes_department_refund_state_wise_year_wise",
    "GST refund": "commercial_taxes_department_refund_state_wise_year_wise",
    
    # IGST Settlement
    "IGST settlement": "commercial_taxes_igst_settlement_state_yearwise",
    "regular settlement": "commercial_taxes_igst_settlement_state_yearwise",
    "adhoc settlement": "commercial_taxes_igst_settlement_state_yearwise",
    
    # Consolidated Raids Report
    "excise raids": "consolidated_raids_report_excise_and_police_year_wise",
    "police raids": "consolidated_raids_report_excise_and_police_year_wise",
    "liquor destruction": "consolidated_raids_report_excise_and_police_year_wise",
    "countrymade liquor": "consolidated_raids_report_excise_and_police_year_wise",
    "foreign liquor": "consolidated_raids_report_excise_and_police_year_wise",
    
    # Bridge Construction
    "bridges": "construction_of_bridges_year_wise",
    "infrastructure": "construction_of_bridges_year_wise",
    "work turnover": "construction_of_bridges_year_wise",
    "construction profit": "construction_of_bridges_year_wise",
    
    # Fertilizer Consumption
    "NPK": "consumption_npk_fertilizer_year_wise",
    "fertilizer": "consumption_npk_fertilizer_year_wise",
    "agriculture input": "consumption_npk_fertilizer_year_wise",
    
    # Course Certificates
    "BIPARD": "course_certificate_details",
    "training certificates": "course_certificate_details",
    "public administration": "course_certificate_details",
    "rural development": "course_certificate_details",
    
    # Crimes Against SC/ST
    "atrocities": "crime_against_sc_st_yearwise",
    "SC/ST crimes": "crime_against_sc_st_yearwise",
    "registered cases": "crime_against_sc_st_yearwise",
    "victims": "crime_against_sc_st_yearwise",
    
    # Crop Data
    "crop production": "crop_area_production_yield_seasonwise_year_and_district_in_bihar",
    "yield": "crop_area_production_yield_seasonwise_year_and_district_in_bihar",
    "Kharif": "crop_area_production_yield_seasonwise_year_and_district_in_bihar",
    "Rabi": "crop_area_production_yield_seasonwise_year_and_district_in_bihar",
    "hectares": "crop_area_production_yield_seasonwise_year_and_district_in_bihar",
    
    # Crop Prices
    "crop prices": "crop_price_yearwise_varietywise_in_Bihar_per_kg",
    "price per kg": "crop_price_yearwise_varietywise_in_Bihar_per_kg",
    "crop varieties": "crop_price_yearwise_varietywise_in_Bihar_per_kg",
    
    # IT Skill Development (District-wise)
    "IT training": "department_of_it_skill_development_trainees_district_wise",
    "data centers": "department_of_it_skill_development_trainees_district_wise",
    "enrollment": "department_of_it_skill_development_trainees_district_wise",
    "placement": "department_of_it_skill_development_trainees_district_wise",
    
    # IT Skill Development (Job Role-wise)
    "IT-ITES": "department_of_it_skill_development_trainees_sector_job_role_wise",
    "electronics": "department_of_it_skill_development_trainees_sector_job_role_wise",
    "job roles": "department_of_it_skill_development_trainees_sector_job_role_wise",
    "data entry": "department_of_it_skill_development_trainees_sector_job_role_wise",
    
    # IT Skill Development (Year-wise)
    "training batches": "department_of_it_skill_development_trainees_year_wise",
    "certified candidates": "department_of_it_skill_development_trainees_year_wise",
    
    # Departmental Budget
    "budget requests": "departmental_budget_requests_year_wise",
    "allocations": "departmental_budget_requests_year_wise",
    "requisitions": "departmental_budget_requests_year_wise",
    "building construction": "departmental_budget_requests_year_wise",
    
    # Diesel Subsidy
    "diesel subsidy": "diesel_subsidy_district_wise_data_bihar",
    "agriculture subsidy": "diesel_subsidy_district_wise_data_bihar",
    "DAO approval": "diesel_subsidy_district_wise_data_bihar",
    
    # Irrigation
    "irrigation": "district_wise_Irrigation_area",
    "canals": "district_wise_Irrigation_area",
    "tubewells": "district_wise_Irrigation_area",
    "ponds": "district_wise_Irrigation_area",
    "hectares irrigated": "district_wise_Irrigation_area",
    
    # District Amenities
    "amenities": "district_wise_amenities",
    "electricity access": "district_wise_amenities",
    "drinking water": "district_wise_amenities",
    "sanitation": "district_wise_amenities",
    "LGD code": "district_wise_amenities",
    
    # ASHA Workers
    "ASHA": "district_wise_asha_health_workers",
    "health workers": "district_wise_asha_health_workers",
    "Ashwin scheme": "district_wise_asha_health_workers",
    "community health": "district_wise_asha_health_workers",
    
    # BharatNet
    "BharatNet": "district_wise_bharat_net_scheme",
    "broadband": "district_wise_bharat_net_scheme",
    "village connectivity": "district_wise_bharat_net_scheme",
    "digital India": "district_wise_bharat_net_scheme",
    
    # Common Service Centers
    "CSC": "district_wise_common_services_centre",
    "e-governance": "district_wise_common_services_centre",
    "digital services": "district_wise_common_services_centre",
    "rural connectivity": "district_wise_common_services_centre",

     # Craftsmen Training Scheme (CTS) and ITIs
    "CTS": "district_wise_craftsmen_training_scheme_CTS_ITI",
    "ITI": "district_wise_craftsmen_training_scheme_CTS_ITI",
    "industrial training": "district_wise_craftsmen_training_scheme_CTS_ITI",
    "vocational training": "district_wise_craftsmen_training_scheme_CTS_ITI",
    "trainee admissions": "district_wise_craftsmen_training_scheme_CTS_ITI",
    "women ITI": "district_wise_craftsmen_training_scheme_CTS_ITI",
    "new-age courses": "district_wise_craftsmen_training_scheme_CTS_ITI",
    
    # Engineering and Polytechnic Colleges
    "engineering colleges": "district_wise_engineering_and_polytechinc_colleges_seat",
    "polytechnic": "district_wise_engineering_and_polytechinc_colleges_seat",
    "technical education": "district_wise_engineering_and_polytechinc_colleges_seat",
    "college seats": "district_wise_engineering_and_polytechinc_colleges_seat",
    "institute capacity": "district_wise_engineering_and_polytechinc_colleges_seat",
    
    # FCA/FPO/PACS
    "FPO": "district_wise_fca_fpo_pacs",
    "FCA": "district_wise_fca_fpo_pacs",
    "PACS": "district_wise_fca_fpo_pacs",
    "farmer organizations": "district_wise_fca_fpo_pacs",
    "ODF+": "district_wise_fca_fpo_pacs",
    "open defecation free": "district_wise_fca_fpo_pacs",
    "agriculture cooperatives": "district_wise_fca_fpo_pacs",
    
    # Government Schools
    "government schools": "district_wise_government_schools_2022_23_bihar",
    "elementary schools": "district_wise_government_schools_2022_23_bihar",
    "secondary schools": "district_wise_government_schools_2022_23_bihar",
    "higher secondary": "district_wise_government_schools_2022_23_bihar",
    
    # Healthcare
    "healthcare": "district_wise_healthcare",
    "sub-centres": "district_wise_healthcare",
    "PHC": "district_wise_healthcare",
    "Ayushman Bharat": "district_wise_healthcare",
    "hospital admissions": "district_wise_healthcare",
    "health infrastructure": "district_wise_healthcare",
    
    # Household Amenities
    "tap water": "district_wise_households_amenities",
    "clean fuel": "district_wise_households_amenities",
    "LPG": "district_wise_households_amenities",
    "water connection": "district_wise_households_amenities",
    "household facilities": "district_wise_households_amenities",
    
    # Irrigation
    "groundwater": "district_wise_irrigation",
    "drip irrigation": "district_wise_irrigation",
    "sprinkler": "district_wise_irrigation",
    "water extraction": "district_wise_irrigation",
    "irrigation methods": "district_wise_irrigation",
    
    # School Categories
    "primary schools": "district_wise_school_category",
    "upper primary": "district_wise_school_category",
    "junior college": "district_wise_school_category",
    "school levels": "district_wise_school_category",
    "education stages": "district_wise_school_category",
    
    # School Location
    "urban schools": "district_wise_school_location",
    "rural schools": "district_wise_school_location",
    "school geography": "district_wise_school_location",
    "school distribution": "district_wise_school_location",
    
    # School Recognition
    "school recognition": "district_wise_school_recognition",
    "pre-primary": "district_wise_school_recognition",
    "recognized schools": "district_wise_school_recognition",
    "unrecognized": "district_wise_school_recognition",
    
    # School Special Facilities
    "special needs": "district_wise_school_special_facilities",
    "CWSN": "district_wise_school_special_facilities",
    "shift schools": "district_wise_school_special_facilities",
    "residential schools": "district_wise_school_special_facilities",
    "boarding schools": "district_wise_school_special_facilities",
    
    # School Streams
    "arts stream": "district_wise_school_streams",
    "science stream": "district_wise_school_streams",
    "commerce": "district_wise_school_streams",
    "vocational": "district_wise_school_streams",
    "school subjects": "district_wise_school_streams",
    
    # School Types
    "co-ed": "district_wise_school_type",
    "girls schools": "district_wise_school_type",
    "boys schools": "district_wise_school_type",
    "school gender": "district_wise_school_type",
    
    # Sown Area
    "agriculture area": "district_wise_sown_area",
    "sown area": "district_wise_sown_area",
    "crop insurance": "district_wise_sown_area",
    "land use": "district_wise_sown_area",
    
    # Startups
    "startups": "district_wise_start_up_bihar",
    "SMIC": "district_wise_start_up_bihar",
    "seed funding": "district_wise_start_up_bihar",
    "entrepreneurship": "district_wise_start_up_bihar",
    
    # Student Dropout
    "dropout rates": "district_wise_student_dropout",
    "primary dropout": "district_wise_student_dropout",
    "secondary dropout": "district_wise_student_dropout",
    "education retention": "district_wise_student_dropout",
    
    # Subject Proficiency
    "student performance": "district_wise_subject_proficiency",
    "learning outcomes": "district_wise_subject_proficiency",
    "basic proficiency": "district_wise_subject_proficiency",
    "EVS": "district_wise_subject_proficiency",
    "mathematics scores": "district_wise_subject_proficiency",
    
    # School Management
    "school types": "district_wise_type_of_school_management_2023_24",
    "private schools": "district_wise_type_of_school_management_2023_24",
    "government schools": "district_wise_type_of_school_management_2023_24",
    "madrasas": "district_wise_type_of_school_management_2023_24",
    "Sanskrit schools": "district_wise_type_of_school_management_2023_24",
    
    # Drone Arrests
    "drone raids": "drone_arrests_and_seizures_district_wise_year_wise",
    "liquor seizures": "drone_arrests_and_seizures_district_wise_year_wise",
    "vehicle seizures": "drone_arrests_and_seizures_district_wise_year_wise",
    "excise enforcement": "drone_arrests_and_seizures_district_wise_year_wise",
    "java jaggery": "drone_arrests_and_seizures_district_wise_year_wise",
    
    # Educational Schemes
    "UDISE": "educational_schemes_under_udise_year_wise",
    "education schemes": "educational_schemes_under_udise_year_wise",
    "scholarships": "educational_schemes_under_udise_year_wise",
    "education benefits": "educational_schemes_under_udise_year_wise",
    "fund transfer": "educational_schemes_under_udise_year_wise",

    # e-Labharti Pension Schemes
    "e-Labharti": "elabharthi_beneficiaries_scheme_wise",
    "pension schemes": "elabharthi_beneficiaries_scheme_wise",
    "MVPY": "elabharthi_beneficiaries_scheme_wise",
    "disabled pension": "elabharthi_beneficiaries_scheme_wise",
    "old age pension": "elabharthi_beneficiaries_scheme_wise",
    "pension disbursement": "elabharthi_beneficiaries_scheme_wise",
    
    # e-Labharti Pension Categories
    "pension categories": "elabharthi_pension_beneficiaries_category_wise",
    "BC pension": "elabharthi_pension_beneficiaries_category_wise",
    "EBC pension": "elabharthi_pension_beneficiaries_category_wise",
    "SC/ST pension": "elabharthi_pension_beneficiaries_category_wise",
    "minority pension": "elabharthi_pension_beneficiaries_category_wise",
    
    # Electricity Board Financials
    "electricity finances": "electricity_board_financial_performance_transaction_year_wise",
    "power sector finances": "electricity_board_financial_performance_transaction_year_wise",
    "electricity revenue": "electricity_board_financial_performance_transaction_year_wise",
    "power subsidies": "electricity_board_financial_performance_transaction_year_wise",
    "electricity expenditure": "electricity_board_financial_performance_transaction_year_wise",
    
    # Engineering College Admissions
    "engineering admissions": "engineering_college_students_district_branch_year_wise",
    "lateral entry": "engineering_college_students_district_branch_year_wise",
    "engineering branches": "engineering_college_students_district_branch_year_wise",
    "technical admissions": "engineering_college_students_district_branch_year_wise",
    
    # Engineering Faculty
    "engineering faculty": "engineering_polytechnic_faculty_strength_post_wise_branch_wise",
    "polytechnic faculty": "engineering_polytechnic_faculty_strength_post_wise_branch_wise",
    "teaching staff": "engineering_polytechnic_faculty_strength_post_wise_branch_wise",
    "professor count": "engineering_polytechnic_faculty_strength_post_wise_branch_wise",
    
    # Student Enrollment
    "school enrollment": "enrollment_of_students_category_wise_year_wise",
    "class-wise enrollment": "enrollment_of_students_category_wise_year_wise",
    "gender enrollment": "enrollment_of_students_category_wise_year_wise",
    "pre-primary enrollment": "enrollment_of_students_category_wise_year_wise",
    
    # Crop Irrigation
    "irrigation duty": "expected_area_of_crop_irrigation_yearwise",
    "crop water requirement": "expected_area_of_crop_irrigation_yearwise",
    "Kharif irrigation": "expected_area_of_crop_irrigation_yearwise",
    "Rabi irrigation": "expected_area_of_crop_irrigation_yearwise",
    
    # BIPARD Faculty
    "BIPARD courses": "faculty_attendees_course_wise_details",
    "training faculty": "faculty_attendees_course_wise_details",
    "public administration training": "faculty_attendees_course_wise_details",
    
    # Faculty Feedback
    "faculty evaluation": "faculty_feedback_course_wise_details",
    "teaching feedback": "faculty_feedback_course_wise_details",
    "instructor ratings": "faculty_feedback_course_wise_details",
    
    # VEGFED Scheme
    "VEGFED": "farmers_under_vegfed_scheme_block_wise_category_wise",
    "farmer registration": "farmers_under_vegfed_scheme_block_wise_category_wise",
    "agriculture scheme": "farmers_under_vegfed_scheme_block_wise_category_wise",
    
    # Fertilizer Consumption
    "fertilizer use": "fertilizer_consumption_year_wise",
    "urea consumption": "fertilizer_consumption_year_wise",
    "DAP": "fertilizer_consumption_year_wise",
    "MOP": "fertilizer_consumption_year_wise",
    "fertilizer per hectare": "fertilizer_consumption_year_wise",
    
    # Fisheries
    "fisheries data": "fisheries_water_bodies_district_wise_year_wise",
    "water bodies": "fisheries_water_bodies_district_wise_year_wise",
    "fish farms": "fisheries_water_bodies_district_wise_year_wise",
    
    # Flood Preparedness (Block)
    "flood preparedness": "flood_preparedness_scorecard_block_wise_district_wise",
    "disaster management": "flood_preparedness_scorecard_block_wise_district_wise",
    "rescue boats": "flood_preparedness_scorecard_block_wise_district_wise",
    "flood shelters": "flood_preparedness_scorecard_block_wise_district_wise",
    
    # Flood Preparedness (District)
    "district flood": "flood_preparedness_scorecard_district_wise",
    "NDRF": "flood_preparedness_scorecard_district_wise",
    "flood equipment": "flood_preparedness_scorecard_district_wise",
    "polythene sheets": "flood_preparedness_scorecard_district_wise",
    
    # Drug Seizures
    "drug enforcement": "ganja_bhang_seized_arrests_made_district_wise_year_wise",
    "narcotics": "ganja_bhang_seized_arrests_made_district_wise_year_wise",
    "ganja seizures": "ganja_bhang_seized_arrests_made_district_wise_year_wise",
    "charas": "ganja_bhang_seized_arrests_made_district_wise_year_wise",
    
    # PMAY Gaps
    "PMAY targets": "gap_in_entry_target_pmay_scheme",
    "housing scheme": "gap_in_entry_target_pmay_scheme",
    "Awas Yojana": "gap_in_entry_target_pmay_scheme",
    
    # Gramin Tola Scheme
    "rural roads": "gramin_tola_sampark_nischay_yojana_targets_and_achievements",
    "all-weather roads": "gramin_tola_sampark_nischay_yojana_targets_and_achievements",
    "road connectivity": "gramin_tola_sampark_nischay_yojana_targets_and_achievements",
    
    # Electricity Consumption
    "per capita electricity": "growth_in_per_capita_electricity_year_wise",
    "power consumption": "growth_in_per_capita_electricity_year_wise",
    "energy use": "growth_in_per_capita_electricity_year_wise",
    
    # Electricity Consumers
    "power consumers": "growth_of_electricity_consumers_year_wise",
    "electricity connections": "growth_of_electricity_consumers_year_wise",
    
    # Handpumps
    "handpumps": "handpumps_in_bihar_year_wise_district_wise_division_wise",
    "geotagged handpumps": "handpumps_in_bihar_year_wise_district_wise_division_wise",
    "water pumps": "handpumps_in_bihar_year_wise_district_wise_division_wise",
    "India Mark": "handpumps_in_bihar_year_wise_district_wise_division_wise",
    
    # Har Ghar Nal
    "tap water scheme": "har_ghar_nal_ka_jal_district_wise_block_wise_year_wise",
    "water supply": "har_ghar_nal_ka_jal_district_wise_block_wise_year_wise",
    "Jal Jeevan": "har_ghar_nal_ka_jal_district_wise_block_wise_year_wise",
    
    # Government Hierarchy
    "officer hierarchy": "hierarchy_division_designation_officers",
    "government structure": "hierarchy_division_designation_officers",
    "bureaucracy": "hierarchy_division_designation_officers",
    
    # Highways
    "road network": "highways_major_district_roads_year_wise_district_wise",
    "NH": "highways_major_district_roads_year_wise_district_wise",
    "SH": "highways_major_district_roads_year_wise_district_wise",
    "MDR": "highways_major_district_roads_year_wise_district_wise",
    
    # Hostel Grants (District)
    "hostel scheme": "hostel_grant_scheme_ec_ebc_beneficiary_details_district_wise",
    "EBC hostel": "hostel_grant_scheme_ec_ebc_beneficiary_details_district_wise",
    "student grants": "hostel_grant_scheme_ec_ebc_beneficiary_details_district_wise",
    
    # Hostel Grants (Block)
    "hostel students": "hostel_grant_scheme_ec_ebc_gender_wise_details_block_wise",
    "BC hostel": "hostel_grant_scheme_ec_ebc_gender_wise_details_block_wise",
    "hostel demographics": "hostel_grant_scheme_ec_ebc_gender_wise_details_block_wise",
    
    # PMAY Completion
    "PMAY completion": "house_completion_year_wise_pmay_scheme",
    "houses built": "house_completion_year_wise_pmay_scheme",
    "housing completion": "house_completion_year_wise_pmay_scheme",

     # PMAY House Progress
    "PMAY progress": "house_progress_in_pmay_scheme",
    "housing installments": "house_progress_in_pmay_scheme",
    "geo-tagged sanctions": "house_progress_in_pmay_scheme",
    "verified accounts": "house_progress_in_pmay_scheme",
    "house completion": "house_progress_in_pmay_scheme",
    
    # Indira Gandhi Disability Pension (District)
    "disability pension": "indira_gandhi_disability_pension_district_wise_year_wise",
    "IGNDP": "indira_gandhi_disability_pension_district_wise_year_wise",
    "pension disbursement": "indira_gandhi_disability_pension_district_wise_year_wise",
    "benefit transfer": "indira_gandhi_disability_pension_district_wise_year_wise",
    
    # Indira Gandhi Disability Pension Progress
    "pension applications": "indira_gandhi_national_disability_pension_progress_report",
    "pending verification": "indira_gandhi_national_disability_pension_progress_report",
    "approved pensions": "indira_gandhi_national_disability_pension_progress_report",
    "rejected applications": "indira_gandhi_national_disability_pension_progress_report",
    
    # Indira Gandhi Old Age Pension
    "old age pension": "indira_gandhi_national_old_age_pension_progress_report",
    "IGNOAP": "indira_gandhi_national_old_age_pension_progress_report",
    "pension approval": "indira_gandhi_national_old_age_pension_progress_report",
    "DEOC pending": "indira_gandhi_national_old_age_pension_progress_report",
    
    # Indira Gandhi Widow Pension Progress
    "widow pension": "indira_gandhi_national_widow_pension_progress_report",
    "IGNWP": "indira_gandhi_national_widow_pension_progress_report",
    "widow applications": "indira_gandhi_national_widow_pension_progress_report",
    "assistant director pending": "indira_gandhi_national_widow_pension_progress_report",
    
    # Indira Gandhi Widow Pension (District)
    "widow benefit": "indira_gandhi_widow_pension_district_wise_year_wise",
    "pension transactions": "indira_gandhi_widow_pension_district_wise_year_wise",
    
    # Industrial Employment
    "sector employment": "industrial_employment_sector_wise_year_wise",
    "industrial jobs": "industrial_employment_sector_wise_year_wise",
    "employment data": "industrial_employment_sector_wise_year_wise",
    
    # Industrial Investment
    "sector investment": "industrial_investment_sector_wise_year_wise",
    "capital invested": "industrial_investment_sector_wise_year_wise",
    "industrial growth": "industrial_investment_sector_wise_year_wise",
    
    # Industries Applications
    "industry licenses": "industries_application_department_wise",
    "license approval": "industries_application_department_wise",
    "application processing": "industries_application_department_wise",
    "business permits": "industries_application_department_wise",
    
    # Irrigation Schemes (Block)
    "irrigation projects": "irrigation_scheme_block_wise_district_wise_year_wise",
    "scheme funding": "irrigation_scheme_block_wise_district_wise_year_wise",
    "tender status": "irrigation_scheme_block_wise_district_wise_year_wise",
    "work progress": "irrigation_scheme_block_wise_district_wise_year_wise",
    
    # Irrigation Schemes (Bihar 2022)
    "command area": "irrigation_schemes_bihar_2022_culturable_command_area_data",
    "irrigation potential": "irrigation_schemes_bihar_2022_culturable_command_area_data",
    "UIP": "irrigation_schemes_bihar_2022_culturable_command_area_data",
    "IPU": "irrigation_schemes_bihar_2022_culturable_command_area_data",
    
    # Jamabandi Land Records
    "land records": "jamabandi_land_record_circle_wise",
    "jamabandi": "jamabandi_land_record_circle_wise",
    "land tax": "jamabandi_land_record_circle_wise",
    "mauja records": "jamabandi_land_record_circle_wise",
    
    # Jeevika Groups
    "SHGs": "jeevika_groups_and_linkage_amount_yearwise",
    "self-help groups": "jeevika_groups_and_linkage_amount_yearwise",
    "credit linkage": "jeevika_groups_and_linkage_amount_yearwise",
    "village organizations": "jeevika_groups_and_linkage_amount_yearwise",
    "CLFs": "jeevika_groups_and_linkage_amount_yearwise",
    
    # Khatian Land Registration
    "khatian": "khatian_land_registration_details",
    "plot registration": "khatian_land_registration_details",
    "land registration": "khatian_land_registration_details",
    
    # Labour Resources Learners
    "skill development": "labour_resources_learner_details_year_district_gender_wise",
    "Kushal Yuva": "labour_resources_learner_details_year_district_gender_wise",
    "training centers": "labour_resources_learner_details_year_district_gender_wise",
    "vocational training": "labour_resources_learner_details_year_district_gender_wise",
    
    # Land Deed Registration
    "deed registration": "land_deed_registration_data",
    "property registration": "land_deed_registration_data",
    
    # Land Holdings
    "agricultural land": "land_holdings_in_bihar_for_agriculture",
    "land holding size": "land_holdings_in_bihar_for_agriculture",
    "marginal farmers": "land_holdings_in_bihar_for_agriculture",
    "large holdings": "land_holdings_in_bihar_for_agriculture",
    
    # Land Utilization
    "land use": "land_utilization_yearwise",
    "fallow land": "land_utilization_yearwise",
    "culturable waste": "land_utilization_yearwise",
    "net sown area": "land_utilization_yearwise",
    
    # Laxmi Bai Pension
    "Laxmi Bai pension": "laxmi_bai_social_security_pension_district_wise_year_wise",
    "social security": "laxmi_bai_social_security_pension_district_wise_year_wise",
    
    # MGNREGA
    "MGNREGA": "manrega_yearwise_all_over_india_details",
    "NREGA": "manrega_yearwise_all_over_india_details",
    "rural employment": "manrega_yearwise_all_over_india_details",
    "job cards": "manrega_yearwise_all_over_india_details",
    "persondays": "manrega_yearwise_all_over_india_details",
    
    # Mid-Day Meal
    "mid-day meal": "mid_day_meal_distribution_district_wise_year_wise",
    "school meals": "mid_day_meal_distribution_district_wise_year_wise",
    "fortified rice": "mid_day_meal_distribution_district_wise_year_wise",
    "food distribution": "mid_day_meal_distribution_district_wise_year_wise",
    
    # Milk Particulars
    "dairy cooperatives": "milk_particulars_year_wise",
    "milk procurement": "milk_particulars_year_wise",
    "DCS": "milk_particulars_year_wise",
    "milk marketing": "milk_particulars_year_wise",
    
    # Milk Price & Composition
    "milk fat": "milk_price_and_composition",
    "SNF": "milk_price_and_composition",
    "buffalo milk": "milk_price_and_composition",
    "cow milk": "milk_price_and_composition",
    
    # Motorboat Raids
    "motorboat raids": "motorboat_based_arrests_seized_liquor_district_wise_year_wise",
    "liquor enforcement": "motorboat_based_arrests_seized_liquor_district_wise_year_wise",
    "Java Mahua": "motorboat_based_arrests_seized_liquor_district_wise_year_wise",

    # Mukhya Mantri Gram Sampark Yojana
    "MMGSY": "mukhya_mantri_gram_sampark_yojana_targets_and_achievements",
    "rural road connectivity": "mukhya_mantri_gram_sampark_yojana_targets_and_achievements",
    "habitation roads": "mukhya_mantri_gram_sampark_yojana_targets_and_achievements",
    "road targets": "mukhya_mantri_gram_sampark_yojana_targets_and_achievements",
    
    # Mukhyamantri Kanya Utthaan (Intermediate)
    "MKUY intermediate": "mukhyamantri_kanya_utthaan_intermediate_beneficiaries",
    "girl education": "mukhyamantri_kanya_utthaan_intermediate_beneficiaries",
    "intermediate scholarships": "mukhyamantri_kanya_utthaan_intermediate_beneficiaries",
    
    # Mukhyamantri Kanya Utthaan (Snatak)
    "MKUY snatak": "mukhyamantri_kanya_utthaan_snatak_beneficiaries",
    "higher education scholarships": "mukhyamantri_kanya_utthaan_snatak_beneficiaries",
    "women graduates": "mukhyamantri_kanya_utthaan_snatak_beneficiaries",
    
    # Mukhyamantri Peyjal Nishchay Yojana
    "urban water supply": "mukhyamantri_peyjal_nishchay_yojana_year_wise",
    "drinking water scheme": "mukhyamantri_peyjal_nishchay_yojana_year_wise",
    "water tanks": "mukhyamantri_peyjal_nishchay_yojana_year_wise",
    
    # Mukhyamantri Shahar Gali-Nali Pakikaran Yojana
    "urban drainage": "mukhyamantri_shahar_gali_nali_pakikaran_yojana_year_wise",
    "street paving": "mukhyamantri_shahar_gali_nali_pakikaran_yojana_year_wise",
    "gali-nali": "mukhyamantri_shahar_gali_nali_pakikaran_yojana_year_wise",
    
    # Multi-Storied Housing Scheme
    "urban housing": "multi_storied_housing_schemes_year_wise",
    "affordable housing": "multi_storied_housing_schemes_year_wise",
    "housing for poor": "multi_storied_housing_schemes_year_wise",
    
    # Municipal Corporation Buildings
    "urban development": "municipal_corporation_buildings_district_wise_year_wise",
    "municipal projects": "municipal_corporation_buildings_district_wise_year_wise",
    "building status": "municipal_corporation_buildings_district_wise_year_wise",
    
    # Nali Gali Pakkiraran Yojana
    "drainage construction": "nali_gali_pakkikaran_yojana_district_wise_block_wise_year_wise",
    "ward drainage": "nali_gali_pakkikaran_yojana_district_wise_block_wise_year_wise",
    "sanction amounts": "nali_gali_pakkikaran_yojana_district_wise_block_wise_year_wise",
    
    # Nali-Gali Report
    "urban infrastructure": "nali_gali_report_district_wise_year_wise",
    "paved drains": "nali_gali_report_district_wise_year_wise",
    "ULB works": "nali_gali_report_district_wise_year_wise",
    
    # National Highways
    "NH data": "national_highways_number_wise",
    "highway length": "national_highways_number_wise",
    "road transportation": "national_highways_number_wise",
    
    # Medhavriti Yojna
    "SC/ST scholarships": "number_of_medhavriti_yojna_beneficiaries",
    "merit scholarships": "number_of_medhavriti_yojna_beneficiaries",
    
    # Ration Cards
    "PDS": "number_of_ration_cards_and_members_district_wise",
    "ration cards": "number_of_ration_cards_and_members_district_wise",
    "PHH cards": "number_of_ration_cards_and_members_district_wise",
    "AAY cards": "number_of_ration_cards_and_members_district_wise",
    
    # Service Plus
    "e-services": "number_of_services_year_wise_district_wise_block_wise",
    "service delivery": "number_of_services_year_wise_district_wise_block_wise",
    "digital services": "number_of_services_year_wise_district_wise_block_wise",
    
    # Patna Smart City
    "smart city": "patna_smartcity_agencywise_summary_report",
    "urban projects": "patna_smartcity_agencywise_summary_report",
    "agency progress": "patna_smartcity_agencywise_summary_report",
    
    # MKUY Payments
    "girl child benefits": "payment_to_mothers_under_mkuy_scheme",
    "mother payments": "payment_to_mothers_under_mkuy_scheme",
    
    # Polytechnic Admissions
    "diploma admissions": "polytechnic_college_students_district_branch_year_wise",
    "technical education": "polytechnic_college_students_district_branch_year_wise",
    "lateral entry": "polytechnic_college_students_district_branch_year_wise",
    
    # Cattle Population
    "livestock census": "population_of_cattle_breed_gender_wise_in_bihar_yearly_trend",
    "cattle gender": "population_of_cattle_breed_gender_wise_in_bihar_yearly_trend",
    "milch animals": "population_of_cattle_breed_gender_wise_in_bihar_yearly_trend",
    
    # Post Matric Scholarships
    "post-matric": "post_matric_scheme_student_benefecries_district_wise",
    "student scholarships": "post_matric_scheme_student_benefecries_district_wise",
    "hostel students": "post_matric_scheme_student_benefecries_district_wise",
    
    # Poultry Farming
    "layer poultry": "poultry_farming_animal_husbandry_year_wise_district_wise",
    "feed mills": "poultry_farming_animal_husbandry_year_wise_district_wise",
    "poultry capacity": "poultry_farming_animal_husbandry_year_wise_district_wise",
    
    # PMGSY-I
    "PMGSY-I": "pradhan_mantri_gram_sadak_yojana_i_targets_and_achievements",
    "rural roads I": "pradhan_mantri_gram_sadak_yojana_i_targets_and_achievements",
    "village connectivity": "pradhan_mantri_gram_sadak_yojana_i_targets_and_achievements",
    
    # PMGSY-II
    "PMGSY-II": "pradhan_mantri_gram_sadak_yojana_ii_targets_and_achievements",
    "rural roads II": "pradhan_mantri_gram_sadak_yojana_ii_targets_and_achievements",
    "road upgrades": "pradhan_mantri_gram_sadak_yojana_ii_targets_and_achievements",
    
    # PMGSY-III
    "PMGSY-III": "pradhan_mantri_gram_sadak_yojana_iii_targets_and_achievements",
    "rural roads III": "pradhan_mantri_gram_sadak_yojana_iii_targets_and_achievements",
    "road consolidation": "pradhan_mantri_gram_sadak_yojana_iii_targets_and_achievements",
    
    # Fertilizer Production
    "fertilizer production": "production_import_npk_fertilizer_year_wise",
    "NPK imports": "production_import_npk_fertilizer_year_wise",
    "soil health": "production_import_npk_fertilizer_year_wise",
    
    # Public Health Housing
    "housing schemes": "public_health_housing_details_district_wise_year_wise",
    "Panchayati Raj": "public_health_housing_details_district_wise_year_wise",
    "PHED": "public_health_housing_details_district_wise_year_wise",
    
    # Road Quality
    "road conditions": "quality_of_roads_year_wise_road_type_wise",
    "road maintenance": "quality_of_roads_year_wise_road_type_wise",
    "lane types": "quality_of_roads_year_wise_road_type_wise",
    
    # Mining Enforcement
    "mining raids": "raids_fir_arrests_district_wise",
    "mining FIRs": "raids_fir_arrests_district_wise",
    "mining revenue": "raids_fir_arrests_district_wise",

    "raids_fir_arrests_year_wise": "raids_fir_arrests_year_wise",
    "mining enforcement statistics": "raids_fir_arrests_year_wise",
    "Bihar mining raids": "raids_fir_arrests_year_wise",
    "mining FIRs yearwise": "raids_fir_arrests_year_wise",
    "mining arrests Bihar": "raids_fir_arrests_year_wise",
    "mining revenue collection": "raids_fir_arrests_year_wise",
    "mining enforcement data": "raids_fir_arrests_year_wise",

    "rainfall_in_bihar_yearwise_districtwise_month_wise": "rainfall_in_bihar_yearwise_districtwise_month_wise",
    "Bihar rainfall data": "rainfall_in_bihar_yearwise_districtwise_month_wise",
    "districtwise rainfall Bihar": "rainfall_in_bihar_yearwise_districtwise_month_wise",
    "monthly rainfall deviation": "rainfall_in_bihar_yearwise_districtwise_month_wise",
    "monsoon rainfall Bihar": "rainfall_in_bihar_yearwise_districtwise_month_wise",
    "actual vs normal rainfall": "rainfall_in_bihar_yearwise_districtwise_month_wise",
    "Bihar precipitation data": "rainfall_in_bihar_yearwise_districtwise_month_wise",

    "registrar_office_details": "registrar_office_details",
    "Bihar registration offices": "registrar_office_details",
    "district registrar count": "registrar_office_details",
    "sub-registrar offices Bihar": "registrar_office_details",
    "land registration offices": "registrar_office_details",
    "property registration offices": "registrar_office_details",

    "revenue_year_wise": "revenue_year_wise",
    "mining revenue Bihar": "revenue_year_wise",
    "geology department revenue": "revenue_year_wise",
    "mineral revenue collection": "revenue_year_wise",
    "sand mining revenue": "revenue_year_wise",
    "mining penalties Bihar": "revenue_year_wise",

    "road_category_with_their_lengths_year_wise": "road_category_with_their_lengths_year_wise",
    "Bihar road length": "road_category_with_their_lengths_year_wise",
    "road infrastructure Bihar": "road_category_with_their_lengths_year_wise",
    "single lane double lane roads": "road_category_with_their_lengths_year_wise",
    "road network length": "road_category_with_their_lengths_year_wise",

    "road_construction_overview_year_wise_road_category_type_wise": "road_construction_overview_year_wise_road_category_type_wise",
    "road construction overview": "road_construction_overview_year_wise_road_category_type_wise",
    "national highways Bihar": "road_construction_overview_year_wise_road_category_type_wise",
    "state highways percentage": "road_construction_overview_year_wise_road_category_type_wise",
    "district roads length": "road_construction_overview_year_wise_road_category_type_wise",
    "greenfield projects Bihar": "road_construction_overview_year_wise_road_category_type_wise",

    "road_construction_projects_road_names_wise_project_cost_wise": "road_construction_projects_road_names_wise_project_cost_wise",
    "road project details": "road_construction_projects_road_names_wise_project_cost_wise",
    "Bihar road construction status": "road_construction_projects_road_names_wise_project_cost_wise",
    "road project costs": "road_construction_projects_road_names_wise_project_cost_wise",
    "ongoing road projects": "road_construction_projects_road_names_wise_project_cost_wise",

    "road_construction_schemes_year_wise": "road_construction_schemes_year_wise",
    "road construction schemes": "road_construction_schemes_year_wise",
    "Bihar road expenditure": "road_construction_schemes_year_wise",
    "centrally sponsored road schemes": "road_construction_schemes_year_wise",
    "RIDF road projects": "road_construction_schemes_year_wise",

    "road_projects_bharatmala_pariyojana_year_wise": "road_projects_bharatmala_pariyojana_year_wise",
    "Bharatmala projects Bihar": "road_projects_bharatmala_pariyojana_year_wise",
    "national highway construction": "road_projects_bharatmala_pariyojana_year_wise",
    "road project allocation": "road_projects_bharatmala_pariyojana_year_wise",
    "Bharatmala status": "road_projects_bharatmala_pariyojana_year_wise",

    "roads_under_rwd_district_wise_block_wise_year_wise": "roads_under_rwd_district_wise_block_wise_year_wise",
    "Rural Works Department roads": "roads_under_rwd_district_wise_block_wise_year_wise",
    "PMGSY MMGSY roads": "roads_under_rwd_district_wise_block_wise_year_wise",
    "blockwise rural roads": "roads_under_rwd_district_wise_block_wise_year_wise",
    "village road connectivity": "roads_under_rwd_district_wise_block_wise_year_wise",

    "sand_ghats_district_wise": "sand_ghats_district_wise",
    "sand mining ghats": "sand_ghats_district_wise",
    "districtwise sand ghats": "sand_ghats_district_wise",
    "sand collection points": "sand_ghats_district_wise",

    "school_aanganwadi_household_water_quality_testing_yearwise": "school_aanganwadi_household_water_quality_testing_yearwise",
    "water quality testing": "school_aanganwadi_household_water_quality_testing_yearwise",
    "school water testing": "school_aanganwadi_household_water_quality_testing_yearwise",
    "Aanganwadi water quality": "school_aanganwadi_household_water_quality_testing_yearwise",
    "household water testing": "school_aanganwadi_household_water_quality_testing_yearwise",

    "sector_wise_start_up_bihar": "sector_wise_start_up_bihar",
    "Bihar startup data": "sector_wise_start_up_bihar",
    "SMIC approved startups": "sector_wise_start_up_bihar",
    "startup seed funding": "sector_wise_start_up_bihar",
    "sectorwise entrepreneurship": "sector_wise_start_up_bihar",

    "seed_analysis_report_year_wise": "seed_analysis_report_year_wise",
    "seed quality testing": "seed_analysis_report_year_wise",
    "seed certification Bihar": "seed_analysis_report_year_wise",
    "agricultural seed standards": "seed_analysis_report_year_wise",
    "seed sample analysis": "seed_analysis_report_year_wise",

    "seed_distribution_year_wise": "seed_distribution_year_wise",
    "crop seed distribution": "seed_distribution_year_wise",
    "seed target achievement": "seed_distribution_year_wise",
    "agricultural seed supply": "seed_distribution_year_wise",
    "paddy wheat seed distribution": "seed_distribution_year_wise",

    "seed_production_bihar_yearwise": "seed_production_bihar_yearwise",
    "seed production statistics": "seed_production_bihar_yearwise",
    "certified seed production": "seed_production_bihar_yearwise",
    "seed storage data": "seed_production_bihar_yearwise",
    "Manak standard seeds": "seed_production_bihar_yearwise",

    "service_application_details_year_wise_district_wise_block_wise": "service_application_details_year_wise_district_wise_block_wise",
    "Service Plus applications": "service_application_details_year_wise_district_wise_block_wise",
    "government service approvals": "service_application_details_year_wise_district_wise_block_wise",
    "application processing status": "service_application_details_year_wise_district_wise_block_wise",
    "blockwise service applications": "service_application_details_year_wise_district_wise_block_wise",

    "soil_testing_year_wise": "soil_testing_year_wise",
    "soil health cards": "soil_testing_year_wise",
    "agricultural soil testing": "soil_testing_year_wise",
    "soil sample collection": "soil_testing_year_wise",
    "farmland soil analysis": "soil_testing_year_wise",

    "state_wise_district_wise_child_birth_issues": "state_wise_district_wise_child_birth_issues",
    "child nutrition indicators": "state_wise_district_wise_child_birth_issues",
    "maternal healthcare data": "state_wise_district_wise_child_birth_issues",
    "stunting wasting data": "state_wise_district_wise_child_birth_issues",
    "institutional births percentage": "state_wise_district_wise_child_birth_issues",

    "stone_kilns_district_wise": "stone_kilns_district_wise",
    "stone crushing units": "stone_kilns_district_wise",
    "mining stone kilns": "stone_kilns_district_wise",
    "districtwise kiln count": "stone_kilns_district_wise",

    "students_block_wise_genderwise_class_wise_yearwise": "students_block_wise_genderwise_class_wise_yearwise",
    "UDISE enrollment data": "students_block_wise_genderwise_class_wise_yearwise",
    "school student statistics": "students_block_wise_genderwise_class_wise_yearwise",
    "genderwise class enrollment": "students_block_wise_genderwise_class_wise_yearwise",
    "blockwise school data": "students_block_wise_genderwise_class_wise_yearwise",

    "sugarcane_incentive_program_yearwise": "sugarcane_incentive_program_yearwise",
    "sugarcane farmer incentives": "sugarcane_incentive_program_yearwise",
    "agricultural incentive program": "sugarcane_incentive_program_yearwise",
    "crop support scheme": "sugarcane_incentive_program_yearwise",
    "sugarcane production support": "sugarcane_incentive_program_yearwise",

    "total_revenue_vs_target_year_wise": "total_revenue_vs_target_year_wise",
    "mining revenue targets": "total_revenue_vs_target_year_wise",
    "revenue achievement percentage": "total_revenue_vs_target_year_wise",
    "geology department targets": "total_revenue_vs_target_year_wise",
    "mineral revenue performance": "total_revenue_vs_target_year_wise",

    "total_students_teachers_districtwise_non_genderwise": "total_students_teachers_districtwise_non_genderwise",
    "district education statistics": "total_students_teachers_districtwise_non_genderwise",
    "classwise student count": "total_students_teachers_districtwise_non_genderwise",
    "teacher student ratio": "total_students_teachers_districtwise_non_genderwise",
    "Bihar school enrollment": "total_students_teachers_districtwise_non_genderwise",

    "tourists_place_wise_district_wise_type_wise_year_wise": "tourists_place_wise_district_wise_type_wise_year_wise",
    "Bihar tourism statistics": "tourists_place_wise_district_wise_type_wise_year_wise",
    "domestic foreign tourist data": "tourists_place_wise_district_wise_type_wise_year_wise",
    "yearwise tourist destinations": "tourists_place_wise_district_wise_type_wise_year_wise",
    "Gaya Bodh Gaya visitors": "tourists_place_wise_district_wise_type_wise_year_wise",
    "Nalanda Rajgir tourism": "tourists_place_wise_district_wise_type_wise_year_wise",
    "Shrawani Sonepur Mela": "tourists_place_wise_district_wise_type_wise_year_wise",

    "tourists_place_wise_type_wise_year_wise_month_wise": "tourists_place_wise_type_wise_year_wise_month_wise",
    "monthly tourist visits": "tourists_place_wise_type_wise_year_wise_month_wise",
    "Bihar tourism monthly data": "tourists_place_wise_type_wise_year_wise_month_wise",
    "districtwise monthly visitors": "tourists_place_wise_type_wise_year_wise_month_wise",
    "religious tourism statistics": "tourists_place_wise_type_wise_year_wise_month_wise",

    "tourists_type_wise_year_wise_month_wise": "tourists_type_wise_year_wise_month_wise",
    "Bihar tourist arrivals": "tourists_type_wise_year_wise_month_wise",
    "monthly visitor statistics": "tourists_type_wise_year_wise_month_wise",
    "domestic foreign tourist count": "tourists_type_wise_year_wise_month_wise",
    "tourism department data": "tourists_type_wise_year_wise_month_wise",

    "trainee_course_wise_completion_details": "trainee_course_wise_completion_details",
    "BIPARD training records": "trainee_course_wise_completion_details",
    "government official training": "trainee_course_wise_completion_details",
    "rural development courses": "trainee_course_wise_completion_details",
    "public administration training": "trainee_course_wise_completion_details",

    "training_programme_details": "training_programme_details",
    "government training programs": "training_programme_details",
    "residential training details": "training_programme_details",
    "course coordinator information": "training_programme_details",
    "trainee department records": "training_programme_details",

    "types_of_milk_resource": "types_of_milk_resource",
    "Bihar milk cooperatives": "types_of_milk_resource",
    "dairy plants count": "types_of_milk_resource",
    "artificial insemination centers": "types_of_milk_resource",
    "cattle feed plants": "types_of_milk_resource",

    "urban_development_schemes_and_financial_details_year_wise": "urban_development_schemes_and_financial_details_year_wise",
    "urban housing schemes": "urban_development_schemes_and_financial_details_year_wise",
    "UDHD financial details": "urban_development_schemes_and_financial_details_year_wise",
    "city development projects": "urban_development_schemes_and_financial_details_year_wise",
    "urban infrastructure Bihar": "urban_development_schemes_and_financial_details_year_wise",

    "urban_water_supply_guidelines": "urban_water_supply_guidelines",
    "water supply protocols": "urban_water_supply_guidelines",
    "urban water maintenance": "urban_water_supply_guidelines",
    "water quality directives": "urban_water_supply_guidelines",
    "public water guidelines": "urban_water_supply_guidelines",

    "vehicles_auctioned_district_wise": "vehicles_auctioned_district_wise",
    "government vehicle auctions": "vehicles_auctioned_district_wise",
    "auction revenue Bihar": "vehicles_auctioned_district_wise",
    "districtwise vehicle sales": "vehicles_auctioned_district_wise",
    "public auction records": "vehicles_auctioned_district_wise",

    "veterinary_infrastructure_year_wise": "veterinary_infrastructure_year_wise",
    "animal hospitals Bihar": "veterinary_infrastructure_year_wise",
    "veterinary dispensaries": "veterinary_infrastructure_year_wise",
    "livestock health facilities": "veterinary_infrastructure_year_wise",
    "animal husbandry infrastructure": "veterinary_infrastructure_year_wise",

    "villages_tested_for_water_quality_district_wise_block_wise": "villages_tested_for_water_quality_district_wise_block_wise",
    "water testing villages": "villages_tested_for_water_quality_district_wise_block_wise",
    "bacteriological chemical testing": "villages_tested_for_water_quality_district_wise_block_wise",
    "pre post monsoon water": "villages_tested_for_water_quality_district_wise_block_wise",
    "rural water safety": "villages_tested_for_water_quality_district_wise_block_wise",

    "water_level_in_river_stations_in_Bihar_agriculture": "water_level_in_river_stations_in_Bihar_agriculture",
    "river water levels": "water_level_in_river_stations_in_Bihar_agriculture",
    "agricultural water monitoring": "water_level_in_river_stations_in_Bihar_agriculture",
    "Bihar river stations": "water_level_in_river_stations_in_Bihar_agriculture",
    "water resources data": "water_level_in_river_stations_in_Bihar_agriculture",

    "water_quality_lab_testing_district_wise_block_wise": "water_quality_lab_testing_district_wise_block_wise",
    "water lab test results": "water_quality_lab_testing_district_wise_block_wise",
    "contamination remediation": "water_quality_lab_testing_district_wise_block_wise",
    "PHED water testing": "water_quality_lab_testing_district_wise_block_wise",
    "bacteriological analysis": "water_quality_lab_testing_district_wise_block_wise",

    "water_quality_testing_drinking_water_sources_wise_district_wise": "water_quality_testing_drinking_water_sources_wise_district_wise",
    "drinking water safety": "water_quality_testing_drinking_water_sources_wise_district_wise",
    "PWS source testing": "water_quality_testing_drinking_water_sources_wise_district_wise",
    "water source contamination": "water_quality_testing_drinking_water_sources_wise_district_wise",
    "monsoon water quality": "water_quality_testing_drinking_water_sources_wise_district_wise",

    "wetlands_in_bihar_district_wise_year_wise": "wetlands_in_bihar_district_wise_year_wise",
    "Bihar wetland conservation": "wetlands_in_bihar_district_wise_year_wise",
    "waterbody area records": "wetlands_in_bihar_district_wise_year_wise",
    "wetland coordinates": "wetlands_in_bihar_district_wise_year_wise",
    "ecological water bodies": "wetlands_in_bihar_district_wise_year_wise",

    "year_wise_bihar_sports_culture_archaeology_schemes_details": "year_wise_bihar_sports_culture_archaeology_schemes_details",
    "cultural heritage schemes": "year_wise_bihar_sports_culture_archaeology_schemes_details",
    "sports development programs": "year_wise_bihar_sports_culture_archaeology_schemes_details",
    "archaeology preservation": "year_wise_bihar_sports_culture_archaeology_schemes_details",
    "government cultural initiatives": "year_wise_bihar_sports_culture_archaeology_schemes_details",

    "year_wise_block_wise_weather_data": "year_wise_block_wise_weather_data",
    "Bihar weather records": "year_wise_block_wise_weather_data",
    "temperature rainfall data": "year_wise_block_wise_weather_data",
    "humidity wind speed": "year_wise_block_wise_weather_data",
    "Mausam Kendra reports": "year_wise_block_wise_weather_data",

    "year_wise_district_wise_block_wise_cold_wave_details": "year_wise_district_wise_block_wise_cold_wave_details",
    "winter relief measures": "year_wise_district_wise_block_wise_cold_wave_details",
    "bonfire night shelters": "year_wise_district_wise_block_wise_cold_wave_details",
    "cold wave response": "year_wise_district_wise_block_wise_cold_wave_details",
    "blanket distribution": "year_wise_district_wise_block_wise_cold_wave_details",

    "year_wise_district_wise_covid_payment": "year_wise_district_wise_covid_payment",
    "COVID relief funds": "year_wise_district_wise_covid_payment",
    "pandemic financial assistance": "year_wise_district_wise_covid_payment",
    "4 lakh 50 thousand relief": "year_wise_district_wise_covid_payment",
    "disaster management payments": "year_wise_district_wise_covid_payment",

    "year_wise_district_wise_ejanani_beneficiaries": "year_wise_district_wise_ejanani_beneficiaries",
    "e-Janani scheme data": "year_wise_district_wise_ejanani_beneficiaries",
    "institutional delivery payments": "year_wise_district_wise_ejanani_beneficiaries",
    "Kanya Utthan Yojna": "year_wise_district_wise_ejanani_beneficiaries",
    "mother child benefits": "year_wise_district_wise_ejanani_beneficiaries",

    "year_wise_district_wise_flood_affected_data": "year_wise_district_wise_flood_affected_data",
    "Bihar flood statistics": "year_wise_district_wise_flood_affected_data",
    "disaster impact assessment": "year_wise_district_wise_flood_affected_data",
    "flood relief measures": "year_wise_district_wise_flood_affected_data",
    "agricultural damage floods": "year_wise_district_wise_flood_affected_data",
    "animal relief camps": "year_wise_district_wise_flood_affected_data",

    "year_wise_houses_sanctioned_under_pmay_scheme": "year_wise_houses_sanctioned_under_pmay_scheme",
    "PMAY housing Bihar": "year_wise_houses_sanctioned_under_pmay_scheme",
    "Awas Yojana approvals": "year_wise_houses_sanctioned_under_pmay_scheme",
    "rural housing scheme": "year_wise_houses_sanctioned_under_pmay_scheme",
    "affordable housing count": "year_wise_houses_sanctioned_under_pmay_scheme"

}


    for keyword, table in KEYWORD_TABLE_MAP.items():
        if keyword in input_lower:
            matched_tables.add(table)

    for table_name, table_info in table_schemas.items():
        # Check table description
        if table_info.get("description") and any(word in input_lower for word in table_info["description"].lower().split()):
            matched_tables.add(table_name)

        # Check column names and descriptions
        for col, col_desc in table_info.get("columns", {}).items():
            if col.lower() in input_lower or any(word in input_lower for word in col_desc.lower().split()):
                matched_tables.add(table_name)

    return list(matched_tables)
