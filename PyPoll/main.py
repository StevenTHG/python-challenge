# Import Dependencies
import os
import csv

# File paths
election_data_csv = os.path.join("PyPoll","Resources", "election_data.csv")
output_file = os.path.join("PyPoll", "analysis", "analysis.txt")

# Initialize variables
total_votes = 0
candidates_list = []
cand_vote = [0, 0, 0]

# Open and read csv
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header and first row
    csv_header = next(csv_reader)
    first_row = next(csv_reader)
    
    # Update variables with entries from first row
    total_votes += 1
    candidates_list.append(first_row[2])
    cand_vote[0] += 1

    # Read through each row of data after the first row and update variables
    for row in csv_reader:
        total_votes += 1
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            cand_vote[candidates_list.index(row[2])] += 1
        else:
            cand_vote[candidates_list.index(row[2])] += 1

# Creates and calculates vote percentages for each candidate
cand_percentage = []
for vote in cand_vote:
    cand_percentage.append(float(vote) / float(total_votes) * 100)

# Calculates the winner of the election
winner = candidates_list[cand_vote.index(max(cand_vote))]

# Create output string for analysis
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"{candidates_list[0]}: {cand_percentage[0]:.3f}% ({cand_vote[0]})\n"
    f"{candidates_list[1]}: {cand_percentage[1]:.3f}% ({cand_vote[1]})\n"
    f"{candidates_list[2]}: {cand_percentage[2]:.3f}% ({cand_vote[2]})\n"
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n")

# # Write to output txt file
with open(output_file, "w") as txtfile:
    writer = txtfile.write(output)
