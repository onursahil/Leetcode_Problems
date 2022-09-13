"""
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.
An alphanumeric string is a string consisting of lowercase English letters and digits.

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""

def secondHighest(s):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    char_list = list(s)
    integers = []

    for i in range(len(char_list)):
        if char_list[i] in nums:
            integers.append(int(char_list[i]))
    
    integers_set = list(set(integers))
    integers_set.sort(reverse=True)

    if len(integers_set) <= 1:
        return -1
    else:
        return integers_set[1]


s = "dfa12321afd"
# s = "abc1111"
# s = "ck077"
result = secondHighest(s)
print(result)