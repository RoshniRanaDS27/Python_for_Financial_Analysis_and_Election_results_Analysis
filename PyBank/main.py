import os
import csv

csv_file = r'PyBank/Resources/budget_data.csv'

#setup variables
date = []
total_sum = 0
count = 0
column_index = 1
previous_value = None
total_change = 0
tally = 0
greatest_inc = 0
greatest_dec = 0
month_greatest_inc = ''
month_greatest_dec = ''
previous_profit = None


#open csv
with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        date.append(row[0]) # here we are appending date frmo current row to the list
        value = int(row[1]) # Converting profit/loss column to integer and summing them up
        total_sum += value
        count += 1
        if previous_profit is not None:
            change = value - previous_profit
            total_change += change
            tally += 1
#calc greatest inc & dec
            if change > greatest_inc:
                greatest_inc = change
                month_greatest_inc = row[0]
            elif change<greatest_dec:
                greatest_dec = change
                month_greatest_dec = row[0]
        previous_profit = value
#calculate the total months
total_months = len(date)
#calculate the average
if tally > 0:
    avg_change = total_change/ tally
else:
     avg_change = 0

#print the output
print("Financial Analysis")
print("------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_sum}')
print(f'Average Change: {avg_change:.2f}')
print(f'Greatest Increase in Profits: {month_greatest_inc}(${greatest_inc})')
print(f'Greatest Decrease in Profits: {month_greatest_dec}(${greatest_dec})')

#Export results to text file
output_file = "Pybank.txt"
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------------------\n")
    file.write(f'Total Months: {total_months}\n')
    file.write(f'Total: ${total_sum}\n')
    file.write(f'Average Change: ${avg_change:.2f}\n')
    file.write(f'Greatest Increase in Profits: {month_greatest_inc}(${greatest_inc})\n')
    file.write(f'Greatest Decrease in Profits: {month_greatest_dec}(${greatest_dec})\n')
print(f'Results have been saved to {output_file}')