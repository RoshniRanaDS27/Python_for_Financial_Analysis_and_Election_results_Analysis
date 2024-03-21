import os
import pandas as pd

# Specify the full path to the CSV file
file_path = "C:/Users/ranar/Downloads/UTOR-VIRT-DATA-PT-02-2024-U-LOLC/Module 3 - Python/Python-Challenge/PyBank/Resources/budget_data.csv"

# Read the CSV file using pandas
df = pd.read_csv(file_path)

# Calculate financial metrics
total_months = len(df)
total_profit_losses = df["Profit/Losses"].sum()
changes = df["Profit/Losses"].diff()
average_change = changes.mean()
greatest_increase = changes.max()
greatest_increase_date = df.loc[changes.idxmax(), "Date"]
greatest_decrease = changes.min()
greatest_decrease_date = df.loc[changes.idxmin(), "Date"]

# Print the financial analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Specify the path to the output folder
output_folder = r"C:\Users\ranar\Downloads\UTOR-VIRT-DATA-PT-02-2024-U-LOLC\Module 3 - Python\Python-Challenge\PyBank\Analysis"

# Export results to a text file in the output folder
output_file = os.path.join(output_folder, "financial_analysis.txt")
with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print(f"Financial analysis results have been exported to {output_file}.")