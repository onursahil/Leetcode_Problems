"""
Shuffle String


Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.


Example 1:

Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.

Example 2:

Input: s = "aiohn", indices = [3,1,4,2,0]
Output: "nihao"


Constraints:

- s.length == indices.length == n
- 1 <= n <= 100
- s contains only lower-case English letters.
- 0 <= indices[i] < n
- All values of indices are unique (i.e. indices is a permutation of the integers from 0 to n - 1).

"""

def restoreString(s, indices):
    if len(s) != len(indices) or s.isupper():
        return False
    else:
        answer = []
        for i in range(len(indices)):
            idx = indices.index(i)
            answer.append(s[idx])
    answer = ''.join(answer)
    return answer


s = "aaiougrt"
indices = [4,0,2,6,7,3,1,5]
result = restoreString(s, indices)
print(result)