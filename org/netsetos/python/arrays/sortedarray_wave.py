def wave(arr):
    size=len(arr)
    arr.sort()
    for i in range(0,size,2):
        if(i>0 and (arr[i-1]>arr[i])):
            arr[i-1],arr[i]=arr[i],arr[i-1]

        if(i<size-1 and arr[i]<arr[i+1]):
            arr[i],arr[i+1]=arr[i+1],arr[i]

    return arr

arr=[1,3,2,5,7,9,4]
data=wave(arr)
print(arr)