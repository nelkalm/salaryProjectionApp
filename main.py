import streamlit as st
import pandas as pd

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


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

salary_schedule = {
    'B': {'2023': {
        '01': (25980, 26796, 28128, 29412, 30852, 32304, 34176, 35808, 37512, 39312, 41124, 43092, 45084, 47168),
        '02': (27264, 28128, 29412, 30852, 32304, 33816, 35808, 37512, 39312, 41124, 43092, 45084, 47268),
        '03': (28524, 29412, 30852, 32304, 33816, 35412, 37512, 39312, 41124, 43092, 45084, 47268, 49488),
        '04': (31320, 32304, 33816, 35412, 37116, 38868, 41124, 43092, 45084, 47268, 49488, 51888, 54324),
        '05': (31836, 32832, 34380, 36036, 37740, 39528, 41832, 43848, 45888, 48048, 50376, 52740, 55212),
        '06': (36000, 37116, 38868, 40716, 42600, 44712, 47268, 49488, 51888, 54324, 56868, 59592, 62460),
        '07': (37704, 38868, 40716, 42600, 44712, 46776, 49488, 51888, 54324, 56868, 59592, 62460, 65388),
        '08': (39492, 40716, 42600, 44712, 46776, 48996, 51888, 54324, 56868, 59592, 62460, 65388, 68556),
        '09': (43344, 44712, 46776, 48996, 51372, 53784, 56868, 59592, 62460, 65388, 68556, 71784, 75168),
        '10': (47532, 48996, 51372, 53784, 56328, 59004, 62460, 65388, 68556, 71784, 75168, 78804, 82500),
        '11': (52176, 53784, 56328, 59004, 61872, 64740, 68556, 71784, 75168, 78804, 82500, 86436, 90540),
        '12': (57240, 59004, 61872, 64740, 67872, 71052, 75168, 78804, 82500, 86436, 90540, 94824, 99360),
        '13': (62784, 64740, 67872, 71052, 74424, 77964, 82500, 86436, 90540, 94824, 99360, 103980, 108996),
        '14': (68940, 71052, 74424, 77964, 81672, 85572, 90540, 94824, 99360, 103980, 108996, 114252, 119580),
        '15': (75624, 77964, 81672, 85572, 89640, 93876, 99360, 103980, 108996, 114252, 119580, 125292, 131232),
        '16': (83028, 85572, 89640, 93876, 98388, 102996, 108996, 114252, 119580, 125292, 131232, 137484, 143976),
        '17': (91044, 93876, 98388, 102996, 107904, 113064, 119580, 125292, 131232, 137484, 143976, 150888, 157932)
    }, '2024': {
        '01': (26759.40, 27599.88, 28971.84, 30294.36, 31777.56, 33273.12, 35201.28, 36882.24, 38637.36, 40491.36, 42357.72, 44384.76, 46523.04),
        '02': (28081.92, 28971.84, 30294.36, 31777.56, 33273.12, 34830.48, 36882.24, 38637.36, 40491.36, 42357.72, 44384.76, 46523.04, 48686.04),
        '03': (29379.72, 30294.36, 31777.56, 33273.12, 34830.48, 36474.36, 38637.36, 40491.36, 42357.72, 44384.76, 46523.04, 48686.04, 50972.64),
        '04': (32259.60, 33273.12, 34830.48, 36474.36, 38229.48, 40034.04, 42357.72, 44384.76, 46523.04, 48686.04, 50972.64, 53444.64, 55953.72),
        '05': (32791.08, 33816.96, 35411.40, 37117.08, 38872.20, 40713.84, 43086.96, 45163.44, 47264.64, 49489.44, 51887.28, 54322.20, 56868.36),
        '06': (37080.00, 38229.48, 40034.04, 41937.48, 43878.00, 46053.36, 48686.04, 50972.64, 53444.64, 55953.72, 58574.04, 61379.76, 64333.80),
        '07': (38835.12, 40034.04, 41937.48, 43878.00, 46053.36, 48179.28, 50972.64, 53444.64, 55953.72, 58574.04, 61379.76, 64333.80, 67349.64),
        '08': (40676.76, 41937.48, 43878.00, 46053.36, 48179.28, 50465.88, 53444.64, 55953.72, 58574.04, 61379.76, 64333.80, 67349.64, 70612.68),
        '09': (44644.32, 46053.36, 48179.28, 50465.88, 52913.16, 55397.52, 58574.04, 61379.76, 64333.80, 67349.64, 70612.68, 73937.52, 77423.04),
        '10': (48957.96, 50465.88, 52913.16, 55397.52, 58017.84, 60774.12, 64333.80, 67349.64, 70612.68, 73937.52, 77423.04, 81168.12, 84975.00),
        '11': (53741.28, 55397.52, 58017.84, 60774.12, 63728.16, 66682.20, 70612.68, 73937.52, 77423.04, 81168.12, 84975.00, 89029.08, 93256.20),
        '12': (58957.20, 60774.12, 63728.16, 66682.20, 69908.16, 73183.56, 77423.04, 81168.12, 84975.00, 89029.08, 93256.20, 97668.72, 102340.80),
        '13': (64667.52, 66682.20, 69908.16, 73183.56, 76656.72, 80302.92, 84975.00, 89029.08, 93256.20, 97668.72, 102340.80, 107099.40, 112265.88),
        '14': (71008.20, 73183.56, 76656.72, 80302.92, 84122.16, 88139.16, 93256.20, 97668.72, 102340.80, 107099.40, 112265.88, 117679.56, 123167.40),
        '15': (77892.72, 80302.92, 84122.16, 88139.16, 92329.20, 96692.28, 102340.80, 107099.40, 112265.88, 117679.56, 123167.40, 129050.76, 135168.96),
        '16': (85518.84, 88139.16, 92329.20, 96692.28, 101339.64, 106085.88, 112265.88, 117679.56, 123167.40, 129050.76, 135168.96, 141608.52, 148295.28),
        '17': (93775.32, 96692.28, 101339.64, 106085.88, 111141.12, 116455.92, 123167.40, 129050.76, 135168.96, 141608.52, 148295.28, 155414.64, 162669.96)
    }, '2025': {
        '01': (28097.37, 28979.87, 30420.43, 31809.08, 33366.44, 34936.78, 36961.34, 38726.35, 40569.23, 42515.93, 44475.61, 46604.00, 48849.19),
        '02': (29486.02, 30420.43, 31809.08, 33366.44, 34936.78, 36572.00, 38726.35, 40569.23, 42515.93, 44475.61, 46604.00, 48849.19, 51120.34),
        '03': (30848.71, 31809.08, 33366.44, 34936.78, 36572.00, 38298.08, 40569.23, 42515.93, 44475.61, 46604.00, 48849.19, 51120.34, 53521.27),
        '04': (33872.58, 34936.78, 36572.00, 38298.08, 40140.95, 42035.74, 44475.61, 46604.00, 48849.19, 51120.34, 53521.27, 56116.87, 58751.41),
        '05': (34430.63, 35507.81, 37181.97, 38972.93, 40815.81, 42749.53, 45241.31, 47421.61, 49627.87, 51963.91, 54481.64, 57038.31, 59711.78),
        '06': (38934.00, 40140.95, 42035.74, 44034.35, 46071.90, 48356.03, 51120.34, 53521.27, 56116.87, 58751.41, 61502.74, 64448.75, 67550.49),
        '07': (40776.88, 42035.74, 44034.35, 46071.90, 48356.03, 50588.24, 53521.27, 56116.87, 58751.41, 61502.74, 64448.75, 67550.49, 70717.12),
        '08': (42710.60, 44034.35, 46071.90, 48356.03, 50588.24, 52989.17, 56116.87, 58751.41, 61502.74, 64448.75, 67550.49, 70717.12, 74143.31),
        '09': (46876.54, 48356.03, 50588.24, 52989.17, 55558.82, 58167.40, 61502.74, 64448.75, 67550.49, 70717.12, 74143.31, 77634.40, 81294.19),
        '10': (51405.86, 52989.17, 55558.82, 58167.40, 60918.73, 63812.83, 67550.49, 70717.12, 74143.31, 77634.40, 81294.19, 85226.53, 89223.75),
        '11': (56428.34, 58167.40, 60918.73, 63812.83, 66914.57, 70016.31, 74143.31, 77634.40, 81294.19, 85226.53, 89223.75, 93480.53, 97919.01),
        '12': (61905.06, 63812.83, 66914.57, 70016.31, 73403.57, 76842.74, 81294.19, 85226.53, 89223.75, 93480.53, 97919.01, 102552.16, 107457.84),
        '13': (67900.90, 70016.31, 73403.57, 76842.74, 80489.56, 84318.07, 89223.75, 93480.53, 97919.01, 102552.16, 107457.84, 112454.37, 117879.17),
        '14': (74558.61, 76842.74, 80489.56, 84318.07, 88328.27, 92546.12, 97919.01, 102552.16, 107457.84, 112454.37, 117879.17, 123563.54, 129325.77),
        '15': (81787.36, 84318.07, 88328.27, 92546.12, 96945.66, 101526.89, 107457.84, 112454.37, 117879.17, 123563.54, 129325.77, 135503.30, 141927.41),
        '16': (89794.78, 92546.12, 96945.66, 101526.89, 106406.62, 111390.17, 117879.17, 123563.54, 129325.77, 135503.30, 141927.41, 148688.95, 155710.04),
        '17': (98464.09, 101526.89, 106406.62, 111390.17, 116698.18, 122278.72, 129325.77, 135503.30, 141927.41, 148688.95, 155710.04, 163185.37, 170803.46)
    }, '2026': {
        '01': (29502.24, 30428.87, 31941.45, 33399.53, 35034.76, 36683.61, 38809.41, 40662.67, 42597.69, 44641.72, 46699.39, 48934.20, 51291.65),
        '02': (30960.32, 31941.45, 33399.53, 35034.76, 36683.61, 38400.60, 40662.67, 42597.69, 44641.72, 46699.39, 48934.20, 51291.65, 53676.36),
        '03': (32391.14, 33399.53, 35034.76, 36683.61, 38400.60, 40212.98, 42597.69, 44641.72, 46699.39, 48934.20, 51291.65, 53676.36, 56197.34),
        '04': (35566.21, 36683.61, 38400.60, 40212.98, 42148.00, 44137.53, 46699.39, 48934.20, 51291.65, 53676.36, 56197.34, 58922.72, 61688.98),
        '05': (36152.17, 37283.20, 39041.07, 40921.58, 42856.60, 44887.01, 47503.37, 49792.69, 52109.27, 54562.11, 57205.73, 59890.23, 62697.37),
        '06': (40880.70, 42148.00, 44137.53, 46236.07, 48375.50, 50773.83, 53676.36, 56197.34, 58922.72, 61688.98, 64577.88, 67671.19, 70928.01),
        '07': (42815.72, 44137.53, 46236.07, 48375.50, 50773.83, 53117.66, 56197.34, 58922.72, 61688.98, 64577.88, 67671.19, 70928.01, 74252.98),
        '08': (44846.13, 46236.07, 48375.50, 50773.83, 53117.66, 55638.63, 58922.72, 61688.98, 64577.88, 67671.19, 70928.01, 74252.98, 77850.48),
        '09': (49220.36, 50773.83, 53117.66, 55638.63, 58336.76, 61075.77, 64577.88, 67671.19, 70928.01, 74252.98, 77850.48, 81516.12, 85358.90),
        '10': (53976.15, 55638.63, 58336.76, 61075.77, 63964.67, 67003.47, 70928.01, 74252.98, 77850.48, 81516.12, 85358.90, 89487.85, 93684.94),
        '11': (59249.76, 61075.77, 63964.67, 67003.47, 70260.30, 73517.13, 77850.48, 81516.12, 85358.90, 89487.85, 93684.94, 98154.56, 102814.96),
        '12': (65000.31, 67003.47, 70260.30, 73517.13, 77073.75, 80684.87, 85358.90, 89487.85, 93684.94, 98154.56, 102814.96, 107679.76, 112830.73),
        '13': (71295.94, 73517.13, 77073.75, 80684.87, 84514.03, 88533.97, 93684.94, 98154.56, 102814.96, 107679.76, 112830.73, 118077.09, 123773.13),
        '14': (78286.54, 80684.87, 84514.03, 88533.97, 92744.68, 97173.42, 102814.96, 107679.76, 112830.73, 118077.09, 123773.13, 129741.71, 135792.06),
        '15': (85876.72, 88533.97, 92744.68, 97173.42, 101792.94, 106603.24, 112830.73, 118077.09, 123773.13, 129741.71, 135792.06, 142278.46, 149023.78),
        '16': (94284.52, 97173.42, 101792.94, 106603.24, 111726.95, 116959.68, 123773.13, 129741.71, 135792.06, 142278.46, 149023.78, 156123.39, 163495.55),
        '17': (103387.29, 106603.24, 111726.95, 116959.68, 122533.08, 128392.65, 135792.06, 142278.46, 149023.78, 156123.39, 163495.55, 171344.64, 179343.63)
    }, '2027': {
        '01': (30461.06, 31417.81, 32979.55, 34485.02, 36173.39, 37875.83, 40070.72, 41984.21, 43982.11, 46092.58, 48217.12, 50524.56, 52958.63),
        '02': (31966.53, 32979.55, 34485.02, 36173.39, 37875.83, 39648.62, 41984.21, 43982.11, 46092.58, 48217.12, 50524.56, 52958.63, 55420.84),
        '03': (33443.85, 34485.02, 36173.39, 37875.83, 39648.62, 41519.90, 43982.11, 46092.58, 48217.12, 50524.56, 52958.63, 55420.84, 58023.75),
        '04': (36722.11, 37875.83, 39648.62, 41519.90, 43517.81, 45572.00, 48217.12, 50524.56, 52958.63, 55420.84, 58023.75, 60837.70, 63693.87),
        '05': (37327.11, 38494.90, 40309.90, 42251.53, 44249.44, 46345.84, 49047.23, 51410.96, 53802.82, 56335.38, 59064.91, 61836.66, 64735.03),
        '06': (42209.32, 43517.81, 45572.00, 47738.74, 49947.70, 52423.98, 55420.84, 58023.75, 60837.70, 63693.87, 66676.66, 69870.50, 73233.17),
        '07': (44207.23, 45572.00, 47738.74, 49947.70, 52423.98, 54843.98, 58023.75, 60837.70, 63693.87, 66676.66, 69870.50, 73233.17, 76666.20),
        '08': (46303.63, 47738.74, 49947.70, 52423.98, 54843.98, 57446.89, 60837.70, 63693.87, 66676.66, 69870.50, 73233.17, 76666.20, 80380.62),
        '09': (50820.02, 52423.98, 54843.98, 57446.89, 60232.70, 63060.73, 66676.66, 69870.50, 73233.17, 76666.20, 80380.62, 84165.39, 88133.07),
        '10': (55730.38, 57446.89, 60232.70, 63060.73, 66043.52, 69181.08, 73233.17, 76666.20, 80380.62, 84165.39, 88133.07, 92396.21, 96729.70),
        '11': (61175.38, 63060.73, 66043.52, 69181.08, 72543.76, 75906.43, 80380.62, 84165.39, 88133.07, 92396.21, 96729.70, 101344.58, 106156.45),
        '12': (67112.82, 69181.08, 72543.76, 75906.43, 79578.64, 83307.13, 88133.07, 92396.21, 96729.70, 101344.58, 106156.45, 111179.36, 116497.73),
        '13': (73613.06, 75906.43, 79578.64, 83307.13, 87260.74, 91411.32, 96729.70, 101344.58, 106156.45, 111179.36, 116497.73, 121914.59, 127795.76),
        '14': (80830.85, 83307.13, 87260.74, 91411.32, 95758.88, 100331.56, 106156.45, 111179.36, 116497.73, 121914.59, 127795.76, 133958.32, 140205.30),
        '15': (88667.72, 91411.32, 95758.88, 100331.56, 105101.21, 110067.84, 116497.73, 121914.59, 127795.76, 133958.32, 140205.30, 146902.51, 153867.05),
        '16': (97348.77, 100331.56, 105101.21, 110067.84, 115358.08, 120760.87, 127795.76, 133958.32, 140205.30, 146902.51, 153867.05, 161197.40, 168809.15),
        '17': (106747.38, 110067.84, 115358.08, 120760.87, 126515.41, 132565.41, 140205.30, 146902.51, 153867.05, 161197.40, 168809.15, 176913.34, 185172.30)
    }
    },
    'G': {
        '2023': {
            '01': [45972.0, 47388.0, 49740.0, 52092.0, 54708.0, 57636.0, 60336.0, 63504.0, 67200.0],
            '02': [50544.0, 52092.0, 54708.0, 57636.0, 60336.0, 63504.0, 66528.0, 69972.0, 74196.0],
            '03': [55908.0, 57636.0, 60336.0, 63504.0, 66528.0, 69972.0, 73392.0, 77052.0, 81816.0],
            '04': [61572.0, 63504.0, 66528.0, 69972.0, 73392.0, 77052.0, 81000.0, 85044.0, 90108.0],
            '05': [67860.0, 69972.0, 73392.0, 77052.0, 81000.0, 85044.0, 89208.0, 93804.0, 99480.0],
            '06': [74712.0, 77052.0, 81000.0, 85044.0, 89208.0, 93804.0, 98496.0, 102996.0, 108756.0],
            '07': [82500.0, 85044.0, 89208.0, 93804.0, 98496.0, 102996.0, 107652.0, 112500.0, 118632.0],
            '08': [90984.0, 93804.0, 98496.0, 102996.0, 107652.0, 112500.0, 117432.0, 122796.0, 129540.0],
            '09': [99876.0, 102996.0, 107652.0, 112500.0, 117432.0, 122796.0, 128256.0, 134028.0, 141624.0],
            '10': [109128.0, 112500.0, 117432.0, 122796.0, 128256.0, 134028.0, 140220.0, 146448.0, 150828.0]
        },
        '2024': {
            '01': [47351.16, 48809.64, 51232.2, 53654.76, 56349.24, 59365.08, 62146.08, 65409.12, 69216.0],
            '02': [52060.32, 53654.76, 56349.24, 59365.08, 62146.08, 65409.12, 68523.84, 72071.16, 76421.88],
            '03': [57585.24, 59365.08, 62146.08, 65409.12, 68523.84, 72071.16, 75593.76, 79363.56, 84270.48],
            '04': [63419.16, 65409.12, 68523.84, 72071.16, 75593.76, 79363.56, 83430.0, 87595.32, 92811.24],
            '05': [69895.8, 72071.16, 75593.76, 79363.56, 83430.0, 87595.32, 91884.24, 96618.12, 102464.4],
            '06': [76953.36, 79363.56, 83430.0, 87595.32, 91884.24, 96618.12, 101450.88, 106085.88, 112018.68],
            '07': [84975.0, 87595.32, 91884.24, 96618.12, 101450.88, 106085.88, 110881.56, 115875.0, 122190.96],
            '08': [93713.52, 96618.12, 101450.88, 106085.88, 110881.56, 115875.0, 120954.96, 126479.88, 133426.2],
            '09': [102872.28, 106085.88, 110881.56, 115875.0, 120954.96, 126479.88, 132103.68, 138048.84, 145872.72],
            '10': [112401.84, 115875.0, 120954.96, 126479.88, 132103.68, 138048.84, 144426.6, 150841.44, 155352.84]
        },
        '2025': {
            '01': [49718.72, 51250.12, 53793.81, 56337.5, 59166.7, 62333.33, 65253.38, 68679.58, 72676.8],
            '02': [54663.34, 56337.5, 59166.7, 62333.33, 65253.38, 68679.58, 71950.03, 75674.72, 80242.97],
            '03': [60464.5, 62333.33, 65253.38, 68679.58, 71950.03, 75674.72, 79373.45, 83331.74, 88484.0],
            '04': [66590.12, 68679.58, 71950.03, 75674.72, 79373.45, 83331.74, 87601.5, 91975.09, 97451.8],
            '05': [73390.59, 75674.72, 79373.45, 83331.74, 87601.5, 91975.09, 96478.45, 101449.03, 107587.62],
            '06': [80801.03, 83331.74, 87601.5, 91975.09, 96478.45, 101449.03, 106523.42, 111390.17, 117619.61],
            '07': [89223.75, 91975.09, 96478.45, 101449.03, 106523.42, 111390.17, 116425.64, 121668.75, 128300.51],
            '08': [98399.2, 101449.03, 106523.42, 111390.17, 116425.64, 121668.75, 127002.71, 132803.87, 140097.51],
            '09': [108015.89, 111390.17, 116425.64, 121668.75, 127002.71, 132803.87, 138708.86, 144951.28, 153166.36],
            '10': [118021.93, 121668.75, 127002.71, 132803.87, 138708.86, 144951.28, 151647.93, 158383.51, 163120.48]
        },
        '2026': {
            '01': [52204.65, 53812.63, 56483.5, 59154.37, 62125.04, 65450.0, 68516.05, 72113.55, 76310.64],
            '02': [57396.5, 59154.37, 62125.04, 65450.0, 68516.05, 72113.55, 75547.53, 79458.45, 84255.12],
            '03': [63487.73, 65450.0, 68516.05, 72113.55, 75547.53, 79458.45, 83342.12, 87498.32, 92908.2],
            '04': [69919.62, 72113.55, 75547.53, 79458.45, 83342.12, 87498.32, 91981.58, 96573.84, 102324.39],
            '05': [77060.12, 79458.45, 83342.12, 87498.32, 91981.58, 96573.84, 101302.37, 106521.48, 112967.0],
            '06': [84841.08, 87498.32, 91981.58, 96573.84, 101302.37, 106521.48, 111849.6, 116959.68, 123500.59],
            '07': [93684.94, 96573.84, 101302.37, 106521.48, 111849.6, 116959.68, 122246.92, 127752.19, 134715.53],
            '08': [103319.16, 106521.48, 111849.6, 116959.68, 122246.92, 127752.19, 133352.84, 139444.07, 147102.39],
            '09': [113416.69, 116959.68, 122246.92, 127752.19, 133352.84, 139444.07, 145644.31, 152198.85, 160824.67],
            '10': [123923.03, 127752.19, 133352.84, 139444.07, 145644.31, 152198.85, 159230.33, 166302.69, 171276.51]
        },
        '2027': {
            '01': [53901.31, 55561.54, 58319.21, 61076.89, 64144.1, 67577.13, 70742.82, 74457.25, 78790.74],
            '02': [59261.89, 61076.89, 64144.1, 67577.13, 70742.82, 74457.25, 78002.83, 82040.85, 86993.41],
            '03': [65551.08, 67577.13, 70742.82, 74457.25, 78002.83, 82040.85, 86050.74, 90342.02, 95927.72],
            '04': [72192.01, 74457.25, 78002.83, 82040.85, 86050.74, 90342.02, 94970.98, 99712.49, 105649.93],
            '05': [79564.57, 82040.85, 86050.74, 90342.02, 94970.98, 99712.49, 104594.7, 109983.43, 116638.43],
            '06': [87598.41, 90342.02, 94970.98, 99712.49, 104594.7, 109983.43, 115484.71, 120760.87, 127514.36],
            '07': [96729.7, 99712.49, 104594.7, 109983.43, 115484.71, 120760.87, 126219.94, 131904.13, 139093.79],
            '08': [106677.03, 109983.43, 115484.71, 120760.87, 126219.94, 131904.13, 137686.81, 143976.0, 151883.21],
            '09': [117102.73, 120760.87, 126219.94, 131904.13, 137686.81, 143976.0, 150377.75, 157145.31, 166051.48],
            '10': [127950.53, 131904.13, 137686.81, 143976.0, 150377.75, 157145.31, 164405.31, 171707.52, 176842.99]
        }
    }
}


