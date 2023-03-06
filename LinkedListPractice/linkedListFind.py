'''
here, we are given a singly linked list, and we need to find a certain element located within that list. 
'''

class Node:
    def __init__(self, value, nextNode = None):
        self.value = value 
        self.nextNode = nextNode 

#iterative approach 
def llfind(head: Node, target: int) -> bool:
    current = head 
    while current != None:
        if current.value == target:
            # return True as soon as target is found 
            return True
        current = current.nextNode
    # if we leave the while loop without returning True, we can return False since the element has clearly not been found. 
    return False

#recursive approach
def llfindRecursive(head: Node, target: int) -> bool:
    if head== None: 
        return False
    if head.value == target: 
        return True
    return llfindRecursive(head.nextNode, target)

def tester():
    # making our nodes here
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    #linking our nodes 
    node1.nextNode = node2
    node2.nextNode = node3

    assert (llfind(node1, 1)) == True
    assert (llfind(node1, 2)) == True
    assert (llfind(node1, 3)) == True
    assert (llfind(node1, 4)) == False
    assert (llfindRecursive(node1, 1)) == True
    assert (llfindRecursive(node1, 2)) == True
    assert (llfindRecursive(node1, 3)) == True
    assert (llfindRecursive(node1, 4)) == False
 

tester()