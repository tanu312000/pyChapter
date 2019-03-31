#Starting node of loop detected
class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None

def find_start_node(head):
    loopExist=0
    fast=head
    slow=head
    while(fast!=None and slow!=None and fast.next!=None):
        fast=fast.next.next
        slow=slow.next
        if (fast==slow):
            loopExist = 1
            break
    if(loopExist):
        slow=head
        while(slow!=fast):
            slow=slow.next
            fast=fast.next
        return slow
    return None


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
nodeF.next = nodeC

data=find_start_node(head)
print(data.data)