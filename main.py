import streamlit as st
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


FRINGE = 0.6524
INDIRECT = 0.349
COLA23 = 1
COLA24 = 1.03
COLA25 = 1.05
COLA26 = 1.05
COLA27 = 1.0325
COLA_LIST = [COLA23, COLA24, COLA25, COLA26, COLA27]
# MAX_DATE = datetime.date(2027, 12, 31)

job_data = [
    ("ADMIN SERVICES OFFICER I-EXCLUDED", "BX", "13", ""),
    ("ADMINISTRATIVE ASST II", "B", "10", ""),
    ("ADMINISTRATIVE ASST III", "B", "12", ""),
    ("ADMINISTRATIVE SERVICES OFFICER I", "B", "13", ""),
    ("ADMINISTRATIVE SERVICES OFFICER II", "B", "15", ""),
    ("ASST COMMISSIONER", "SR", "", ""),
    ("ASST PROGRAM DIR", "B", "14", ""),
    ("ATTORNEY", "SR", "", ""),
    ("AUDIO-VISUAL SPECIALIST", "B", "11", ""),
    ("AUDITOR III", "G", "07", ""),
    ("BEHAVIORAL HEALTH ASSISTANT", "B", "10", ""),
    ("BUILDING/CONSTRUCTION INSPECTOR", "T", "16", ""),
    ("CASE MANAGER ASST", "B", "11", ""),
    ("CERTIFIED MEDICAL ASST", "B", "09", ""),
    ("CHIEF CONTRACT EXPEDITER", "B", "15", ""),
    ("CHIEF SANITARIAN", "BX", "17", ""),
    ("CLERK III", "B", "08", ""),
    ("CLERK IV", "B", "10", ""),
    ("CLINICAL THERAPIST III", "G", "07", ""),
    ("COMMISSIONER OF HEALTH", "EX", "", ""),
    ("COMMUNICABLE DISEASE CONTROL INVESTIGATOR II", "B", "12", ""),
    ("COMMUNITY OUTREACH COORD", "B", "14", ""),
    ("CONTRACTS ADMINISTRATOR", "SR", "", ""),
    ("CONTRACTS COMPLIANCE COORD", "B", "15", "X"),
    ("CONTRACTS REVIEW SPECIALIST II", "B", "13", ""),
    ("COORD OF GRANTS MANAGEMENT", "B", "14", ""),
    ("COORDINATING PLANNER", "SR", "", ""),
    ("DATA BASE ANALYST", "G", "06", ""),
    ("DATA SERVICES ADMINISTRATOR", "BX", "17", ""),
    ("DENTAL ASST", "B", "10", ""),
    ("DENTIST", "M", "SR", "X"),
    ("DEPUTY COMMISSIONER", "EX", "", ""),
    ("DIR / COMMUNITY LIAISON", "EX", "", ""),
    ("DIR OF ADMINISTRATION", "SR", "X", ""),
    ("DIR OF ADMINISTRATION I", "BX", "15", ""),
    ("DIR OF ADMINISTRATION II", "BX", "16", ""),
    ("DIR OF ADMINISTRATIVE SERVICES", "SR", "", ""),
    ("DIR OF DISEASE INVESTIGATIONS", "BX", "18", ""),
    ("DIR OF ENVIR HEALTH & SAFETY COMPLIANCE", "SR", "", ""),
    ("DIR OF ENVIRONMENTAL INSPECTIONS", "BX", "17", ""),
    ("DIR OF EPIDEMIOLOGY", "SR", "", ""),
    ("DIR OF MENTAL HEALTH CENTER", "BX", "17", ""),
    ("DIR OF NUTRITION", "SR", "", ""),
    ("DIR OF PLANNING RESEARCH AND DEVELOPMENT", "SR", "", ""),
    ("DIR OF PROGRAM OPERATIONS", "SR", "", ""),
    ("DIR OF PUBLIC AFFAIRS", "SR", "", ""),
    ("DIR OF PUBLIC HEALTH OPERATIONS", "BX", "18", ""),
    ("DIR OF SCHOOL NURSING", "", "", ""),
    ("DIRECTOR OF MARKETING", "SR", "", ""),
    ("ENVIRONMENTAL ENGINEER I", "G", "06", ""),
    ("ENVIRONMENTAL ENGINEER II", "G", "07", ""),
    ("ENVIRONMENTAL ENGINEER III", "G", "08", ""),
    ("ENVIRONMENTAL INVESTIGATOR", "B", "14", ""),
    ("EPIDEMIOLOGIST II", "G", "07", ""),
    ("EPIDEMIOLOGIST III", "G", "09", ""),
    ("EPIDEMIOLOGIST IV", "GY", "11", ""),
    ("EXEC ADMINISTRATIVE ASST II", "BX", "15", ""),
    ("FINANCE OFFICER", "G", "07", ""),
    ("FIRST DEPUTY COMMISSIONER", "EX", "", ""),
    ("GENERAL COUNSEL", "EX", "", ""),
    ("GIS ANALYST", "B", "13", ""),
    ("GRANTS RESEARCH SPECIALIST", "G", "07", ""),
    ("HEAD STOREKEEPER", "B", "10", ""),
    ("HEALTH CODE ENFORCEMENT INSPECTION ANALYST", "B", "13", ""),
    ("INFECTION PREVENTION SPECIALIST", "GY", "10", ""),
    ("INFORMATION COORD", "BX", "16", ""),
    ("INQUIRY AIDE III", "B", "09", ""),
    ("LABOR RELATIONS SUPVSR", "GY", "05", ""),
    ("LABORATORY TECHNICIAN III", "B", "11", ""),
    ("MANAGER OF QUALITY ASSURANCE", "SR", "", ""),
    ("MANAGING DEPUTY COMMISSIONER", "EX", "", ""),
    ("MEDICAL DIR", "SR", "", ""),
    ("MENTAL HEALTH CRISIS CLINICIAN", "", "", ""),
    ("MGR OF EMERGENCY MANAGEMENT SERVICES", "B", "17", ""),
    ("MGR OF FOOD PROTECTION SERVICES", "SR", "", ""),
    ("NURSE PRACTITIONER", "S", "08", ""),
    ("POLICY ANALYST", "SR", "", ""),
    ("PROGRAM ANALYST", "B", "14", ""),
    ("PROGRAM AUDITOR III", "B", "14", ""),
    ("PROGRAM DIR", "BX", "17", ""),
    ("PROJECT COORD", "BX", "15", ""),
    ("PROJECT MANAGER", "SR", "", ""),
    ("PROJECTS ADMINISTRATOR", "SR", "", ""),
    ("PSYCHIATRIC NURSE PRACTIONER", "", "", ""),
    ("PSYCHOLOGIST", "G", "08", ""),
    ("PUBLIC HEALTH ADM III - EXCLUDED", "BX", "16", ""),
    ("PUBLIC HEALTH ADMINISTRATOR I", "B", "12", ""),
    ("PUBLIC HEALTH ADMINISTRATOR II", "B", "14", ""),
    ("PUBLIC HEALTH ADMINISTRATOR III", "B", "16", ""),
    ("PUBLIC HEALTH AIDE", "B", "08", ""),
    ("PUBLIC HEALTH INFORMATICS SPECIALIST", "GY", "08", ""),
    ("PUBLIC HEALTH NURSE I", "S", "04", ""),
    ("PUBLIC HEALTH NURSE II", "S", "05", ""),
    ("PUBLIC HEALTH NURSE III", "SZ", "06", ""),
    ("PUBLIC HEALTH NURSE IV", "SZ", "07", ""),
    ("PUBLIC HEALTH NUTRITIONIST I", "G", "02", ""),
    ("PUBLIC HEALTH NUTRITIONIST II", "G", "03", ""),
    ("PUBLIC HEALTH NUTRITIONIST III", "GY", "05", ""),
    ("RECOVERY TEAM PROGRAM MGR", "", "", ""),
    ("REGIONAL COMMUNICABLE DISEASE INVESTIGATOR", "B", "15", ""),
    ("REGIONAL NUTRITION COORD", "G", "07", ""),
    ("SANITARIAN II", "B", "14", ""),
    ("SENIOR DATA ENTRY OPERATOR", "B", "09", ""),
    ("SENIOR EMERGENCY MANAGEMENT COORD", "B", "16", ""),
    ("SENIOR ENVIRONMENTAL INSPECTOR", "B", "14", ""),
    ("SENIOR EQUITY OFFICER", "", "", ""),
    ("SENIOR HELP DESK TECHNICIAN", "B", "14", ""),
    ("SENIOR PERSONNEL ASSISTANT", "B", "12", ""),
    ("SENIOR POLICY ANALYST", "SR", "", ""),
    ("SENIOR PROGRAMMER/ANALYST", "G", "08", ""),
    ("SR DIR OF CRISIS SERVICES", "", "", ""),
    ("SR RECOVERY TEAM PROGRAM MGR", "", "", ""),
    ("STAFF ASSISTANT - EXCLUDED", "BX", "13", ""),
    ("STAFF ASST", "B", "13", ""),
    ("SUPERVISING DISEASE CONTROL INVESTIGATOR", "B", "14", ""),
    ("SUPERVISING DISEASE CONTROL INVESTIGATOR - EXCL", "BX", "14", ""),
    ("SUPERVISING ENVIRONMENTAL ENGINEER", "GY", "10", ""),
    ("SUPERVISING ENVIRONMENTAL INSPECTOR", "BX", "15", ""),
    ("SUPERVISING SANITARIAN", "BX", "16", ""),
    ("SUPRVNG BUILDING/CONTRUCT INSPECTOR", "T", "17", ""),
    ("SUPVSR OF DATA ENTRY OPERATORS", "B", "11", ""),
    ("SUPVSR OF PERSONNEL ADMINISTRATION", "BX", "17", ""),
    ("TRAINING DIRECTOR", "BX", "16", ""),
    ("TRAINING OFFICER", "B", "14", ""),
    ("WEB AUTHOR", "B", "15", "")
]

