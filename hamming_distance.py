"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:

Input: x = 3, y = 1
Output: 1
 
Constraints:

0 <= x, y <= 231 - 1
"""

def hammingDistance(x, y):
    x_bit_string = ''.join(str(1 & x >> i) for i in range(32)[::-1])
    y_bit_string = ''.join(str(1 & y >> i) for i in range(32)[::-1])
    
    return sum(x_bit_string[i] != y_bit_string[i] for i in range(len(x_bit_string)))

x, y = 3, 1
result = hammingDistance(x, y)
print(result)