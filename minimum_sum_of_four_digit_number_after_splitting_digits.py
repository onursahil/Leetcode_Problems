"""
You are given a positive integer num consisting of exactly four digits. 
Split num into two new integers new1 and new2 by using the digits found in num. 
Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. 
Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.

Example 1:

Input: num = 2932
Output: 52
Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.

Example 2:

Input: num = 4009
Output: 13
Explanation: Some possible pairs [new1, new2] are [0, 49], [490, 0], etc. 
The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.

Constraints:

1000 <= num <= 9999
"""

def minimumSum(num):
    sorted_nums = sorted([int(i) for i in list(str(num))])
    new_1 = str(sorted_nums[0]) + str(sorted_nums[2])
    new_2 = str(sorted_nums[1]) + str(sorted_nums[3])
    
    return int(new_1) + int(new_2)
        
num = 4009
result = minimumSum(num)
print(result)