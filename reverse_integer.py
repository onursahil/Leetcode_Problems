"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Example 4:

Input: x = 0
Output: 0
 
Constraints:

-231 <= x <= 231 - 1
"""

def reverse(x):
    ans_list = []
    ans = 0
    
    neg = x < 0
    x = abs(x)
    
    while x >= 10:
        remainder = x % 10
        ans_list.append(remainder)
        x //= 10

    ans_list.append(x)

    for i in range(len(ans_list)):
        ans += ans_list[-1-i] * (10 ** i)

    ans = ans if not neg else -ans
    if ans > (2 ** 31) - 1:
        return 0
    if ans < -(2 ** 31):
        return 0
    return ans 

x = -2147483648
result = reverse(x)
print(result)