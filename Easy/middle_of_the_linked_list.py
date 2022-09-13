"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

Note:

The number of nodes in the given list will be between 1 and 100.
"""

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.reference = next

class LinkedList(object):
    def __init__(self, sequence):
        self.head = Node(sequence[0])
        current = self.head
        for item in sequence[1:]:
            current.reference = Node(item)
            current = current.reference

def read_llist(linkedly_list):
    current = linkedly_list.head
    while current != None:
        print(current.value)
        current = current.reference

def middleNode(linkedly_list):
    current = linkedly_list.head
    elements = []
    while current != None:
        elements.append(current.value)
        current = current.reference
        
    index = len(elements) // 2
    start_index = 0
    current_node = linkedly_list.head
    while current_node != None and start_index < index:
        current_node = current_node.reference
        start_index += 1
    
    return current_node


array = [1, 2, 3, 4, 5]
linked_list = LinkedList(array)
# read_llist(linked_list)
print(middleNode(linked_list).value)