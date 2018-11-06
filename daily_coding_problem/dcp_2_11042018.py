'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

given_list = [1, 2, 3, 4, 5]


def compute(a_list):
    new_list = []

    for index, value in enumerate(a_list):
        original_list = a_list
        original_int = original_list[index]
        original_list[index] = 1

        result = 1
        for x in original_list:
            result = result * x

        new_list.append(result)

        original_list[index] = original_int

    return new_list

r = compute(given_list)
print(r)
