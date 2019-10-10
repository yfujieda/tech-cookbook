students = []
score_list = []

for _ in range(int(input())):

    temp = []

    name = input()
    score = float(input())

    temp.append(name)
    temp.append(score)

    score_list.append(score)
    students.append(temp)

# remove duplicate scoring and sort the score list from low to high
score_list = list(dict.fromkeys(score_list))
score_list.sort()

# check if the list has 2 or more records
if len(students) >= 2:
    
    # placeholder for second lowest score student
    second_lowest_students = []

    # get the second lowest score student based on the score list's index 1
    second_lowest_score = score_list[1]

    # loop through the student's list
    for i in students:

        print(i)
        # check if there is a match between second lowest score student and student in the student list
        if second_lowest_score in i:

            # append the student in the second_lowest_students list
            # if there is more than 1, it will add to the list as well
            second_lowest_students.append(i[0])
        else:
            pass

    # it will sort the final list of second_lowest_students in alphabetical order.
    # then print out in separate line.
    print('\n'.join(sorted(second_lowest_students, key=lambda second_lowest_students: second_lowest_students)))

else:
    print(students[0][0])
