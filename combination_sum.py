"""
Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.


Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []

Example 4:

Input: candidates = [1], target = 1
Output: [[1]]

Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]

"""

def combinationSum(candidates, target):
    result = []
    candidates.sort(reverse=True)

    def generate(remains=target, combination=[]):
        if remains < 0:
            return
        if not remains:
            result.append(combination)
            return
        
        last_used = combination[-1] if combination else candidates[0]

        for c in candidates:
            if c > last_used:
                continue
            generate(remains - c, combination + [c])
    
    generate()
    return result


candidates = [2, 3, 6, 7]
target = 7
result = combinationSum(candidates, target)
print(result)