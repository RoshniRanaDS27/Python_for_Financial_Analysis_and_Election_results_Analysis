import os
import csv

# Path to the CSV File
csv_file = 'PyPoll/resources/election_data.csv'

# Variables for analysis
total_votes = 0
candidates_votes = {}

# Read from the CSV file
with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip header row
    
    for row in csvreader:
        total_votes += 1  # Increment total votes for each row
        candidate_name = row[2]  # Assuming the candidate's name is in the third column
        
        # Count votes for each candidate
        if candidate_name in candidates_votes:
            candidates_votes[candidate_name] += 1
        else:
            candidates_votes[candidate_name] = 1

# Calculate voting percentage
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates_votes.items()}

# Determine the winner
winner = max(candidates_votes, key=candidates_votes.get)

# Print the analysis results
print("Election Results")
print("------------------")
print(f"Total Votes: {total_votes}")
print('-------------------')
for name, votes in candidates_votes.items():
    print(f"{name}: {percentages[name]:.2f}% ({votes})")
print('-------------------------')
print(f"Winner: {winner}")
print('----------------------------')

# Export results into a text file
output_file = 'PyPoll.txt'
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write('-------------------\n')
    for name, votes in candidates_votes.items():
        file.write(f"{name}: {percentages[name]:.2f}% ({votes})\n")
    file.write('-------------------------\n')
    file.write(f"Winner: {winner}\n")
    file.write('----------------------------')