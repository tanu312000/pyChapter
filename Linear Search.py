# def search(arr,x):
#     for i in range(len(arr)):
#         if(arr[i]==x):
#             return i
#     return -1
#
#
#
#
# print(search([1,2,3,4,5,6],6))


class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None

def LinearSearch(head,x):
    if (head!=None):
        while(head!=None):
            if(head.data == x):
                return head
            head=head.next

    return head




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



print(LinearSearch(head,4))