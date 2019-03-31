class Node:

    def __init__(Node, data):
        Node.data = data  # Assign data
        Node.next = None  # Initialize next as null

def lPalin(self, A):
    current = A
    mid = A
    prev = None
    newCurrent = None
    newtemp = None
    newprev = None

    if (current == None or current.next == None):
        return 1

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
            newPrev = newCurrent
            newCurrent = newtemp
        else:
            newCurrent.next = newPrev
            newPrev = newCurrent
            newCurrent = newtemp

    current = A

    while (newPrev != None and current != None):
        if (newPrev.val != current.val):
            return 0

        newPrev = newPrev.next
        current = current.next

    return 1
lPalin(head)
