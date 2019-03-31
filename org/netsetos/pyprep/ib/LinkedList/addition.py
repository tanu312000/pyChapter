class Node:
    def __init__(Node, data):
        Node.data = data  # Assign data
        Node.next = None  # Initialize next as null


def addTwoNumbers(A, B):
    carry = 0
    head = Node(0)
    curr = head
    while (A or B or carry):
        if (A and B):
            curr.data = A.data + B.data + carry
            A = A.next
            B = B.next
        elif A:
            curr.val = A.val + carry
            A = A.next
        elif B:
            curr.val = B.val + carry
            B = B.next
        else:
            curr.val = carry
            carry = 0

        if (curr.val > 9):
            carry = curr.val / 10
            curr.val = curr.val % 10
        else:
            carry = 0

        curr.next = Node(0)
        prev = curr
        curr = curr.next

    prev.next = None
    return head

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


A=1,2,3,4,5
B=3,6,9
test=addTwoNumbers(A,B)
print(test)