# Unit 3 | Assignment - Py Me Up, Charlie
# PyBank 

# Andy Oh

import os
import csv

file_input = "budget_data_2.csv"
file_output = "result_PyBank2.csv"

csvpath = os.path.join('raw_data', file_input)

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    count_row = 0
    total_revenue = 0
    greatest_increase = 0
    greatest_decrease = 0
    budget_chart = []
    date_high = ""
    date_low = ""

    for row in csvreader:
        date = row[0]
        revenue = int(row[1])
        count_row += 1
        total_revenue += int(row[1])
        budget_chart.append({"Date": date, "Revenue": revenue})

        if(revenue > greatest_increase):
            greatest_increase = revenue
            date_high = row[0]

        if(revenue < greatest_increase):
            greatest_decrease = revenue
            date_low = row[0]

    avg_revenue = float(total_revenue / count_row)
   
    print("\nFinancial Analysis")
    print("----------------------------")
    print("Total Months: " + str(count_row))
    print("Total Revenue: $" + str(total_revenue))
    print("Average Revenue Change: $" + str(avg_revenue))
    print("Greatest Increase in Revenue: " + str(date_high) + " " + str(greatest_increase))
    print("Greatest Decrease in Revenue: " + str(date_low) + " " +str(greatest_decrease))

    # Specify the file to write to
    with open(file_output, 'w', newline='') as csvfile:

        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the first row (column headers)
        csvwriter.writerow(['Financial Analysis'])
        csvwriter.writerow(['Total Months', str(count_row)])
        csvwriter.writerow(['Total Revenue ($)', str(total_revenue)])
        csvwriter.writerow(['Average Revenue Change ($)', str(avg_revenue)])
        csvwriter.writerow(["Greatest Increase in Revenue: " + str(greatest_increase)])
        csvwriter.writerow(["Greatest Decrease in Revenue: " + str(greatest_decrease)])