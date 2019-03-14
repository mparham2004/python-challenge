import os
import csv
import pandas as pd

# Path to collect data from the folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')



with open(budget_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    totals = []
    for row_count, row in enumerate(csvreader, start=1):
        value = int(row['Profit/Losses'])
        totals.append(value)

#calculate a column showing differences by month, then get average, greatest increase and decrease



#use pandas to read data
budget_data_pd = pd.read_csv(budget_csv)



df = budget_data_pd['Profit/Losses']
monthly_change = df.diff()
average_change = df.diff().max()
budget_data_pd["monthly_change"] = monthly_change

print ("")
print ("Financial Analysis")
print ("-------------------------------")
print ("Total Months: {}".format(row_count))
print ("Total: ${}".format(sum(totals)))
print ("Average Change: $"+ str(round(monthly_change.mean(),2)))
print ("Greatest Increase in Profits: $" + str(monthly_change.max()) + " date")
print ("Greatest Decrease in Profits: $" + str(monthly_change.min())+ " date")



budget_data_pd.head()

with open("main_text_file.txt",'w',encoding = 'utf-8') as f:
   f.write("main_text_file\n")
   f.write("print path test")

   

