def rotatebyreverse(arr,leftI,rightI):

    while(leftI<rightI):
        arr[leftI],arr[rightI]=arr[rightI],arr[leftI]
    leftI=leftI+1
    rightI=rightI-1

def rotateleft(arr,d):
    size = len(arr)
    rotatebyreverse(arr,0,d-1)
    rotatebyreverse(arr,d,size-1)
    rotatebyreverse(arr, 0, size-1)

arr=[1,2,3,4,5,6]
d=rotateleft(arr,2)
print(d)