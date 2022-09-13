"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 
Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
import string
def isPalindrome(s):
    alphabet = list(string.ascii_lowercase)
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    s_lower = s.lower()
    s_lower = s_lower.replace(" ", "")
    temp_s = s_lower
    for i in range(len(s_lower)):
        if s_lower[i] not in alphabet and s_lower[i] not in numbers:
            temp_s = temp_s.replace(s_lower[i], "")
    
    temp_s_r = temp_s[::-1]
    if temp_s_r == temp_s:
        return True
    return False

s = "0P"
result = isPalindrome(s)
print(result)