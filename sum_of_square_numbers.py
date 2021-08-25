"""
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: c = 3
Output: false

Example 3:

Input: c = 4
Output: true

Example 4:

Input: c = 2
Output: true

Example 5:

Input: c = 1
Output: true
 
Constraints:
0 <= c <= 231 - 1
"""

def judgeSquareSum(c):
    hashset = set()
    for i in range(int(c ** (1/2)) + 1):
        hashset.add(i * i)

    for xSquare in hashset:
        if c - xSquare in hashset:
            return True
    return False

c = 1000
result = judgeSquareSum(c)
print(result)