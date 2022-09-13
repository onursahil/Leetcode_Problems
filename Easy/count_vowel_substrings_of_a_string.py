"""
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') 
and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.

Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"

Example 2:

Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.

Example 3:

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"

Example 4:

Input: word = "bbaeixoubb"
Output: 0
Explanation: The only substrings that contain all five vowels also contain consonants, so there are no vowel substrings.
 
Constraints:

1 <= word.length <= 100
word consists of lowercase English letters only.
"""

def countVowelSubstrings(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    length = len(word)
    count = 0
    substrings = [word[i:j+1] for i in range(length) for j in range(i,length) if len(word[i:j+1]) >= 5]

    for sub in substrings:
        vowels_dict = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        for char in sub:
            if char in vowels:
                vowels_dict[char] += 1
        
        vowel_count = vowels_dict.values()
        if 0 in vowel_count:
            continue
        else:
            if sum(vowel_count) == len(sub):
                count += 1

    return count


word = "aeiouu"
result = countVowelSubstrings(word)
print(result)