"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 
Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

def setZeroes(matrix):
    zeros = []
    m = len(matrix)
    n = len(matrix[0])

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                zeros.append((row, col))
    
    for row, col in zeros:
        for new_col in range(n):
            matrix[row][new_col] = 0
        for new_row in range(m):
            matrix[new_row][col] = 0

    return matrix


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
result = setZeroes(matrix)
print(result)