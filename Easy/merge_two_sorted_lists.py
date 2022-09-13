"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = []
Output: []

Example 3:

Input: l1 = [], l2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    list1 = []
    current = l1
    while current != None:
        list1.append(current.val)
        current = current.next
    
    list2 = []
    current = l2
    while current != None:
        list2.append(current.val)
        current = current.next
        
    if len(list1) == 0 and len(list2) == 0:
        empty_list = ListNode()
        empty_list.value = None
    
    assemble = list1 + list2
    assemble.sort()
    print(assemble)
    
    cur = dummy = ListNode()
    for e in assemble:
        cur.next = ListNode(e)
        cur = cur.next
    
    return dummy.next