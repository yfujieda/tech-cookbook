import os
import random

r_size = int(10) # set the number of times you want to iterate
file_name = "sample_output_to_csv.csv" # file name to be used when saving as CSV file


# file_string value below will be stored as the first line in the CSV file
# first line is usually the header row
file_string = "UID,NUM_VALUE,NOTES\n" 

# use open() to initiate some action with the file
# "a" means append. You want to append the data instead of overwriting it
f = open(file_name, "a")

# write() to actually write the data into the file
f.write(file_string)

for _ in range(r_size):

    random_number = random.randint(1, 9999)

    # file_string below is representing the row
    file_string = f"{_},{random_number},The quick brown fox jumps over the lazy dog\n"

    # It opens the file assigned in file_name and it is preparing to "append" the data
    f = open(file_name, "a")

    # write() will store the data in file_string to CSV file
    f.write(file_string)
