"""
Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.


Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Constraints:

0 <= s.length <= 105
s[i] is 'A', 'C', 'G', or 'T'.
"""
from collections import defaultdict

def findRepeatedDnaSequences(s):
    if len(s)<10:
        return []
    hash_table = defaultdict(int)
    for i in range(10, len(s)+1):
        temp_s = s[i-10:i]
        hash_table[temp_s] += 1
    answer = []
    for key in hash_table.keys():
        if hash_table[key] >= 2:
            answer.append(key)
    return answer


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
result = findRepeatedDnaSequences(s)
print(result)