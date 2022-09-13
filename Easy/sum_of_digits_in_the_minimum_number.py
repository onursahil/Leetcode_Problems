"""
Given an integer array nums, return 0 if the sum of the digits of the minimum integer 
in nums is odd, or 1 otherwise.

Example 1:

Input: nums = [34,23,1,24,75,33,54,8]
Output: 0
Explanation: The minimal element is 1, and the sum of those digits is 1 which is odd, so the answer is 0.

Example 2:

Input: nums = [99,77,33,66,55]
Output: 1
Explanation: The minimal element is 33, and the sum of those digits is 3 + 3 = 6 which is even, so the answer is 1.

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

def sumOfDigits(nums):
    total = 0
    for i in range(len(str(min(nums)))):
        total += int(str(min(nums))[i])

    if total % 2 == 0:
        return 1
    else:
        return 0

nums = [34,23,1,24,75,33,54,8]
result = sumOfDigits(nums)
print(result)