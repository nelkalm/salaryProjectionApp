import streamlit as st
import datetime
from datetime import date

FRINGE = 0.6524
INDIRECT = 0.349
COLA23 = 1
COLA24 = 1.03
COLA25 = 1.05
COLA26 = 1.05
COLA27 = 1.0325
COLA_LIST = [COLA23, COLA24, COLA25, COLA26, COLA27]
MAX_DATE = datetime.date(2027, 12, 31)

# from jobData import job_data

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


salary_schedule = [
    {"schedule": "B", "data": {
        '01': [25980, 26796, 28128, 29412, 30852, 32304, 34176, 35808, 37512, 39312, 41124, 43092, 45168],
        '02': [27264, 28128, 29412, 30852, 32304, 33816, 35808, 37512, 39312, 41124, 43092, 45168, 47268],
        '03': [28524, 29412, 30852, 32304, 33816, 35412, 37512, 39312, 41124, 43092, 45168, 47268, 49488],
        '04': [31320, 32304, 33816, 35412, 37116, 38868, 41124, 43092, 45168, 47268, 49488, 51888, 54324],
        '05': [31836, 32832, 34380, 36036, 37740, 39528, 41832, 43848, 45888, 48048, 50376, 52740, 55212],
        '06': [36000, 37116, 38868, 40716, 42600, 44712, 47268, 49488, 51888, 54324, 56868, 59592, 62460],
        '07': [37704, 38868, 40716, 42600, 44712, 46776, 49488, 51888, 54324, 56868, 59592, 62460, 65388],
        '08': [39492, 40716, 42600, 44712, 46776, 48996, 51888, 54324, 56868, 59592, 62460, 65388, 68556],
        '09': [43344, 44712, 46776, 48996, 51372, 53784, 56868, 59592, 62460, 65388, 68556, 71784, 75168],
        '10': [47532, 48996, 51372, 53784, 56328, 59004, 62460, 65388, 68556, 71784, 75168, 78804, 82500],
        '11': [52176, 53784, 56328, 59004, 61872, 64740, 68556, 71784, 75168, 78804, 82500, 86436, 90540],
        '12': [57240, 59004, 61872, 64740, 67872, 71052, 75168, 78804, 82500, 86436, 90540, 94824, 99360],
        '13': [62784, 64740, 67872, 71052, 74424, 77964, 82500, 86436, 90540, 94824, 99360, 103980, 108996],
        '14': [68940, 71052, 74424, 77964, 81672, 85572, 90540, 94824, 99360, 103980, 108996, 114252, 119580],
        '15': [75624, 77964, 81672, 85572, 89640, 93876, 99360, 103980, 108996, 114252, 119580, 125292, 131232],
        '16': [83028, 85572, 89640, 93876, 98388, 102996, 108996, 114252, 119580, 125292, 131232, 137484, 143976],
        '17': [91044, 93876, 98388, 102996, 107904, 113064, 119580, 125292, 131232, 137484, 143976, 150888, 157932]
    }
    },
    {"schedule": "G", "data": {
        '01': [45972, 47388, 49740, 52092, 54708, 57636, 60336, 63504, 67200],
        '02': [50544, 52092, 54708, 57636, 60336, 63504, 66528, 69972, 74196],
        '03': [55908, 57636, 60336, 63504, 66528, 69972, 73392, 77052, 81816],
        '04': [61572, 63504, 66528, 69972, 73392, 77052, 81000, 85044, 90108],
        '05': [67860, 69972, 73392, 77052, 81000, 85044, 89208, 93804, 99480],
        '06': [74712, 77052, 81000, 85044, 89208, 93804, 98496, 102996, 108756],
        '07': [82500, 85044, 89208, 93804, 98496, 102996, 107652, 112500, 118632],
        '08': [90984, 93804, 98496, 102996, 107652, 112500, 117432, 122796, 129540],
        '09': [99876, 102996, 107652, 112500, 117432, 122796, 128256, 134028, 141624],
        '10': [109128, 112500, 117432, 122796, 128256, 134028, 140220, 146448, 150828]
    }
    }]


def get_salary(title, step, salary_schedule, start_date):
    # Find the job in job_data based on the position title
    job_info = None
    for job in job_data:
        if job[0] == title:
            job_info = job
            break

    if job_info is None:
        return None  # Job title not found

    # Extract the schedule and grade from the job_info
    schedule = job_info[1]
    grade = job_info[2]

    # Check if regrading is applicable
    regrade_date = date(2025, 1, 1)
    if start_date >= regrade_date and grade in ['6', '7']:
        grade = '8'

    # Find the salary for the given grade and step
    salary_data = None
    for data in salary_schedule:
        if data['schedule'] == schedule:
            salary_data = data['data']
            break

    if salary_data is None or grade not in salary_data or step >= len(salary_data[grade]):
        return None  # Invalid grade or step

    salary = salary_data[grade][step]

    return salary


# Function to return a list of salaries based on the number of years worked
def get_salary_steps(position, years_worked, salary_schedule, start_date):
    salaries_list = []
    for i in range(years_worked):
        salary = get_salary(position, i, salary_schedule,
                            start_date) * COLA_LIST[i]
        salaries_list.append(salary)
    return salaries_list


# Function to calculate average annual salary, average annual fringe, average annual indirect
def calculate_average_annuals(salaries_list):
    total_salary = sum(salaries_list)
    num_years = len(salaries_list)
    average_salary = total_salary / num_years
    average_fringe = average_salary * FRINGE
    average_indirect = average_salary * INDIRECT
    return average_salary, average_fringe, average_indirect


def format_currency(amount):
    return "${:,.2f}".format(amount)


# Get the position names from job_data
position_names = [position[0] for position in job_data]

# Streamlit app


def main():
    st.title("Salary Projection App")
    st.write("Enter the required information below:")

    # Input fields
    person_name = st.text_input("Person's Name")
    position_name = st.selectbox("Position Name", position_names)
    start_date = st.date_input("Start Date")
    grant_end_date = st.date_input("End Date", max_value=MAX_DATE)

    if st.button("Calculate Salaries"):
        years_worked = (grant_end_date - start_date).days // 365
        salaries = get_salary_steps(
            position_name, years_worked, salary_schedule, start_date)

        # Output the list of salaries
        st.write(
            f"Salaries for {position_name} over {years_worked} years:")
        for i, salary in enumerate(salaries):
            st.write(f"Year {i}: {format_currency(salary)}")

        average_salary, average_fringe, average_indirect = calculate_average_annuals(
            salaries)

        st.write(f"Average annual salary: {format_currency(average_salary)}")
        st.write(f"Average annual fringe: {format_currency(average_fringe)}")
        st.write(
            f"Average annual indirect: {format_currency(average_indirect)}")


if __name__ == "__main__":
    main()
