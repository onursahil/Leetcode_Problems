"""
Split a String in Balanced Strings

Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

"""

def balancedStringSplit(s):
    R = 0
    L = 0
    count = 0
    for char in s:
        if char == "R":
            R += 1
        else:
            L += 1
        if R == L:
            count += 1
            R = 0
            L = 0

    return count


s = "RLRRRLLRLL"
result = balancedStringSplit(s)
print(result)