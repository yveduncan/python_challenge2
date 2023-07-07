# create file paths across operating systems
import os

# Module for reading CSV files
import csv
from pickle import APPEND

# identify file path
csvpath1 = os.path.join('Resources', 'budget_data.csv')

# open file
with open(csvpath1) as csvfile: 
  reader = csv.reader(csvfile)

# Read each row of data after the header
  for row in reader:
    print("Total Months:", len(list(reader)))

# open file
with open(csvpath1) as csvfile: 
  reader = csv.reader(csvfile)

# Read the total amount for column B
  total = 0
  next(reader)
  for row in reader:
    total += int(row[1])
    total_str = str(total)
  print("Total: $", total_str)

# identify file path 2
csvpath2 = os.path.join('Resources', 'budget_data_modified.csv')

# open file in reader mod
with open(csvpath1, mode='r') as file:
# read contents
  reader = csv.reader(file)
# extract header row from csv
  header = next(reader)
# append new column
  header.append('Changes')

# open file in writer mode
with open(csvpath2, mode='w', newline='') as new_file:
# create csv writer
  csv_writer = csv.writer(new_file)
  # write the header row to the new csv file
  csv_writer.writerow(header)

with open(csvpath1, mode='r') as infile:
    reader = csv.reader(infile)
    header = next(reader)

    with open(csvpath2, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)

        # Write header row
        writer.writerow(header)

        # Write data rows
        for row in reader:
            profit_losses = int(row[1])
            writer.writerow(row + [profit_losses])

        # Calculate and write sum of profit/losses column
        infile.seek(0)
        next(reader)  # Skip header row
        sum_of_profit_losses = sum(int(row[1]) for row in reader)
        writer.writerow(['', sum_of_profit_losses])

# import csv
import csv
# import os
import os

# identify file path 2
csvpath2 = os.path.join('Resources', 'budget_data_modified.csv')

# open file in read mode
with open(csvpath2, mode='r') as file:

  #skip the header
  reader = csv.reader(file)
  header = next(reader)

  # create empty list
  data = []
  # loop through each row
  for row in reader:
    # extract data and covert to float
    data.append(float(row[1]))

    # create empty list called "Changes"
    changes = []
    for i in range(1, len(data)):
       changes.append(data[i] - data[i-2])

with open(csvpath2, mode='r') as file:
  reader = csv.reader(file)
  rows = [row for row in reader]

with open(csvpath2, mode='w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(header + ['Changes'])

  for i in range(1, len(rows)):
      writer.writerow(rows[i] + [changes[i-2]])
      