salary_schedule = {'B': {'01': [2165, 2233, 2344, 2451, 2571, 2692, 2848, 2984, 3126], '02': [2272, 2344, 2451, 2571, 2692, 2818, 2984, 3126, 3276], '03': [2377, 2451, 2571, 2692, 2818, 2951, 3126, 3276, 3427], '04': [2610, 2692, 2818, 2951, 3093, 3239, 3427, 3591, 3764], '05': [2653, 2736, 2865, 3003, 3145, 3294, 3486, 3654, 3824], '06': [3000, 3093, 3239, 3393, 3550, 3726, 3939, 4124, 4324], '07': [3142, 3239, 3393, 3550, 3726, 3898, 4124, 4324, 4527], '08': [3291, 3393, 3550, 3726, 3898, 4083, 4324, 4527, 4739], '09': [3612, 3726, 3898, 4083, 4281, 4482, 4739, 4966, 5205], '10': [3961, 4083, 4281, 4482, 4694, 4917, 5205, 5449, 5713], '11': [4348, 4482, 4694, 4917, 5156, 5395, 5713, 5982, 6264], '12': [4770, 4917, 5156, 5395, 5656, 5921, 6264, 6567, 6875], '13': [5232, 5395, 5656, 5921, 6202, 6497, 6875, 7203, 7545], '14': [
    5745, 5921, 6202, 6497, 6806, 7131, 7545, 7902, 8280], '15': [6302, 6497, 6806, 7131, 7470, 7823, 8280, 8665, 9083], '16': [6919, 7131, 7470, 7823, 8199, 8583, 9083, 9521, 9965], '17': [7587, 7823, 8199, 8583, 8992, 9422, 9965, 10441, 10936]},

    'G': {'01': [3831, 3949, 4145, 4341, 4559, 4803, 5028, 5292, 5600], '02': [4212, 4341, 4559, 4803, 5028, 5292, 5544, 5831, 6183], '03': [4659, 4803, 5028, 5292, 5544, 5831, 6116, 6421, 6818], '04': [5131, 5292, 5544, 5831, 6116, 6421, 6750, 7087, 7509], '05': [5655, 5831, 6116, 6421, 6750, 7087, 7434, 7817, 8290], '06': [6226, 6421, 6750, 7087, 7434, 7817, 8208, 8583, 9063], '07': [6875, 7087, 7434, 7817, 8208, 8583, 8971, 9375, 9886], '08': [7582, 7817, 8208, 8583, 8971, 9375, 9786, 10233, 10795], '09': [8323, 8583, 8971, 9375, 9786, 10233, 10688, 11169, 11802], '10': [9094, 9375, 9786, 10233, 10688, 11169, 11685, 12204, 12569]}}


