"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:

Input: haystack = "", needle = ""
Output: 0
"""

def strStr(haystack, needle):
    # return haystack.find(needle)
    for i in range(len(haystack) - len(needle)):
        if needle in haystack[i:i+len(needle)]:
            return i
    return -1
    
    # return True

haystack, needle = "hello", "ll"
result = strStr(haystack, needle)
print(result)