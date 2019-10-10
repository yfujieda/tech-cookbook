def split_and_join(line):
    a = line.split(" ")
    a = "-".join(a)
    return a

line = input()
result = split_and_join(line)
print(result)
