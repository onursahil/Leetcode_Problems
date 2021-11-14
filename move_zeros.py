"""
Given an integer array nums, move all 0's to the end of it while maintaining the 
relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]
 
Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""

def moveZeroes(nums):
    ptr1 = 0
    ptr2 = 1
    while ptr2 < len(nums):
        if nums[ptr1] != 0:
            ptr1 += 1
        elif nums[ptr2] != 0:
            nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
            ptr1 += 1
        ptr2 += 1

    return nums

nums = [0,1,0,3,12]
result = moveZeroes(nums)
print(result)