"""
The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s, which is then converted into an integer.

For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get 21.
You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' inclusive.

Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord, or false otherwise.

Example 1:

Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
Output: true
Explanation:
The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.

Example 2:

Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
Output: false
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aab" -> "001" -> 1.
We return false because 0 + 0 != 1.

Example 3:

Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
Output: true
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aaaa" -> "0000" -> 0.
We return true because 0 + 0 == 0.

Constraints:

1 <= firstWord.length, secondWord.length, targetWord.length <= 8
firstWord, secondWord, and targetWord consist of lowercase English letters from 'a' to 'j' inclusive.
"""
import string

def isSumEqual(firstWord, secondWord, targetWord):
    # alphabet = string.ascii_lowercase

    # firstStr, secondStr, targetStr = "", "", ""
    
    # for i in range(len(firstWord)):
    #     firstStr += str(alphabet.index(firstWord[i]))
    # firstInt = int(firstStr)

    # for i in range(len(secondWord)):
    #     secondStr += str(alphabet.index(secondWord[i]))
    # secondInt = int(secondStr)

    # for i in range(len(targetWord)):
    #     targetStr += str(alphabet.index(targetWord[i]))
    # targettInt = int(targetStr)

    # if (firstInt + secondInt) == targettInt:
    #     return True
    # else:
    #     return False

    dic = {'a':'0','b':'1','c':'2','d':'3','e':'4','f':'5','g':'6','h':'7','i':'8','j':'9'}
    w1,w2,wt = '','',''
    for item in firstWord:
        w1 += dic[item]
    for item in secondWord:
        w2 += dic[item]
    for item in targetWord:
        wt += dic[item]

    if int(w1) + int(w2) == int(wt):
        return True
    else:
        return False

firstWord, secondWord, targetWord = "acb", "cba", "cdb"
result = isSumEqual(firstWord, secondWord, targetWord)
print(result)