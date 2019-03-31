def sub_array(arr,sum):
    currSum=arr[0]
    start=0
    x=len(arr)
    for index in range(1,x):
        if(currSum>sum and start<index-1):
            currSum=currSum-arr[start]
            start=start+1

        if(currSum==sum):
            print("Sum found between indexes",start,index-1)
            return 1
        if(index<x):
            currSum=currSum+arr[index]
    print("No Subarray Found")
    return 0


arr=[8,5,-2,3,4,6,7]
data=sub_array(arr,16)
print(data)