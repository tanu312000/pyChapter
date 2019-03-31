def partition (A,p,r):
    x=A[r]
    i=p-1

    for j in range (p,r-1):
        if(A[j]<=x):
            i=i+1
            A[i],A[j]=A[j],A[i]

        A[i+1],A[r]=A[r],A[i+1]
        return(i+1)


def quickSort(A,p,r):
    if(p<r):
        q=partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)


A=[10,23,45,15,67,34,67]
partition(A,0,6)
quickSort(A,0,6)

n=len(A)
quickSort(A,0,n-1)
print(A)

