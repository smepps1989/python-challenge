import os
import csv

filepath = os.path.join('Resources', 'budget_data.csv')

# Create dictionary with month amd profit/loss information
budget_dict = {}
with open(filepath, 'r') as file:
    text = csv.reader(file, delimiter=',')
    next(text)
    for row in text:
        budget_dict[row[0]] = int(row[1])

# Find profit/loss difference between the months and store that into a dictionary
budget_diff = {}
previous_value = 0
current_value = 0
for key, value in budget_dict.items():
    current_value = budget_dict[key]
    difference = current_value - previous_value
    budget_diff[key] = difference
    previous_value = budget_dict[key]

# Create list to do average calculations while ecluding first value
budget_list = []
for value in budget_diff.values():
    budget_list.append(value)

# Find the largest profit, largest loss values for the analysis
total_months = len(budget_dict)
total_profits_losses = sum(budget_dict.values())
# ignore first month's entry because that is the starting point and will have no difference
avg_change = round(sum(budget_list[1:])/(len(budget_list) - 1),2)
largest_increase = max(budget_diff.values())
largest_loss = min(budget_diff.values())

# Print requested values to terminal
print('Financial Analysis for pyBank: ')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profits_losses}')
print(f'Average Change: ${avg_change}')
for key, value in budget_diff.items():
    if budget_diff[key] == largest_increase:
        print(f'Greatest Increase in Profits: {key} (${value})')
        
for key2, value2 in budget_diff.items():
    if budget_diff[key2] == largest_loss:
        print(f'Greatest Decrease in Profits: {key2} (${value2})')

# Export results to analysis folder
writing_path = os.path.join('analysis', 'results.csv')
with open(writing_path, 'w') as newfile:
    writer = csv.writer(newfile, delimiter=',')
    writer.writerow(['Total Months', 'Total', 'Average Change', 'Greatest Increase in Profits', 'Greatest Decrease in Profits'])
    writer.writerow([f'{total_months}, ${total_profits_losses}, ${avg_change}, ${largest_increase}, ${largest_loss}'])