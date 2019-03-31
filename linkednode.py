class Node:

    def __init__(Node, data):
        Node.data = data  # Assign data
        Node.next = None  # Initialize next as null
def count_nodes(head):
        count=1
        current=head
        while(current.next is not None):
            current=current.next
            count=count+1
        return count

def traverse(head):
        current = head  # start from the head node
        while current != None:
            print(current.data)  # access the node value
            current = current.next  # move on to the next node

def lPalin(A):
    current = A
    mid = A
    prev = None
    newCurrent = None
    newtemp = None
    newprev = None

    if (current == None or current.next == None):
        return 0

    while (current != None and current.next != None):
        current = current.next.next
        prev = mid
        mid = mid.next

    prev.next = None
    newCurrent = mid

    while (newCurrent != None):
        newtemp = newCurrent.next
        if (newCurrent == mid):
            newCurrent.next = None
            newprev = newCurrent
            newCurrent = newtemp

        else:
            newCurrent.next = newprev
            newprev = newCurrent
            newCurrent = newtemp
    curr = A

    while (newprev != None and current != None):
        if (newprev.data != current.data):
            return 0
        newprev = newprev.next
        current = current.next

    return 1



nodeA = Node(6)
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(2)
nodeE = Node(1)
nodeF = Node(9)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF


print("This Linked list's length is: (should print 5)")
#print(count_nodes(nodeA))
print(traverse(nodeA))

#traverse(Node)












