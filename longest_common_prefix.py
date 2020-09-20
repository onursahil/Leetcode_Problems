"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

from collections import Counter

def longestCommonPrefix(strs):
    common_prefix = ""
    try:
        min_length = min([len(word) for word in strs])
    except:
        return common_prefix
    
    index = 1
    for i in range(min_length):
        temp_list = [word[:index] for word in strs]
        
        if len(set(temp_list)) == 1:
            index += 1
        else:
            break
    
    count = index - 1
    if count != 0:
        common_prefix = strs[0][:count]
    else:
        pass
    
    return common_prefix


strs = ["flower","flow","flight"]
result = longestCommonPrefix(strs)
print(result)