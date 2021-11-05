"""
Given a string s, return the number of substrings that have only one distinct letter.

Example 1:

Input: s = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.

Example 2:

Input: s = "aaaaaaaaaa"
Output: 55

Constraints:

1 <= s.length <= 1000
s[i] consists of only lowercase English letters.
"""

def countLetters(s):
    cnt = 1
    ans = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            ans += (cnt + 1) * cnt // 2
            cnt = 1
    
    return ans + (cnt + 1) * cnt // 2


s = "aaaaaaaaaa"
result = countLetters(s)
print(result)