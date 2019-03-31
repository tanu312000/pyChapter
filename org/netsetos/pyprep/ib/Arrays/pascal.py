def Pascal(A):
    arr=[[] for i in range (A)]
    for i in range(A):
        for j in range(i+1):
            if(j<i):
                if(j==0):
                    arr[i].append(1)
                else:
                    arr[i].append(arr[i-1][j] +arr[i-1][j-1])
            elif(j==i):
                arr[i].append(1)
    return (arr)


d=Pascal(6)
print(d,end=" ")