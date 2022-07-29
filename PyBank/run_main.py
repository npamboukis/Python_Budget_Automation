# Import libraries
import csv
import os
from pathlib import Path

# Set path to csv file
csvpath = Path('../PyBank/budget_data.csv')

# Hold the total amount of profit
net_profit = []
date = []

with open(csvpath, 'r') as csvfile:
    
#     Read budget_data.csv file
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip header row / line_num will be the row counter & represent # of months
    header = next(csvreader)
    line_num = 0
    
    
    for row in csvreader:
        
        line_num +=1
        
        # Add data to net_profit
        profit = int(row[1])
        
        # Append profit into net_profit
        net_profit.append(profit)
        date.append(row[0])
        
    

max_profit = 0
min_profit = 0
avg_profit = 0
total_profit = 0
profit_change = []

# Change in Profit
for i in range(1, len(net_profit)):
    
    profit_change.append(net_profit[i] - net_profit[i-1])
    
    avg_profit = sum(profit_change) / len(profit_change)
    
    max_profit = max(profit_change)
    
    min_profit = min(profit_change)
    
#     Add date from which max/min_profit reside in
    max_date = str(date[profit_change.index(max(profit_change)) +1])
    min_date = str(date[profit_change.index(min(profit_change)) +1])

# Total Profit
for profit in net_profit:
    
    # Calculate total earnings
    total_profit += profit

# Create a txt file within PyBank folder & display the results
output_path = Path('../PyBank/results.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write("Results from budget_data.csv\n\n'''''\n")
    txtfile.write("\n")
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Months: {line_num}\n")
    txtfile.write(f"Total: ${total_profit}\n")
    txtfile.write(f"Average Change: ${round(avg_profit,2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_date} $({max_profit})\n")
    txtfile.write(f"Greatest Decrease in Profits: {min_date} $({min_profit})\n\n")
    txtfile.write("'''''")
    
    
    
# Display on Terminal
        
# print("")
# print(f"Financial Analysis")
# print(f"--------------------------\n")
# print(f"Total Months: {line_num}")
# print(f"Total: ${total_profit}")
# print(f"Average Change: ${round(avg_profit,2)}")
# print(f"Greatest Increase in Profits: {max_date} $({max_profit})")
# print(f"Greatest Decrease in Profits: {min_date} $({min_profit})\n")