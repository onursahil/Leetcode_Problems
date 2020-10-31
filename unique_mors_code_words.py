"""
Unique Mors Code Words

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

Note:

- The length of words will be at most 100.
- Each words[i] will have length in range [1, 12].
- words[i] will only consist of lowercase letters.
"""

import string
def uniqueMorseRepresentations(words):
    alphabet = list(string.ascii_lowercase)
    mors_alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    mors_hash = dict(zip(alphabet, mors_alphabet))

    mors_repr = []
    for word in words:
        word_list = list(word)
        mors_transformed = "".join([mors_hash[word_list[i]] for i in range(len(word_list))])
        mors_repr.append(mors_transformed)

    unique_transforms = list(set(mors_repr))
    answer = len(unique_transforms)

    return answer

words = ["gin", "zen", "gig", "msg"]
result = uniqueMorseRepresentations(words)
print(result)