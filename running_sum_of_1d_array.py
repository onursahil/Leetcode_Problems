"""

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


Constraints:

- 1 <= nums.length <= 1000
- -10^6 <= nums[i] <= 10^6

"""

def runningSum(nums):
    if len(nums) < 1 or len(nums) > 1000:
        return False

    answer = [sum(nums[:i+1]) for i in range(len(nums)) if nums[i] > -(10 ** 6) or nums[i] < 10 ** 6]

    return answer


nums = [3,1,2,10,1]
result = runningSum(nums)
print(result)