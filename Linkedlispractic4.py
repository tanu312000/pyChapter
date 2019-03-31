#Reverse K-linked list

class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None

def traverse(head):
    temp=head
    while(temp!=None):
        print("Data is", temp.data)
        temp=temp.next

    return head

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

def reverse_klinkedlist(head,k):
    count=1
    prev=head
    while(count<k and prev.next!=None):
        prev=prev.next
        count=count+1

    newstart=prev
    nextNode=newstart

    while(1):
        prev=head
        temp=nextNode.next

        if(temp == None):
            ReverseUiteration(prev)
            return newstart

        nextNode.next=None
        nextNode=temp
        head=temp
        count=1

        while(count<k):
            if(temp.next == None):
                ReverseUiteration(prev)
                prev.next=nextNode
                return newstart

            temp=temp.next
            count=count+1

        ReverseUiteration(prev)
        prev.next=temp
        nextNode=temp

    return newstart



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
#nodeF.next = nodeC

data=reverse_klinkedlist(head,2)
traverse(data)



