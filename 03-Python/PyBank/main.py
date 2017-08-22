# Unit 3 | Assignment - Py Me Up, Charlie
# PyBank 

# Andy Oh

import os
import csv
import operator

# files = ['budget_data_1.csv', 'budget_data_2']

csvpath = os.path.join('raw_data', 'budget_data_1.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    count_row = 0
    total_revenue = 0
    max_rev = 0

    budget_chart = []

    for row in csvreader:
        # date = row[0]
        # revenue = float(row[1])
        count_row += 1
        total_revenue += int(row[1])
        # budget_chart.append({"Date": date, "Revenue": revenue})

    avg_revenue = float(total_revenue / count_row)
    # max_rev = max(budget_chart[Revenue])

    print("\nFinancial Analysis")
    print("----------------------------")
    print("Total Months: " + str(count_row))
    print("Total Revenue: $" + str(total_revenue))
    print("Average Revenue Change: $" + str(avg_revenue))
    # print("Greatest Increase in Revenue: " + max_rev)
    # print("Greatest Decrease in Revenue: " + min_rev)
    print("\n")


    # Specify the file to write to
    with open('result_PyBank.csv', 'w', newline='') as csvfile:

        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the first row (column headers)
        csvwriter.writerow(['Financial Analysis'])
        csvwriter.writerow(['Total Months', str(count_row)])
        csvwriter.writerow(['Total Revenue ($)', str(total_revenue)])
        csvwriter.writerow(['Average Revenue Change ($)', str(avg_revenue)])