#1 Data that needs to be retrieved
#2 Total number of votes cast
#3 A complete list of candidates who received votes
#4  Total number of votes each candidate received
#5 Percentage of votes each candidate won
#6 The winner of the election based on popular vote

file_to_load = 'Resources/election_results.csv'
# election_data = open(file_to_load, 'r')
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# election_data = open(file_to_load, 'r')
# # Open the election results and read the file
# with open(file_to_load) as election_data:
#     print(election_data)
#     import os
    
#     os.path.join()
#     print(dir(os))

#     #path and join do NOT WORK.  WHY?
#     file_to_load = os.path.join("Resources", "election_results.csv")

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

# Write some data to the file.
    #txt_file.write("Hello World")



# # Write three counties to the file.
#     txt_file.write("Arapahoe, ")
#     txt_file.write("Denver, ")
#     txt_file.write("Jefferson")
   
   # Write three counties to the file.
    #txt_file.write("Arapahoe\nDenver\nJefferson")

    # Read the file object with the reader function.
    #file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
       # Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers) 