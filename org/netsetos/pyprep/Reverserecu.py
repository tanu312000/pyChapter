#Reversing Using Recursion

class Node:
    def __init__(Node, data):
        Node.data = data  # Assign data
        Node.next = None  # Initialize next as null

def traverse(head):
    tempNode=head
    while(tempNode != None):
        print("Node Data is",tempNode.data)
        tempNode=tempNode.next

def reverse(prev,current):
    head=current
    if(current!=None):
        reverse(current,current.next)
        current.next=prev
    else:
        head=prev
    return head

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

head=reverse(None,head)
traverse(head)