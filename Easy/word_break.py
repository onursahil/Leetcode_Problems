"""
Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.


Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

"""

def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    lookup_table = [False for i in range(len(s)+1)]
    lookup_table[0] = True
    
    for i in range(1,len(s)+1):
        for j in range(i):
            if lookup_table[j] and s[j:i] in wordSet:
                lookup_table[i]=True
                break
    return lookup_table[-1]


s = "cars"
wordDict = ["car","ca","rs"]
result = wordBreak(s, wordDict)
print(result)