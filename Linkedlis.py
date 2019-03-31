class Node:

    def __init__(Node, data):
        Node.data = data  # Assign data
        Node.next = None  # Initialize next as null

def traverse(head):
    tempNode=head
    while(tempNode != None):
        print("Node Data is",tempNode.data)
        tempNode=tempNode.next

def insertNode(head,newNode):
    newNode.next=head
    head=newNode
    return head


def insertend(head,newNode):
    current=head
    while(current.next!=None):
        current=current.next
    current.next=newNode
    newNode.next = None
    return head


def insertmiddle(head,newNode):
    current=head
    while (current.data != 'e'):
        current = current.next
    newNode.next=current.next
    current.next=newNode
    return head

def delNode(head):
    if(head==None):
        return
    if(head.next==None):
        head=None
        return
    head=head.next
    return head

def delmiddle(head,nodedeleted):
    temp=head
    while(temp.next.data!=nodedeleted):
        temp=temp.next
    temp.next=temp.next.next
    return head

def delend(head,nodedeleted):
    temp=head
    while(temp.next.next!=None):
        temp=temp.next
    temp.next=None
    return head

def lastttofirst(head):
    if(head==None or head.next==None):
        return

    last=head
    seclast=None

    while(last.next!=None):
        seclast=last
        last=last.next

    last.next=head
    seclast.next=None
    head=last
    return head

def ll(head):
    if(head==None):
        return
    print(head.data)
    if(head.next!=None):
        ll(head.next.next)
    print(head.data)








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

head=ll(head)
# nodeP=head.next.next
# nodeP.next.next.next=nodeP
# head.next=nodeP.next
# print(head.next.next.next)
# raverse(head)
#head=insertmiddle(head,nodeM)
#head=insertend(head,nodeZ)
#head=delNode(head)
#head=delmiddle(head,'e')
#head=delend(head,'f')
#head=lastofirst(head,'f')
#head=lastttofirst(head)





#print(count_nodes(nodeA))


#traverse(Node)












