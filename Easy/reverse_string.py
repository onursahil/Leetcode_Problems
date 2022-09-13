"""
Write a function that reverses a string. The input string is given as an array of characters s. 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
import math
def reverseString(s):
    for i in range(math.floor((len(s) - 1) / 2)):
        tmp = s[i]
        s[i] = s[len(s)-1-i]
        s[len(s)-1-i] = tmp

    return s

    """
    In-Place Solution

    i=0
    j=len(s)-1
    while i<j:
        temp=s[i]
        s[i]=s[j]
        s[j]=temp
        i+=1
        j-=1
    """

s = ["h","e","l","l","o"]
s = ["H","a","n","n","a","h"]
result = reverseString(s)
print(result)