import math
class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None

def count_list(head):
    temp=head
    count=1
    while(temp.next!=None):
        temp=temp.next
        count=count+1
    return count

def traverse(head):
    temp=head
    while(temp!=None):
        print("Data is", temp.data)
        temp=temp.next

    return head

def removekthnode(head,k):
    fast=head
    slow=head
    temp=head
    count=1
    while(count<k and fast!=None):
        fast=fast.next
        count=count+1

    if(fast==None):
        return None
    while(fast.next!=None):
        temp=slow
        fast=fast.next
        slow=slow.next
    temp.next=slow.next

    return head


def middleNode(head):
    fast=head
    slow=head

    while(fast!=None and fast.next!=None):
        fast=fast.next.next
        slow=slow.next
    return slow.data


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


#count=count_list(head)
#print(count)
#traverse(head)
#head=middleNode(head)
head=removekthnode(head,4)
traverse(head)
