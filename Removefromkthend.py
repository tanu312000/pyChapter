class Node:

    def __init__(Node, data):
        Node.data = data  # Assign data
        Node.next = None  # Initialize next as null

def traverse(head):
    tempNode=head
    while(tempNode != None):
        print("Node Data is",tempNode.data)
        tempNode=tempNode.next

def findkth_Node(head,n):
    prevNode=head
    nextNode=head
    count=0
    temp=head
    if (head == None):
        return None

    while(count<n and nextNode!=None):
        nextNode=nextNode.next
        count=count+1

        #for 2 elements
    if(nextNode==None):
        head=head.next
        return head

    while(nextNode!=None):
        temp=prevNode
        prevNode=prevNode.next
        nextNode=nextNode.next


    temp.next = prevNode.next

    return head

head = Node(1)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(4)
nodeE = Node(5)
nodeF = Node(6)


head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF


head=findkth_Node(head,2)
traverse(head)