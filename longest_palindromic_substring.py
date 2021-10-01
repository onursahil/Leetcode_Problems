"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"

Example 4:

Input: s = "ac"
Output: "a"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

def longestPalindrome(s):
    if len(s) == 1:
        return s

    res = s[0]
    max_length=1
    for i in range(len(s)):
        for j in range(len(s)-1,i+max_length-1,-1):
            if s[i:j+1]==s[i:j+1][::-1]:
                max_length=j-i
                res=s[i:j+1]
                break
    
    return res


s = "cbbd"
result = longestPalindrome(s)
print(result)