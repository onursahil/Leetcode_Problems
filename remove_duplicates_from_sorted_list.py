"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]

Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def deleteDuplicates(head):
    nums = []
    current = head
    while current:
        nums.append(current.val)
        current = current.next
    if len(nums) == 0:
        return ListNode("")
    
    unique_nums = list(set(nums))
    unique_nums.sort()

    cur = dummy = ListNode(unique_nums[0])
    for i in range(1, len(unique_nums)):
        cur.next = ListNode(unique_nums[i])
        cur = cur.next
    
    return dummy