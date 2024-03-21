import csv
import os

# Variables for analysis
total_votes = 0
candidates = {}

# Specify the path to the output folder
output_folder = r"c:\Users\ranar\Downloads\UTOR-VIRT-DATA-PT-02-2024-U-LOLC\Module 3 - Python\Python-Challenge\PyPoll\Analysis"

# Read from the file (assuming the provided data is saved in this file)
input_file_path = 'C:/Users/ranar/Downloads/UTOR-VIRT-DATA-PT-02-2024-U-LOLC/Module 3 - Python/Python-Challenge/PyPoll/resources/election_data.csv'

# Read from the file (assuming the provided data is saved in this file)
with open('C:/Users/ranar/Downloads/UTOR-VIRT-DATA-PT-02-2024-U-LOLC/Module 3 - Python/Python-Challenge/PyPoll/resources/election_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    
    for row in reader:
        total_votes += 1  # Increment total votes for each row
        candidate_name = row[2]  # Assuming the candidate's name is in the third column
        
        # Count votes for each candidate
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Determine the winner
winner = max(candidates, key=candidates.get)

output_file_path = os.path.join(output_folder, 'election_results.txt')

# Print and save the analysis
with open(output_file_path, 'w') as output_file:
    output = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    
    print(output, end="")
    output_file.write(output)
    
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        candidate_results = f"{candidate}: {percentage:.3f}% ({votes})\n"
        
        print(candidate_results, end="")
        output_file.write(candidate_results)
    
    winner_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n"
    )
 
    print(winner_summary)
    output_file.write(winner_summary)
    
print(f"Election results have been exported to {output_file_path}.")