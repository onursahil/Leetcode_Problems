"""
Given an array of integers arr, 
return true if the number of occurrences of each value in the array is unique, 
or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. 
No two values have the same number of occurrences.

Example 2:

Input: arr = [1,2]
Output: false

Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

from collections import Counter
def uniqueOccurrences(arr):
    arr_count = dict(Counter(arr))
    values = sorted(list(arr_count.values()))
    set_values = sorted(list(set(values)))
    
    if set_values == values:
        return True
    else:
        return False

arr = [-17,19,-17,-17,19,2,19,-17,19,19,2,19,0,19,19]
result = uniqueOccurrences(arr)
print(result)