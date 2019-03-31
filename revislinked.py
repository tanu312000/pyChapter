class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None

def traverse(head):
    temp=head
    while(temp!=None):
        print("Data is",temp.data)
        temp=temp.next

def insert(head,newNode):
    newNode.next=head
    head=newNode
    return head

def insertend(head,newNode):
    temp=head
    while(temp.next!=None):
        temp=temp.next
    temp.next=newNode
    newNode.next=None
    return head

def insertmiddle(head,newNode):
    temp=head
    while(temp.data!=2):
        temp=temp.next
    newNode.next=temp.next
    temp.next=newNode
    return head

def delnode(head):
    if(head==None or head.next==None):
        return head
    head=head.next
    return head

def delnodeend(head,nodetodeleted):
    if (head == None or head.next == None):
        return head
    temp=head
    while(temp.next.next!=None):
        temp=temp.next
    temp.next=None
    return head

def delnodemiddle(head,nodetodeleted):
    if (head == None or head.next == None):
        return head
    temp=head
    while(temp.next.data!=nodetodeleted):
        temp=temp.next
    temp.next=temp.next.next
    return head

def lasttofirst(head):
    if(head==None or head.next==None):
        return head
    p=head
    q=None
    while(p.next!=None):
        q=p
        p=p.next
    p.next=head
    q.next=None
    head=p
    return head

def printSLLRecursion(head):
    temp=head
    if(temp.next!=None):

        print("Data is",temp.data)
        printSLLRecursion(temp.next)

def ReverseSLLRecursion(head):
    temp=head
    if(temp.next!=None):
        ReverseSLLRecursion(temp.next)
        print("Data is",temp.data)

def ReverseUiteration(head):
    current=head
    prev=None
    nextNode=None
    while(current!=None):
        nextnode=current.next
        current.next=prev
        prev=current
        current=nextnode
    return prev

def revusing_recursion(prev,current):
    head=current
    if(current!=None):
        return revusing_recursion(current, current.next)
        current.next=prev
    else:
        head=prev





head = Node(1)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(4)
nodeE = Node(5)
nodeF = Node(6)
nodeG = Node(50)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF


#head=insert(head,nodeG)
#head=insertend(head,nodeG)
#head=insertmiddle(head,nodeG)
#head=delnode(head)
#head=delnodeend(head,6)
#head=delnodemiddle(head,4)
#head=lasttofirst(head)
#printSLLRecursion(head)
#ReverseSLLRecursion(head)
#head=ReverseUiteration(head)
head1=revusing_recursion(None,head)
traverse(head1)
#traverse(head)