"""
Sequential Digits

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.


Example 1:

Input: low = 100, high = 300
Output: [123,234]

Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
"""

def sequentialDigits(low, high):
    answer = []
    for i in range(low, high + 1):
        num_list = list(str(i))
        for j in range(len(num_list) - 1):
            flag = True
            if int(num_list[j]) == int(num_list[j + 1]) + 1:
                continue
            else:
                flag = False
        if flag == True:
            answer.append(i)
    
    return answer


low = 100
high = 300
result = sequentialDigits(low, high)
print(result)