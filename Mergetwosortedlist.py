# class Node:
#     def __init__(Node,data):
#         Node.data=data
#         Node.next=None
#
#
# def altnode(head,head3,head4):
#     head3=head
#     if(head!=None or head.next!=None):
#         return
#     head4=head.next
#     while(head):
#         temp=head.next
#         if(temp!=None):
#             head=temp.next
#
#         head.next=temp
#         head=temp
#     return head3,head4
#
#
#
#
#
# def traverse(head):
#     temp=head
#     while(temp!=None):
#         print("Data is", temp.data)
#         temp=temp.next
#
#     return head
#
# def merge_Sorted_List(head1,head2):
#     if(head1.data <= head2.data):
#         mergeList=head1
#         head1=head1.next
#
#     else:
#         mergeList=head2
#         head2=head2.next
#
#     temp=mergeList
#     while(head1!=None and head2!=None):
#         if(head1.data <= head2.data):
#             temp.next=head1
#             temp=temp.next
#             head1=head1.next
#
#         else:
#             temp.next=head2
#             temp=temp.next
#             head2=head2.next
#
#     if(head1==None):
#         temp.next=head2
#     else:
#         temp.next=head1
#
#     return mergeList
#
# head = Node(4)
# nodeB = Node(5)
# nodeC = Node(6)
# head2 = Node(1)
# nodeE = Node(2)
# nodeF = Node(3)
#
#
# head.next = nodeB
# nodeB.next = nodeC
#
# head2.next = nodeE
# nodeE.next = nodeF
#
# head3=None
# head4=None
# #data=merge_Sorted_List(head1,head2)
# data=altnode(head,head3,head4)
# traverse(head3)
# traverse(head4)
# #traverse(data)

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    # Function to push node at head
    def push(self, data):
        new = Node(data)
        new.next = self
        return new

        # Function to get the alternate

    # nodes of the linked list
    def printAlternateNode(self):
        head = self

        while head and head.next != None:
            print(head.data, end=" ")
            head = head.next.next


# Driver Code
node = Node()

# Use push() function to construct
# the below list 8 -> 23 -> 11 -> 29 -> 12
node = node.push(12)
node = node.push(29)
node = node.push(11)
node = node.push(23)
node = node.push(8)

node.printAlternateNode()