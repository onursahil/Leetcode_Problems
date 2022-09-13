"""
A permutation perm of n + 1 integers of all the integers in the range [0, n] 
can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. 
If there are multiple valid permutations perm, return any of them.

Example 1:

Input: s = "IDID"
Output: [0,4,1,3,2]

Example 2:

Input: s = "III"
Output: [0,1,2,3]

Example 3:

Input: s = "DDI"
Output: [3,2,0,1]
 
Constraints:

1 <= s.length <= 105
s[i] is either 'I' or 'D'.
"""

def diStringMatch(s):
    low, high = 0, len(s)
    perm = []
    for char in s:
        if char == "I":
            perm.append(low)
            low += 1
        if char == "D":
            perm.append(high)
            high -= 1
    
    return perm + [low]

s = "DDI"
result = diStringMatch(s)
print(result)