def copyRandomList(head):
    if (head == None):
        return None
    #Step:1 create a new node
    # for each existing node and join them together
    # // eg: A->B->C
    # will
    # be
    # A->A
    # '->B->B'->C->C'
    Node.node = head
    while (node != None):
        copyNode=Node(node.data)
        nextNode=node.next
        node.next=copyNode
        copyNode.next=nextNode
        node = nextNode


    # // Step2: copy the random links:
    # for each new node n',

    node = head
    while (node != None):
        copyNode=node.next
        if(node.random != None):
            copyNode.random = node.random.next
        else:
            copyNode.random = None

    node = copyNode.next

    #Step3: detach the  list: // basically
    copyHead=head.next
    while(copyNode!=None and node!=None):
        node.next = node.next.next
    
    while (copyNode != NULL & & node != NULL) {
    node->next = node->next->next;
    if (copyNode->next == NULL) {
    break;
    }
    copyNode->next = copyNode->next->next;

    copyNode = copyNode->next;
    node = node->next;
    }

    return copyHead;

}
};


A=[1,2,3]
test=copyRandomList(A)
print(test)
