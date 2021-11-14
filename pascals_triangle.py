"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

Constraints:

1 <= numRows <= 30
"""

def generate(numRows):
    x = [1]
    y = []
    
    if numRows == 1:
        y.append(x)
        return y
    if numRows == 2:
        y.append(x)
        y.append(x * 2)
        return y
    y.append(x)
    y.append(x * 2)
    
    for i in range(3, numRows + 1):
        z = x * i
        for j in range(1, len(z) - 1):
            z[j] = y[len(z) - 2][j - 1] + y[len(z)-2][j]
        y.append(z)
    
    return y

numRows = 5
result = generate(numRows)
print(result)