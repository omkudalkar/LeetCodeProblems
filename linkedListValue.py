'''
here, we are given a singly linked list, and we need to store the value 
of every node in an array. 
'''

class Node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

# iterative solution
def makeArray(head):
    # this is the array in which we store our values 
    ret_arr = []
    current = head 
    while current != None:
        ret_arr.append(current.value)
        current = current.nextNode
    return ret_arr

# recursive solution
def makeArrayRecursively(head):
    ret_arr = []
    helperFunc(head, ret_arr)
    return ret_arr 
def helperFunc(head, ret_arr):
    if head == None:
        return 
    ret_arr.append(head.value)
    helperFunc(head.nextNode, ret_arr)

# quick test
def tester():
    # make nodes
    node1 = Node("a")
    node2 = Node("b")
    node3 = Node("c")
    # link nodes
    node1.nextNode = node2
    node2.nextNode = node3 

    assert(makeArrayRecursively(node1)) == ['a','b','c']
    assert(makeArray(node1)) == ['a','b','c']

tester()
    


