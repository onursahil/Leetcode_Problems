"""
Sum of All Odd Length Subarrays

Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.


Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.

Example 3:

Input: arr = [10,11,12]
Output: 66

"""

def sumOddLengthSubarrays(arr):
    total = 0
    if len(arr) < 3:
        total += sum(arr)
        return total
    else:
        for i in range(len(arr)):
            total += arr[i]
            j = i + 3
            while j < len(arr) + 1:
                sub_array = arr[i:j]
                total += sum(sub_array)
                j += 2

    return total


# arr = [1, 4, 2, 5, 3, 7, 8]
arr = [490,42,927,859,484,129,646,582,690,830,421,894,438,498,109,86,312,443,174,458,948,379,420,508,970,757,71,336,674,597,619,767,335,823,412,78,296,202,875,168,163,779,49,674,385,351,561,214,60,373,213,272,848,58,566,275,786,226,886,378,372,165,329,352,590,14,906,135,546,311,481,694,385,161,99,310,327,145,490,613,132,421,676,217,814,604,919,17,868,914,241,31,959,458,159,688,133,867,212,308]
result = sumOddLengthSubarrays(arr)
print(result)
print("Arr: ", len(arr))