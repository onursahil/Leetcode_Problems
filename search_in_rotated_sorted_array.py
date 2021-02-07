"""
You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.
Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
If target is found in the array return its index, otherwise, return -1.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1
 
Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
"""

def search(nums, target):
    if target in nums[:len(nums)//2]:
        return nums[:len(nums)//2].index(target)
    elif target in nums[len(nums)//2:]:
        return len(nums[:len(nums)//2]) + nums[len(nums)//2:].index(target)
    else:
        return -1

nums, target = [4,5,6,7,0,1,2], 0
result = search(nums, target)
print(result)