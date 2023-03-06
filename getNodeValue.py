'''
here, we are given a singly linked list, and we need to return the element at a certain index.
'''

class Node:
    def __init__(self, value, nextNode = None):
        self.value = value 
        self.nextNode = nextNode

# iterative approach 
def valAtIndex(head : Node, index : int) -> int:
    count = 0
    current = head 
    while current != None:
        if count == index:
            return current.value 
        count+=1
        current = current.nextNode
    # if we exit while loop, then that index doesn't exist in our ll. 
    return(-1) 

# recursive approach 
def valAtIndexRecursive(head, index):
    if head == None:
        return -1
    if index == 0:
        return head.value 
    return valAtIndexRecursive(head.nextNode, index-1)

def tester():
    # making our nodes here
    node1 = Node(1) # 0
    node2 = Node(2) # 1
    node3 = Node(3) # 2
    #linking our nodes 
    node1.nextNode = node2
    node2.nextNode = node3

    assert(valAtIndex(node1, 0)) == 1
    assert(valAtIndex(node1, 1)) == 2
    assert(valAtIndex(node1, 2)) == 3
    assert(valAtIndexRecursive(node1, 0)) == 1
    assert(valAtIndexRecursive(node1, 1)) == 2
    assert(valAtIndexRecursive(node1, 2)) == 3

tester()