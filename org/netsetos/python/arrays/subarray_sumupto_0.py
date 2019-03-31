class SubArray:

    def findminmax(self,arr,sum_sofar,max,min,arr_size):
        for index in range(1,arr_size):
            if(arr[index]==0):
                sum_sofar[index]=sum_sofar[index-1]+(-1)
            elif (arr[index] == 1):
                sum_sofar[index] = sum_sofar[index - 1] + (1)
            if(sum_sofar[index]<min[0]):
                min=sum_sofar[index]
            if (sum_sofar[index]>max[0]):
                max=sum_sofar[index]

    def findLargestSubarray(self,arr,arr_size):
        maxSize=-1
        max=[0]*1
        min=[0]*1
        sum_sofar=[0]*arr_size
        if(arr[0]==0):
            sum_sofar[0]=-1
        else:
            sum_sofar[0]=1
        max[0]=sum_sofar[0]
        min[0]=sum_sofar[0]
        self.findminmax(arr,sum_sofar,max,min,arr_size)
        hash_size=max[0]-min[0]+1
        hash=[-1]*hash_size
        sum_far=0
        for index in range(0,hash_size):
            hash[index]=-1
        for index in range(0,arr_size):
            if(sum_sofar[index]==0):
                maxSize=index+1
                startIndex=0
                continue
            sum_far=sum_sofar[index]-min
            if(hash[sum_far]==-1):
                hash[sum_far]=index
            else:
                if(index-hash[sum_far]>maxSize):
                    maxSize=index-hash[sum_far]
                    startIndex=hash[sum_far]+1
        print("Maximum Size is",max)

        if(maxSize<=-1):
            print("No such subarray")

        else:
            print("largest sub-array is from ",startIndex,startIndex+maxSize-1)


sa=SubArray()
arr=[0,1,1,1,0,1,1,0]
size=len(arr)
sa.findLargestSubarray(arr,size)