class Personnel:
    def __init__(self, position_name, grade, schedule, step, start_date, end_date):
        self.position_name = position_name
        self.grade = grade
        self.schedule = schedule
        self.step = step
        self.start_date = datetime.strptime(start_date, '%m/%d/%Y')
        self.end_date = datetime.strptime(end_date, '%m/%d/%Y')
        self.salary_steps = self.generate_salary_steps()
        self.salary_table = self.generate_hash_table()
        self.eligible_for_regrade = self.check_eligible_for_regrade()
        self.regrade_date = None

    def generate_salary_steps(self):
        # Initialize the salary steps with step 0
        salary_steps = [{"step": 0, "date": self.start_date}]

        # Determine the first eligible step increase date (6 months after the start date)
        next_step_date = self.start_date + relativedelta(months=6)

        # Keep adding step increase dates until the end date is reached
        while next_step_date < self.end_date:
            salary_steps.append(
                {"step": len(salary_steps), "date": next_step_date})
            # Increase step date by 12 months for subsequent steps
            next_step_date += relativedelta(years=1)

        return salary_steps

    def generate_hash_table(self):
        hash_table = {}
        current_date = self.start_date

        while current_date < self.end_date:
            month_year = current_date.strftime('%B %Y')
            hash_table[month_year] = []
            # Add one month to the current date
            if current_date.month == 12:
                current_date = datetime(current_date.year + 1, 1, 1)
            else:
                current_date = datetime(
                    current_date.year, current_date.month + 1, 1)

        return hash_table

    def check_eligible_for_regrade(self):
        return self.grade in ["06", "07"]

    def regrade(self):
        if self.eligible_for_regrade:
            self.regrade_date = datetime(2025, 1, 1)

    def populate_salary_table(self, salary_data):
        current_date = self.start_date
        current_step = self.step
        current_grade = self.grade
        current_schedule = self.schedule
        while current_date <= self.end_date:
            month_year = current_date.strftime('%B %Y')
            current_year = str(current_date.year)
            # handle new year and regrade
            if (current_date.month == 1) or (self.eligible_for_regrade and current_date == self.regrade_date):
                if self.eligible_for_regrade and current_date == self.regrade_date:
                    current_grade = '08'  # update grade due to regrade
                # get the new annual salary
                current_annual_salary = salary_data[current_schedule][current_year][current_grade][current_step]
            # handle step increases
            if month_year in [step['date'].strftime('%B %Y') for step in self.salary_steps]:
                current_step += 1
                # get the new annual salary due to step increase
                current_annual_salary = salary_data[current_schedule][current_year][current_grade][current_step]

            # compute monthly salary
            current_monthly_salary = current_annual_salary / 12
            # update the salary_table for the current month
            self.salary_table[month_year] = [
                current_monthly_salary, current_schedule, current_grade, current_step]
            # advance to next month
            if current_date.month == 12:
                current_date = datetime(current_date.year + 1, 1, 1)
            else:
                current_date += relativedelta(months=1)

    def annual_salaries(self):
        annual_salaries = {}
        current_year_start = self.start_date
        current_year_end = current_year_start + relativedelta(years=1, days=-1)

        while current_year_start <= self.end_date:
            annual_salary = 0
            for month_year in self.salary_table:
                date = datetime.strptime(month_year, '%B %Y')
                if current_year_start <= date <= current_year_end:
                    annual_salary += self.salary_table[month_year][0]
            year_range = f'{current_year_start.strftime("%B %Y")} to {current_year_end.strftime("%B %Y")}'
            annual_salaries[year_range] = round(annual_salary, 2)
            current_year_start += relativedelta(years=1)
            current_year_end += relativedelta(years=1)

        return annual_salaries

    def average_annual_salary(self):
        annual_salaries = self.annual_salaries()
        total_salary = sum(annual_salaries.values())
        avg_annual_salary = total_salary / len(annual_salaries)
        return round(avg_annual_salary, 2)

    def calculate_annual_fringe_cost(self):
        average_annual_salary = self.average_annual_salary()
        fringe_cost = average_annual_salary * 0.6524
        return round(fringe_cost, 2)

    def calculate_annual_indirect_cost(self):
        average_annual_salary = self.average_annual_salary()
        fringe_cost = self.calculate_annual_fringe_cost()
        indirect_cost = (average_annual_salary + fringe_cost) * 0.349
        return round(indirect_cost, 2)


