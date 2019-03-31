def closest(arr):
    size=len(arr)
    arr2=[0]*size
    for i in range(size):
        for j in range(i+1,size):
            if(arr[j]>arr[i]):
                arr2[i]=arr[j]
                print("Greater element",arr[i],"to next is",arr[j])
                break
    print(arr2)

arr=[4,5,14,1,3,7]
data=closest(arr)
print(data)