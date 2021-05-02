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
file_name = "election_results.csv"

file_to_load = os.path.join(file_path, file_name)
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)


file_path = "Resources"
file_name = "election_results.txt"

     # Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join(file_path, file_name)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file.
     txt_file.write("Arapahoe, ")
     txt_file.write("Denver, ")
     txt_file.write("Jefferson")
     txt_file.write("\n\n")
     txt_file.write("Arapahoe\nDenver\nJefferson")