def get_step_raises(position_title, job_data, salary_schedule):
    for title, schedule, grade, step in job_data:
        if title == position_title:
            if schedule in salary_schedule and grade in salary_schedule[schedule]:
                return salary_schedule[schedule][grade]

    return None


def generate_monthly_salaries(position_title, start_date, end_date, job_data, salary_schedule):
    step_raises = get_step_raises(position_title, job_data, salary_schedule)
    if step_raises is None:
        return None

    start_date = datetime.strptime(start_date, "%m/%d/%Y")
    end_date = datetime.strptime(end_date, "%m/%d/%Y")
    num_months = (end_date.year - start_date.year) * 12 + \
        (end_date.month - start_date.month) + 1

    monthly_salaries = []
    step_raise_index = 0

    for i in range(num_months):
        monthly_salaries.append(step_raises[step_raise_index])

        if (i + 1) % 12 == 0:
            step_raise_index = (step_raise_index + 1) % len(step_raises)

    return monthly_salaries


if __name__ == '__main__':
    job_title1 = "GRANTS RESEARCH SPECIALIST"
    start_date1 = "7/1/2023"
    end_date1 = "6/30/2025"

    job_title2 = "ENVIRONMENTAL INVESTIGATOR"
    start_date2 = "1/1/2024"
    end_date2 = "12/31/2024"

    step_raises = get_step_raises(job_title1, job_data, salary_schedule)
    print(step_raises)
    monthly_salaries = generate_monthly_salaries(
        job_title1, start_date1, end_date1, job_data, salary_schedule)
    print(monthly_salaries)

    # print(get_monthly_salary_per_month(job_title1, start_date1, end_date1))
    # print(calculate_annual_salary(job_title1, start_date1, end_date1))

    # print()

    # print(get_monthly_salary_per_month(job_title2, start_date2, end_date2))
    # print(calculate_annual_salary(job_title2, start_date2, end_date2))
