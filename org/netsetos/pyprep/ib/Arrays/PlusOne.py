def PlusOne(A):
    size=len(A)
    A[size-1]=A[size-1]+1
    carry=A[size-1]/10
    A[size - 1]=A[size-1]%10

    for i in range(size-2,-1,-1):
        if(carry==1):
            A[i]=A[i]+1
            carry=A[i]/10
            A[i]=A[i]%10

    if(carry ==1):
        A.insert(0,1)


arr=[9,9,9]
PlusOne(arr)

for i in range(0,len(arr)):
    print(arr[i],end=" ")

