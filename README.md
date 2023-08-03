# Salary Projection App

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/nelkalm/salaryProjectionApp?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/nelkalm/salaryProjectionApp)
![GitHub issues](https://img.shields.io/github/issues-raw/nelkalm/salaryProjectionApp)

## Project Description
This app is designed to provide detailed salary calculations for specific job positions over a specified period of time. It includes Total Salary, Total Fringe, Total Indirect, and Total Cost calculations. A Monthly Salary Table is also displayed, showing the monthly salary, schedule, grade, and step for each month within the specified period. The application allows for dynamic calculation of fringe and indirect rates based on user input. 

**Note:** This app currently only works for schedules B and G.

## How to Use
To use this application:

1. Select a job title from the dropdown list.
2. Specify the start and end dates for the period over which you want to calculate salaries.
3. Enter the fringe and indirect rates.
4. Click on the "Calculate Salary Details" button to get the salary details.

The application will display the Monthly Salary Table and detailed salary calculations including the Total Salary, Total Fringe, Total Indirect, and Total Cost for the selected job position over the specified period.

## Installation
Clone the repository and install the necessary dependencies mentioned in the requirements.txt file. 

```bash
git clone https://github.com/nelkalm/salaryProjectionApp.git
cd salaryProjectionApp
pip install -r requirements.txt
```

After installing the dependencies, you can run the application locally with the following command:

```bash
streamlit run main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

This project is created by [Nelson Lu](https://www.nelsonlu.me/).
