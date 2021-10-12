"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Example 3:

Input: nums = [1,1]
Output: 1

Example 4:

Input: nums = [1,1,2]
Output: 1

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
"""

def findDuplicate(nums):
    nums.sort()
    count_dict = {}
    for i in range(len(nums)):
        if nums[i] in count_dict.keys():
            return nums[i]
        else:
            count_dict[nums[i]] = 1

nums = [3,1,3,4,2]
result = findDuplicate(nums)
print(result)