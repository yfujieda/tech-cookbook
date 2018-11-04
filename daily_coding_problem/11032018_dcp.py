'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

# given values
l = [10, 15, 3, 7]
k = 17

# will be used for recursion
l_len = len(l)

# do the work
def compute(a_list, k):
    
    # loop through the list
    for i in range(l_len):

        a_list_len = len(a_list)
        base_num = a_list[0]
        sum_num = 0

        # pop the first item in the list
        a_list.pop(0)

        # refresh the list without the first one
        a_list_len = len(a_list)

        for j in range(a_list_len):
            sum_num = base_num + a_list[j]
            # print(base_num, a_list, a_list_len, sum_num)

            if sum_num == k:
                # return the values used to match the k value
                return base_num, a_list[j]
    
    # return False if nothing matches.
    return False

r = compute(l, k)

if not r:
    print("there was no match!")
else:
    print(f'there was a match with k({k}), {r[0]} + {r[1]}')
