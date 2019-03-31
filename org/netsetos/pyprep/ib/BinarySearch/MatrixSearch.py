def MatrixSearch(A,B):

    start = 0
    end = (len(A)*len(A[0])) - 1
    print(start)
    print(end)
    print(A[-1][-1])


    m = len(A)
    n = len(A[0])

    while (start<end):
        mid = int((start + end) / 2)
        i = int(mid / n)
        j = mid % n
        if (A[i][j]<B):
            start = mid + 1
        elif (A[i][j]>B):
            end = mid
        elif(A[i][j]==B):
            return 1

    return 1 if A[-1][-1] == B else 0



A=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
d=MatrixSearch(A,1)
print(d)