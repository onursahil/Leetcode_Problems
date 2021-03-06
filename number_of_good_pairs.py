"""
Number of Good Pairs


Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.


Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.


Constraints:

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

"""

def numIdenticalPairs(nums):
    answer = 0
    if len(nums) < 1 or len(nums) > 100:
        return False
    else:
        for i in range(len(nums) - 1):
            if nums[i] < 1 or nums[i] > 100:
                return False
            else:
                answer += nums[i + 1:].count(nums[i])
    return answer


nums = [1,1,1,1]
result = numIdenticalPairs(nums)
print(result)