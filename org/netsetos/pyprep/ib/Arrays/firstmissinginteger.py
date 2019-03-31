def segregate(self,arr):
    size=len(arr)
    j=0
    for i in range(0,size):
        if (arr[i] <= 0):
            arr[i], arr[j] = arr[j],arr[i]
            j=j+1
    return j


def findMissingPositive(A):
    size=len(A)
    arr_positive=[]
    firstNonnegative=self.segregate(A)
    for i in range(firstNonnegative,size):
        arr_positive.append(A[i])


def find_MissingNum(A):
    size=len(A)
    for i in range(0,size):
        x=abs(A[i])
        if(x - 1 < size and A[x-1] > 0):
            A[x - 1] = -A[x - 1]

    for i in range(0,size):
        if(A[i]>0):
            return i+1

arr=[0,10,2,-10,-20]
d=findMissingPositive(arr)
print(d)

