"""
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.

Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from itertools import accumulate

def maxAbsoluteSum_optimized(nums):
    return max(accumulate(nums, initial=0)) - min(accumulate(nums, initial=0))

def maxAbsoluteSum(nums):
    def allSubArrays(L,L2=None):
        if L2==None:
            L2 = L[:-1]
        if L==[]:
            if L2==[]:
                return []
            return allSubArrays(L2,L2[:-1])
        return [L]+allSubArrays(L[1:],L2)

    sub_arrays = allSubArrays(nums)

    maximum = 0
    for arr in sub_arrays:
        total = abs(sum(arr))
        if total > maximum:
            maximum = total

    return maximum


nums = [1,-3,2,3,-4]
result = maxAbsoluteSum(nums)
result_optimized = maxAbsoluteSum_optimized(nums)
print(result_optimized, result_optimized)