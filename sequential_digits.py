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

from collections import deque

def sequentialDigits(low, high):

    # Solution with collections.dequeue
    answer = []
    queue = deque(range(1,10))
    while queue:
        q_element = queue.popleft()
        if low <= q_element <= high:
            answer.append(q_element)
        remaining = q_element % 10
        if remaining < 9: 
            queue.append(q_element*10 + remaining + 1)

    # Solution with lists
    answer = []
    queue = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while queue:
        q_element = queue.pop(0)
        if low <= q_element <= high:
            answer.append(q_element)
        remaining = q_element % 10
        if remaining < 9:
            queue.append(q_element * 10 + remaining + 1)

    return answer

low = 10
high = 1000000000
result = sequentialDigits(low, high)
print(result)