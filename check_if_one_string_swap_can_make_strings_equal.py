"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose 
two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

Example 4:

Input: s1 = "abcd", s2 = "dcba"
Output: false

Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""

def areAlmostEqual(s1, s2):
    if s1 == s2:
        return True
    
    def swap(c, i, j):
        c = list(c)
        c[i], c[j] = c[j], c[i]
        return ''.join(c)

    s1_chars = list(set(s1)).sort()
    s2_chars = list(set(s2)).sort()

    if s1_chars == s2_chars:
        for i in range(len(s1)):
            for j in range(i + 1, len(s1)):
                temp = swap(s1, i, j)
                if temp == s2:
                    return True
                else:
                    continue
    else:
        return False

    return False



s1, s2 = "attack", "defend"
result = areAlmostEqual(s1, s2)
print(result)