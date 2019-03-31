class Node:

    def __init__(Node, data):
        Node.data = data  # Assign data
        Node.next = None  # Initialize next as null


#Traversing Using Recursion
def traverseR(head):
    current=head
    if(current.next!=None):
        print("Data is ",current.data)
        traverseR(current.next)

#Traversing reverse Using Recursion
def traverseR1(head):
    current=head
    if(current.next!=None):
        traverseR1(current.next)
        print("Data is ",current.data)




head = Node('a')
nodeB = Node('b')
nodeC = Node('c')
nodeD = Node('d')
nodeE = Node('e')
nodeF = Node('f')



head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF



traverseR(head)
#traverseR1(head)