class Node:

    def __init__(Node, data):
        Node.data = data  # Assign data
        Node.next = None  # Initialize next as null

def traverse(head):
        current = head  # start from the head node
        while current != None:
            print(current.data)  # access the node value
            current = current.next  # move on to the next node




def deleteDuplicates(head):
    if(head==None or head.next==None):
        return head

    prev=head
    nextnode=head.next

    while(nextnode!=None):
        if(nextnode.data==prev.data):
            prev.next=nextnode.next
            nextnode=nextnode.next

        else:
            prev=nextnode
            nextnode=nextnode.next

    return head

head = Node(1)
nodeB = Node(2)
nodeC = Node(2)
nodeD = Node(4)
nodeE = Node(5)
nodeF = Node(5)


head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF

head=deleteDuplicates(head)
# traverse(head)
#head=findkth_Node(head,3)
traverse(head)