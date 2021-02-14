"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.

Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:

Input: head = [0]
Output: 0

Example 3:

Input: head = [1]
Output: 1

Example 4:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880

Example 5:

Input: head = [0,0]
Output: 0
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def getDecimalValue(self):
        current = self.head
        nums = ""
        
        while current:
            nums += str(current.data)
            current = current.next
            
        result = int(nums, 2)
        
        print(result)
        # return result

if __name__ == "__main__":
    linked_list = LinkedList()
    binary_list = []
    
    try:
        while True:
            user_input = input("Enter the binary: ")
            binary_list.append(user_input)
    except NameError:
        pass
    except SyntaxError:
        pass

    linked_list.head = Node(binary_list[0])
    objs = [Node(binary_list[i]) for i in range(1, len(binary_list))]

    linked_list.head.next = objs[0]
    for i in range(len(objs) - 1):
        objs[i].next = objs[i + 1]

    linked_list.getDecimalValue()