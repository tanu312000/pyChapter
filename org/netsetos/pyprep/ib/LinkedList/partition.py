def partition(self, A, B):
    frontHead = ListNode(None)
    frontCurr = frontHead
    backHead = ListNode(None)
    backCurr = backHead
    curr = A
    while (curr != None):
        nxt = curr.next
        if curr.val < B:

            # come before nodes
            frontCurr.next = curr
            frontCurr = curr
        else:
            # comes after nodes
            backCurr.next = curr
            backCurr = curr
        # Next
        curr = nxt
    # End back
    backCurr.next = None
    # Connect back to front
    frontCurr.next = backHead.next
    frontHead = frontHead.next
    return frontHead