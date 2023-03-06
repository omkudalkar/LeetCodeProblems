'''
Here, we are given a singly linked list, and we need to reverse it. 
'''

class Node:
    def __init__(self, value, nextNode = None):
        self.value = value 
        self.nextNode = nextNode 

# making our nodes here
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
#linking our nodes 
node1.nextNode = node2
node2.nextNode = node3

# reverse List iteratively.
def revserseList(head):
    prev = None
    curr = head
    while curr != None:
        next = curr.nextNode
        curr.nextNode = prev
        prev = curr
        curr = next
    return prev

# prints list. 
def printList(head):
    curr = head 
    while curr != None:
        print(curr.value)
        curr = curr.nextNode

# this should print out 3 2 1. 
printList(revserseList(node1))
    
