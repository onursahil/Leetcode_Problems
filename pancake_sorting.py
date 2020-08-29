""" 
Pancake Sorting

Given an array of integers A, We need to sort the array performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 0 <= k < A.length.
Reverse the sub-array A[0...k].
For example, if A = [3,2,1,4] and we performed a pancake flip choosing k = 2, we reverse the sub-array [3,2,1], so A = [1,2,3,4] after the pancake flip at k = 2.

Return an array of the k-values of the pancake flips that should be performed in order to sort A. Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

Constraints:

- 1 <= A.length <= 100
- 1 <= A[i] <= A.length
- All integers in A are unique (i.e. A is a permutation of the integers from 1 to A.length).

"""



def pancakeSort(A):
    
    def reverse(A, idx):
        to_reverse = A[0:idx + 1]
        A[0:idx + 1] = to_reverse[::-1]

    answer = []
    n = len(A)
    
    # Because: All integers in A are unique (i.e. A is a permutation of the integers from 1 to A.length)
    max_num = n
    for i in range(n):
        # Find the id of the maximum number
        id_max = A.index(max_num)

        # Flip/Reverse the array from beginning to the point where the maximum number is placed in the array
        reverse(A, id_max)

        # Append the real-index (index numbers start from 0, so we need +1 of that value)
        answer.append(id_max + 1)

        # Reverse all the array so that the largest number goes to the end of the array, thus, fixes the number at the end.
        # That is the reason of using 'max_num - 1' at each iteration
        reverse(A, max_num - 1)

        # Finally, since we moved the largest number to the end and fixed it there, we need to narrow our array(search space) to one lower
        # So if the beginning array length is 4, we fix 4 to the end so that our array lenght should become 3 while the next largest number is 3.
        max_num -= 1
    return answer


A = [3, 2, 4, 1]
answer = pancakeSort(A)
print(answer)

"""

Explanation:

- The array is a permutation of the integers from 1 to array.length. This is means that, if the length of the array is 4, then the maximum number in the array is 4.
- So we need to find the index of the maxiumum number which is array.length, so => id_max = array.index(len(array)).
- Next, we reverse our array from beginning(index = 0) to the index of largest number in the array(id_max) => A[0:id_max+1] (id_max + 1, because of the index slicing rule)
- After that we add/append the real-index number to the result array which we need as an answer
- Reversing all the array to move the largest number to the end of the array
- Finally narrowing our array so that our next largest number becomes the -1 narrowed length of the array

"""