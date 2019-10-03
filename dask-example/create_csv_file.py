import random

file_name = "sample_data_set.csv"
random_number = 0

# specify the number of rows
r_size = 1000000

file_string = "UID,NUM_VALUE,NOTES\n"
f = open(file_name, "a")
f.write(file_string)

for _ in range(r_size):

    random_number = random.randint(1, 9999)
    file_string = f"{_},{random_number},The quick brown fox jumps over the lazy dog\n"

    print(file_string)

    f = open(file_name, "a")
    f.write(file_string)
