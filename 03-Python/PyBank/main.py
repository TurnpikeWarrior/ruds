# Unit 3 | Assignment - Py Me Up, Charlie
# PyBank 

# Andy Oh

# Dependencies
import os
import csv

# Files to Input/Output
file_input = "budget_data_2.csv"
file_output = "result_PyBank2.csv"

csvpath = os.path.join('raw_data', file_input)

# Reading the file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skipping the first row aka header
    header = next(csvreader)

    # Initializing the variables 
    count_row = 0
    total_revenue = 0
    greatest_increase = 0
    greatest_decrease = 0
    budget_chart = []
    date_high = ""
    date_low = ""

    # Iterating through CSV file
    for row in csvreader:
        date = row[0]
        revenue = int(row[1])
        count_row += 1
        total_revenue += int(row[1])
    
        # Building an array 
        budget_chart.append({"Date": date, "Revenue": revenue})

        # Finding the greatest increase in revenue
        if(revenue > greatest_increase):
            greatest_increase = revenue
            date_high = row[0]

        # Finding the lowest increase in revenue
        if(revenue < greatest_increase):
            greatest_decrease = revenue
            date_low = row[0]
    
    # Average Revenue Change 
    avg_revenue = float(total_revenue / count_row)
   
    # Printing the output 
    print("\nFinancial Analysis")
    print("----------------------------")
    print("Total Months: " + str(count_row))
    print("Total Revenue: $" + str(total_revenue))
    print("Average Revenue Change: $" + str(avg_revenue))
    print("Greatest Increase in Revenue: " + str(date_high) + " " + str(greatest_increase))
    print("Greatest Decrease in Revenue: " + str(date_low) + " " +str(greatest_decrease))

    # Specifying the file to write to
    with open(file_output, 'w', newline='') as csvfile:

        # Initializing csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Writing to output file
        csvwriter.writerow(['Financial Analysis'])
        csvwriter.writerow(['Total Months', str(count_row)])
        csvwriter.writerow(['Total Revenue ($)', str(total_revenue)])
        csvwriter.writerow(['Average Revenue Change ($)', str(avg_revenue)])
        csvwriter.writerow(["Greatest Increase in Revenue: " + str(greatest_increase)])
        csvwriter.writerow(["Greatest Decrease in Revenue: " + str(greatest_decrease)])