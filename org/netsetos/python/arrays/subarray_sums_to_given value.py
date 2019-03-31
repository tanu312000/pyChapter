class unsortedarray:
    def subarraysum(self,arr,x,y):#x=size of array
        currSum=arr[0]
        start=0
        for index in range(1,x):
            while(currSum>sum and start<index-1):
                currSum=currSum-arr[start]
                start=start+1
            if(currSum == sum):
                print("Sum found between indexes are",start,index)
                return 1
            if(index<x):
                currSum=currSum+arr[index]
                print("No Subarray found")
                return 0