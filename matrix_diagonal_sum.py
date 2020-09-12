"""
Matrix Diagonal Sum


Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.


Example 1:

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.


Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

"""

def diagonalSum(mat):
    remaining = len(mat) // 2
    mat_len = len(mat)
    total = 0
    if mat_len % 2 == 0:
        left_mat = mat[:remaining-1]
        right_mat = mat[remaining+1:][::-1]
        middle = mat[remaining-1:remaining+1]
        for i in range(len(middle)):
            middle_l = middle[i]
            total += middle_l[len(middle_l) // 2] + middle_l[(len(middle_l) // 2) - 1]
    else:
        left_mat = mat[:remaining]
        right_mat = mat[remaining+1:][::-1]
        middle = mat[remaining]
        total += middle[len(middle) // 2]

    for i in range(len(left_mat)):
        left_l = left_mat[i]
        right_l = right_mat[i]
        total += left_l[i] + left_l[len(left_l) - 1 - i]
        total += right_l[i] + right_l[len(right_l) - 1 - i]

        

    return total


mat = [[1, 2, 3, 4, 5, 6, 7],
        [8, 9, 10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19, 20, 21],
        [22, 23, 24, 25, 26, 27, 28],
        [29, 30, 31, 32, 33, 34, 35],
        [36, 37, 38, 39, 40, 41, 42],
        [43, 44, 45, 46, 47, 48, 49]]

result = diagonalSum(mat)
print(result)