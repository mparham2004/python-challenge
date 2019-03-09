test
import os
import csv

# Path to collect data from the folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')


with open(budget_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    totals = []
    for row_count, row in enumerate(csvreader, start=1):
        value = int(row['Profit/Losses'])
        totals.append(value)

#calculate a column showing differences by month, then get average, greatest increase and decrease
differences = 

print ("")
print ("Financial Analysis")
print ("-------------------------------")
print ("Total Months: {}".format(row_count))
print ("Total: ${}".format(sum(totals)))
print ("Average Change: $")
print ("Greatest Increase in Profits: $")
print ("Greatest Decrease in Profits: $")
