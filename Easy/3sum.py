"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

def threeSum(nums):
    if len(nums) <= 2:
        return []

    nums.sort()
    result = []
    seen = {}

    for i in range(len(nums)):
        if nums[i] in seen:
            continue
            
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]

        while left < right:
            calculated = nums[left] + nums[right]
            if target == calculated:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            
                while (left < len(nums) and nums[left] == nums[left - 1]):
                    left += 1
                
                while (right > 0 and nums[right] == nums[right + 1]):
                    right -= 1
            
            elif calculated < target:
                left += 1
            else:
                right -= 1
            
        seen[nums[i]] = True
    

    return result


nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)
print(result)