"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""

from collections import Counter
def firstUniqChar(s):
    count_dict = dict(Counter(s))
    for key, value in count_dict.items():
        if value == 1:
            return s.index(key)

    return -1

s = "leetcode"
result = firstUniqChar(s)
print(result)