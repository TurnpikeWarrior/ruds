# Unit 3 | Assignment - Py Me Up, Charlie
# PyBoss 

# Andy Oh

# Dependencies
import os
import csv

state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Files to Input/Output
file_input = "employee_data1.csv"
file_output = "result_PyBoss.csv"

csvpath = os.path.join('raw_data', file_input)

# Reading the file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skipping the first row aka header
    header = next(csvreader)

    employee_data = []

    for row in csvreader:
        empID = row[0]
        empName = row[1]
        DOB = row[2]
        SSN = row[3]
        state = row[4]

        firstName = empName.split()[0]
        lastName = empName.split()[1]

        if state == state_abbrev[0]
            state = state_abbrev[1]
            
        employee_data.append({empID, firstName, lastName, DOB, SSN, state})
        print(empID, firstName, lastName, DOB, SSN, state)

    # Printing the output 
    # print("EMP ID, First Name, Last Name, DOB, SSN, State")
    
    # print(employee_data)

    # # Specifying the file to write to
    # with open(file_output, 'w', newline='') as csvfile:

    #     # Initializing csv.writer
    #     csvwriter = csv.writer(csvfile, delimiter=',')

    #     # Writing to output file
    #     csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    #     csvwriter.writerow(employee_data)