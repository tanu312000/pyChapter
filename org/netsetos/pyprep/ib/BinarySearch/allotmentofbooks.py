def books(A,B):
    if(len(A)<B):
        return -1
    if(len(A)==B):
        return max(A)
    low=max(A)
    high=sum(A)
    while(low<=high):
        mid=int((low+high)/2)
        student=1
        page=0

        for book in A:
            if(page+book)>mid:
                student=student+1
                page=book

            else:
                page=page+book

        if(student<=B):
            high=mid-1
        else:
            low=mid+1
    return low

A=[12,34,67,90]
B=2
d=books(A,B)
print(d)