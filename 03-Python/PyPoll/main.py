# Unit 3 | Assignment - Py Me Up, Charlie
# PyPoll 

# Andy Oh

# Unit 3 | Assignment - Py Me Up, Charlie
# PyBank 

# Andy Oh

import os
import csv

csvpath = os.path.join('raw_data', 'election_data_1.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    election_data = []

    for row in csvreader:


    print("\Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    print(candidate_name + ":" + vote_percentage + "%" + "(" + str(total_candidate_votes) + ")")
    print("-------------------------")
    print("Winner: " + winner_name)
    print("-------------------------")
    print("\n")


    # Specify the file to write to
    with open('result_PyPoll.csv', 'w', newline='') as csvfile:

        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the first row (column headers)
        csvwriter.writerow(['Election Results'])
        csvwriter.writerow(['Total Votes Casted', total_votes])
        