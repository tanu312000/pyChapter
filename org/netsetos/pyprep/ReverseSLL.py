# Reversing Using Iteration

class Node:
    def __init__(Node, data):
        Node.data = data  # Assign data
        Node.next = None  # Initialize next as null

def traverse(head):
    tempNode=head
    while(tempNode != None):
        print("Node Data is",tempNode.data)
        tempNode=tempNode.next


def reverserr(currentNode):
    prev     = None
    nextNode = None

    while(currentNode!=None):
        nextNode=currentNode.next
        currentNode.next=prev
        prev=currentNode
        currentNode=nextNode
    return prev

head = Node('a')
nodeB = Node('b')
nodeC = Node('c')
nodeD = Node('d')
nodeE = Node('e')
nodeF = Node('f')
nodeZ = Node('z')
nodeM = Node('m')


head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF

head=reverserr(head)
traverse(head)