def reverse(A,m,n):
    curr=A
    start=None
    startTemp=None
    end=None
    endTemp=None

    if(A==None):
        return None
    length=0
    while(length<m):
        length=length+1
        if(length==m-1):
            start==curr
        elif(length==m):
            startTemp=curr
        prev=curr
        curr=curr.next
    while (length < n):
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
        length = length + 1
        if (length == n):
            endTemp=prev
            end=curr
            startTemp.next=curr
            if (start!=None):
                start.next=endTemp
            elif(start==None):
                A=endTemp
    return A