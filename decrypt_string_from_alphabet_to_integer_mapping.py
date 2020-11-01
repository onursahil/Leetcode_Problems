"""
Decrypt String from Alphabet to Integer Mapping

Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.


Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"

Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
 

Constraints:

- 1 <= s.length <= 1000
- s[i] only contains digits letters ('0'-'9') and '#' letter.
- s will be valid string such that mapping is always possible.
"""

import string
def freqAlphabets(s):
    answer = []
    alphabet = list(string.ascii_lowercase)
    first_part = dict(zip(["1", "2", "3", "4", "5", "6", "7", "8", "9"], alphabet[0:10]))
    second_part = dict(zip(["10#", "11#", "12#", "13#", "14#", "15#", "16#", "17#", "18#", "19#", "20#", "21#", "22#", "23#", "24#", "25#", "26#"], alphabet[9:]))
    first_part.update(second_part)

    i = 0
    while i < len(s):
        if (i + 2) < len(s) and s[i + 2] == "#":
            answer.append(first_part[''.join(s[i] + s[i + 1] + s[i + 2])])
            i += 3
        else:
            answer.append(first_part[s[i]])
            i += 1

    return ''.join(answer)

s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
result = freqAlphabets(s)
print(result)