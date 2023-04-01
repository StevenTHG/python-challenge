# Import Dependencies
import os
import csv

# File paths
budget_data_csv = os.path.join("PyBank","Resources", "budget_data.csv")
output_file = os.path.join("PyBank", "analysis", "analysis.txt")

# Initialize variables
total_months = 0
total_net = 0
profit_loss_list = []
change_list = []
month_list = []
counter = 0

# Open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header and first row
    csv_header = next(csv_reader)
    first_row = next(csv_reader)
    
    # Update variables with entries from first row
    total_months += 1
    total_net += int(first_row[1])
    profit_loss_list.append(int(first_row[1]))
    month_list.append(first_row[0])

    # Read through each row of data after the first row and update variables
    for row in csv_reader:
        total_months += 1
        month_list.append(row[0])
        total_net += int(row[1])
        profit_loss_list.append(int(row[1]))
        change_list.append(profit_loss_list[counter+1] - profit_loss_list[counter])
        counter += 1

# Calculates the greatest increase/decrease and which month it occurred in
incr_month = month_list[change_list.index(max(change_list))+1]
greatest_incr = max(change_list)
decr_month = month_list[change_list.index(min(change_list))+1]
greatest_decr = min(change_list)

# Calculate average change
average_change = sum(change_list) / len(change_list)

# Create output string for analysis
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {incr_month} (${greatest_incr})\n"
    f"Greatest Decrease in Profits: {decr_month} (${greatest_decr})")

# Write to output txt file
with open(output_file, "w") as txtfile:
    writer = txtfile.write(output)
