def SortedInsertPosition(A,Targ):
    start_i=0
    final_i=len(A)-1

    if(len(A)==1 and A[0]==Targ):
        return 0
    if(final_i -1 <Targ):
        return final_i+1

    while(start_i < final_i):
        mid=(start_i+final_i)/2
        if(A[mid]==Targ):
            return mid
        elif(A[mid]>Targ):
            final_i=mid-1
            ans=mid-1
        else:
            start_i=mid+1
            ans=mid+1
    if(A[ans]<Targ):
        return ans+1
    else:
        return ans


A=[1,3,5,6]
test=SortedInsertPosition(A,7)
print(test)