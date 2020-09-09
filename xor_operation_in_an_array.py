"""
XOR Operation in an Array


Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

 

Example 1:

Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.


Constraints:

- 1 <= n <= 1000
- 0 <= start <= 1000
- n == nums.length

"""

from functools import reduce

def xorOperation(n, start):
    nums = []
    for i in range(n):
        nums.append(start + (2 * i))

    answer = reduce(lambda i, j: int(i) ^ int(j), nums)
    
    return answer

n, start = 10, 5
result = xorOperation(n, start)
print(result)