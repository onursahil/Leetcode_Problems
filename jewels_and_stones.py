"""

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".


Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3


Note:

- S and J will consist of letters and have length at most 50.
- The characters in J are distinct.

"""

def numJewelsInStones(J, S):
    answer = 0
    for i in range(len(J)):
        answer += S.count(J[i])
    return answer


J = "aA"
S = "aAAbbbb"

# J = "z"
# S = "ZZ"

result = numJewelsInStones(J, S)
print(result)