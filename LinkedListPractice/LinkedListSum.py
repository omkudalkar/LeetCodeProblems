'''
here, we are given a singly linked list, and we need to find the sum of all elements. 
'''

class Node:
    def __init__(self, value, nextNode = None):
        self.value = value 
        self.nextNode = nextNode

#iterative approach 
def sum(head):
    current = head
    sum = 0 
    while current != None:
        sum += current.value 
        current = current.nextNode
    return sum

#recursive approach 
def sumRecursive (head):
    if head == None:
        return 0
    return head.value + sumRecursive(head.nextNode)

def tester():
    # make our nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    #link our nodes together 
    node1.nextNode = node2
    node2.nextNode = node3
    
    assert (sum(node1)) == 6
    assert (sumRecursive(node1)) == 6
    
    # make our nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(-3)
    #link our nodes together 
    node1.nextNode = node2
    node2.nextNode = node3
    assert (sum(node1)) == 0
    assert (sumRecursive(node1)) == 0
    
tester()