def Count_triangles(A):
    size=len(A)
    count=0
    for i in range(size-2):
        k=i+2
        for j in range(i+1,size):
            while(k>size and A[i]+A[j]>A[k]):
                k=k+1
            count=count+k-j-1
    return count

A=[1,1,1,3,5]
test=Count_triangles(A)
print(test)