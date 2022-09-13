"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

Example 1:

Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

Example 2:

Input: left = 47, right = 85
Output: [48,55,66,77]

Constraints:

1 <= left <= right <= 104
"""

def selfDividingNumbers(left, right):
    num_range = range(left, right + 1)
    answer = []
    for num in num_range:
        num_digits = list(str(num))
        if '0' in num_digits:
            continue
        div_count = 0
        for digit in num_digits:
            if num % int(digit) != 0:
                continue
            else:
                div_count += 1
        if div_count == len(num_digits):
            answer.append(num)

    return answer

left, right = 47, 85
result = selfDividingNumbers(left, right)
print(result)