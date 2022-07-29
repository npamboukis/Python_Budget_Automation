# Import libraries
import csv
import os
from pathlib import Path

# Set path to csv file
csvpath = Path('../PyBank/budget_data.csv')

# Hold the total amount of profit
net_profit = []

with open(csvpath, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    
    # Skip header row
    header = next(csvreader)
    line_num = 0
    
    for row in csvreader:
        
        line_num +=1
        
        # Add data to net_profit
        profit = int(row[1])
        # Append profit into net_profit
        net_profit.append(profit)
        
    # print(line_num)
    # print(net_profit)

max_profit = 0
min_profit = 0
avg_profit = 0
total_profit = 0

for profit in net_profit:
    
    # Calculate total earnings
    total_profit += profit
    
    # Find greatest increase and decrease in profit
    if min_profit == 0:
        min_profit = profit
    elif profit < min_profit:
        min_profit = profit
    elif profit > max_profit:
        # profit -=1
        max_profit = profit
    
print("")
print(f"Financial Analysis")
print(f"--------------------------\n")
print(f"Total Months: {line_num}")
print(f"Total: ${total_profit}")
print(f"Greatest Increase in Profits: {max_profit}")
print(f"Greatest Decrease in Profits: {min_profit}")