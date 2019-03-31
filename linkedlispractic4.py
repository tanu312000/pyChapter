class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None

def find_mergepoint(head1,head2):
    temp1=head1

    while(temp1.next!=None):
        temp2 = head2
        while(temp2.next!=None):

            if(temp1==temp2):
                return temp2

            temp2 = temp2.next
        temp1 = temp1.next








head1 = Node(1)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(4)
nodeE = Node(5)
nodeF = Node(6)
nodeG = Node(7)
nodeH = Node(8)
head2 = Node(11)
nodeJ = Node(18)
nodeH = Node(20)

head1.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = nodeG
nodeG.next = nodeH
head2.next = nodeJ
nodeJ.next = nodeH
nodeH.next = nodeE


data = find_mergepoint(head1,head2)
print(data.data)