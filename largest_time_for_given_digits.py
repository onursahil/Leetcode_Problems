"""

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.


Example 1:

Input: [1,2,3,4]
Output: "23:41"


Note:

- A.length == 4
- 0 <= A[i] <= 9

"""
from itertools import permutations 

def largestTimeFromDigits(A):
    A.sort(reverse=False)
    if all(x == 0 for x in A) :
        answer = '00:00'
        return answer
    first_p = [element for element in list(permutations(A, 2)) if element[0] < 3]
    print(first_p)
    if len(first_p) == 0:
        return ""
    for t in first_p[::-1]:
        f_cl = int(str(t[0]) + str(t[1]))
        print(f_cl)
        if f_cl > 23:
            continue
        elif str(f_cl) == '00' or str(f_cl) == '0':
            first_clock = str(f_cl)
            break
        else:
            first_clock = str(f_cl)
            if int(first_clock) < 24:
                a = t[0]
                print(a)
                b = t[1]
                break
            return ""

    A.remove(a)
    A.remove(b)

    print(first_clock)

    # second_p = [element for element in list(permutations(A, 2)) if element[0] < 6 and element[0] != a and element[0] != b and element[1] != a and element[1]!= b]
    second_p = [element for element in list(permutations(A, 2)) if element[0] < 6]
    if len(second_p) == 0:
        return ""

    second_clock = str(second_p[len(second_p) - 1][0]) + str(second_p[len(second_p) - 1][1])

    if len(first_clock) == 1:
        first_clock  = '0' + first_clock

    answer = first_clock + ":" + second_clock
    return answer


A = [4, 2, 4, 4]
result = largestTimeFromDigits(A)
print(result)