st.title("Salary Projection App")


def get_job_details(job_data, position_title):
    for job in job_data:
        if job[0] == position_title:
            return job[1], job[2], job[3]   # grade, schedule, step
    return None, None, None  # return None if the job was not found


def create_personnel(job):
    for data in job_data:
        if data[0] == job:
            position_name, schedule, grade, step = data
            break
    start_date_str = start_date.strftime('%m/%d/%Y')
    end_date_str = end_date.strftime('%m/%d/%Y')

    personnel = Personnel(position_name, grade, schedule,
                          step, start_date_str, end_date_str)
    personnel.populate_salary_table(salary_schedule)
    return personnel


# Extract all titles
titles = [job[0] for job in job_data]

# Create a form
# Use selectbox instead of text_input
selected_job = st.selectbox("Select Job Title", titles)
start_date = st.date_input("Select Start Date").strftime('%m/%d/%Y')
end_date = st.date_input("Select End Date").strftime('%m/%d/%Y')

if st.button("Calculate Salary Details"):

    schedule, grade, step = get_job_details(job_data, selected_job)
    # st.write(grade, schedule, step)

    personnel = Personnel(selected_job, grade, schedule,
                          -1, start_date, end_date)
    personnel.regrade()
    # if personnel.regrade_date is not None:
    #     print("Regrade date:", personnel.regrade_date.strftime('%m/%d/%Y'))

    personnel.populate_salary_table(salary_schedule)

    st.write(f"Schedule: {personnel.schedule}")
    st.write(f"Grade: {personnel.grade}")

    st.subheader('Monthly Salary Table')
    # st.dataframe(personnel.salary_table)
    # Convert the dictionary into a DataFrame
    monthly_salary_table = pd.DataFrame.from_dict(personnel.salary_table, orient='index',
                                                  columns=['Monthly Salary', 'Schedule', 'Grade', 'Step'])

    # reset index to have a numeric one for iloc to work correctly
    monthly_salary_table.reset_index(inplace=True)

    # Determine the number of chunks to split the DataFrame into
    num_chunks = len(monthly_salary_table) // 12
    if len(monthly_salary_table) % 12 != 0:
        num_chunks += 1

    sum_annual_salaries = []

    # Split the DataFrame into chunks and display each one
    for i in range(num_chunks):
        start_index = i * 12
        end_index = start_index + 12
        chunk = monthly_salary_table.iloc[start_index:end_index]
        st.dataframe(chunk)

        # Compute and display the sum of monthly salaries for each chunk
        sum_annual_salary = chunk['Monthly Salary'].sum()
        st.write(
            f"Sum of Monthly Salaries for this period: ${sum_annual_salary:,.2f}")
        # Append the sum of the annual salary to the list
        sum_annual_salaries.append(round(sum_annual_salary, 2))
        st.text("")  # add an empty line for spacing

    # Calculate total salaries
    total_salary = sum(sum_annual_salaries)

    # Calculate average annual salary based on the number of months
    average_annual_salary = total_salary / (len(monthly_salary_table) / 12)
    average_annual_fringe = average_annual_salary * 0.6524
    average_annual_indirect = (
        average_annual_salary + average_annual_fringe) * 0.349

    # Display the results
    st.write(f"Total Salary: ${total_salary:,.2f}")
    st.write(f"Average Annual Salary: ${average_annual_salary:,.2f}")
    st.write(f"Average Annual Fringe: ${average_annual_fringe:,.2f}")
    st.write(f"Average Annual Indirect: ${average_annual_indirect:,.2f}")


# # Example usage:
# # # STEPS NEED TO START AT -1!!!
# personnel = Personnel("PUBLIC HEALTH ADMINISTRATOR II", "16", "B",
#                       -1, "8/1/2023", "7/31/2027")

# print(personnel.position_name)
# print(personnel.grade)
# print(personnel.schedule)
# print(personnel.step)
# print(personnel.start_date)
# print(personnel.end_date)
# print(personnel.salary_steps)
# print(personnel.salary_table)

# print("Eligible for regrade:", personnel.eligible_for_regrade)

# # Check if eligible for regrade and set the regrade_date
# personnel.regrade()
# if personnel.regrade_date is not None:
#     print("Regrade date:", personnel.regrade_date.strftime('%m/%d/%Y'))


# personnel.populate_salary_table(salary_schedule)
# print(personnel.salary_table)

# print(personnel.annual_salaries())

# print(personnel.average_annual_salary())
