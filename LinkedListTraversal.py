# here we make our node class. 
class Node:
    # constructor
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode
# making three nodes to work with. 
node1 =  Node("a")
node2 = Node("b")
node3 = Node("c") 
# linking nodes together. 
node1.nextNode = node2
node2.nextNode = node3
# a -> b -> c -> none
# printing linked list iteratively. 
def printLinkedList(head) -> None:
    # means we start at the beginning of the list. 
    current = head
    while current!= None:
        print (current.value)
        current = current.nextNode
# printing linked list recursively. 
def printLinkedListRecursively(head) -> None:
    # if the head is None, means we are at the very end we are done. 
    if head == None:
        return 
    print(head.value)
    printLinkedListRecursively(head.nextNode)

printLinkedList(node1)
printLinkedListRecursively(node1)