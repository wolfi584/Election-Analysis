#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


# Assign a variable for the file to load and the path.
import csv
import os
# Assign a variable for the file to load and the path.
file_path = "Resources"
file_load_name = "election_results.csv"
file_save_name = "election_results.txt"

# Create a filename variable to a direct or indirect path to the file.
file_to_load = os.path.join(file_path, file_load_name)
file_to_save = os.path.join(file_path, file_save_name)

# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader function.
     file_reader = csv.reader(election_data)
#     for row in file_reader:
#         print(row)

# Read and print the header row.
     headers = next(file_reader)
     print(headers)