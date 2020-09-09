"""
Shuffle the Array


Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].


Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].


Constraints:

- 1 <= n <= 500
- nums.length == 2n
- 1 <= nums[i] <= 10^3

"""

def shuffle(nums, n):
    first_n, second_n = nums[:n], nums[n:]
    answer = []
    if len(nums) != (2 * n):
        return False
    elif n < 1 or n > 500:
        return False
    else:
        for i in range(len(first_n)):
            if first_n[i] < 1 or first_n[i] > 10 ** 3 or second_n[i] < 1 or second_n[i] > 10 ** 3:
                return False
            else:
                answer.append(first_n[i])
                answer.append(second_n[i])
    return answer

nums = [2, 5, 1, 3, 4, 7]
n = 3
result = shuffle(nums, n)
print(result)