"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0
 
Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
"""

from collections import Counter
def maxNumberOfBalloons(text):
    cnt = Counter(text)
    return min(cnt["b"], cnt["a"], cnt["l"]//2, cnt["o"]//2, cnt["n"])

text = "loonbalxballpoon"
text = "balllllllllllloooooooooon"
result = maxNumberOfBalloons(text)
print(result)