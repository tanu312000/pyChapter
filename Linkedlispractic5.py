#find merge point using approach 1 (Order n2)
class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None

def merge_singly_list(head1,head2):
    temp1=head1
    while(temp1.next!=None):
        temp2=head2
        while(temp2.next!=None):
            if(temp1==temp2):
                return temp2.data
            temp2=temp2.next
        temp1=temp1.next

head1 = Node(1)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(4)
nodeE = Node(5)
nodeF = Node(6)
nodeG = Node(7)
nodeH = Node(8)
head2 = Node(11)
nodeI = Node(18)
nodeJ = Node(20)


head1.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = nodeG
nodeG.next = nodeH
head2.next = nodeI
nodeI.next = nodeJ
nodeJ.next = nodeE

data=merge_singly_list(head1,head2)
print(data)


