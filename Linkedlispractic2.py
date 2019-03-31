#Detect Loop
class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None

def detect_loop(head):
    fast=head
    slow=head
    while(fast!=None and slow!=None and fast.next!=None):
        fast=fast.next.next
        slow=slow.next
        if (fast==slow):
            return 1
    return 0

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
nodeF.next = nodeD

data=detect_loop(head)
print(data)

