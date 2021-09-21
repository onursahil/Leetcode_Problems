"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

def findMaxConsecutiveOnes(nums):
    nums_str = "".join(str(num) for num in nums)
    splitted_nums_str = nums_str.split("0")

    maximum = 0
    for sub in splitted_nums_str:
        if len(sub) > maximum:
            maximum = len(sub)

    return maximum

# nums = [1,0,1,1,0,1]
# nums = [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0]
# nums = [1, 1, 0, 1, 1, 1]
nums = [1]
result = findMaxConsecutiveOnes(nums)
print(result)