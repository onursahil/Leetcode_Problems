"""
Maximum Product Subarray


Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.


Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.


Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""

def maxProduct(nums):
    result = nums[0]
    minimum = nums[0]
    maximum = nums[0]

    for num in nums[1:]:
        temp_max = maximum
        temp_min = minimum
        maximum = max(max(temp_max * num, temp_min * num), num)
        minimum = min(min(temp_max * num, temp_min* num), num)
        result = max(result, maximum)

    return result


nums = [-2,3,-4]
result = maxProduct(nums)
print(result)