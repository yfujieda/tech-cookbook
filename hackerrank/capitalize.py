import os

def solve(s):

    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s

s = input()
result = solve(s)
print(result + '\n')
