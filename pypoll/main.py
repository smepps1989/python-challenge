import os
import csv

# Define path to file
file_path = os.path.join('Resources', 'election_data.csv')

# open csv and read into an empty dictionary
voter_results = {}
with open(file_path, 'r') as file:
    text = csv.reader(file, delimiter=',')
    next(text)
    for row in text:
        voter_results[row[0]] = row[2]

total_votes = len(voter_results)

# find set of unique candidates similar to what is described on stack overflow.com (https://stackoverflow.com/questions/17218139/print-all-unique-values-in-a-python-dictionary#17218164)
candidates = set(voter_results.values())

# create dictionary with voter results and find number of votes given to each candidate
candidate_results = {}
for candidate in candidates:
    counter = 0
    for value in voter_results.values():
        if value == candidate:
            counter += 1
    candidate_results[candidate] = counter

# Election Results
print(f'Election Results')
print(f'Total Votes: {total_votes}')

# Find counts cast for each candidate and find the winner
for candidate in candidate_results.keys():
    num_votes = candidate_results[candidate]
    percent_total = round((num_votes / total_votes * 100) , 3)
    if num_votes == max(candidate_results.values()):
        winner = candidate
    print(f'{candidate}: {percent_total}% ({candidate_results[candidate]})')
print(f'Winner: {winner}!')

# Export results to analysis folder
newfile_path = os.path.join('analysis', 'results.csv')

with open(newfile_path, 'w') as newfile:
    writer = csv.writer(newfile, delimiter=',')
    writer.writerow(['Candidate', 'Percent of Votes', 'Number of votes'])
    for candidate in candidate_results.keys():
        num_votes = candidate_results[candidate]
        percent_total = round((num_votes / total_votes * 100) , 3)
        writer.writerow([f'{candidate}, {percent_total}%, {num_votes}'])
    writer.writerow([f'Winner: {winner}'])