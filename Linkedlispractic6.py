#find merge point using approach 2 (Order n)
class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None

def merge_singly_list2(head1,head2):
    loopExist = 0
    fast = head1
    slow = head1
    temp2=head2
    while(temp2.next!=None):
        temp2=temp2.next
    lastNode=temp2
    temp2.next=head2
    while (fast != None and slow != None and fast.next != None):
        fast = fast.next.next
        slow = slow.next
        if (fast == slow):
            loopExist = 1
            break
    if (loopExist):
        slow = head1
        while (slow != fast):
            slow = slow.next
            fast = fast.next
        lastNode.next=None
        return slow.data
    return None



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

data=merge_singly_list2(head1,head2)
print(data)
