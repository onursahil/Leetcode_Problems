"""
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

Example 2:

Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""

def areOccurrencesEqual(s):
    count_dict = {}

    for i in range(len(s)):
        if s[i] not in count_dict:
            count_dict[s[i]] = 1
        else:
            count_dict[s[i]] += 1
    
    if len(list(set(count_dict.values()))) == 1:
        return True
    else:
        return False

s = "aaabb"
result = areOccurrencesEqual(s)
print(result)