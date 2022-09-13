"""
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false
 
Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
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

def isPalindrome(linkedly_list):
    current = linkedly_list.head
    elements = []
    while current != None:
        elements.append(current.value)
        current = current.reference
    
    if elements == elements[::-1]:
        return True
    else:
        return False

array = [1, 2, 2, 1]
linked_list = LinkedList(array)
# read_llist(linked_list)
result = isPalindrome(linked_list)
print(result)