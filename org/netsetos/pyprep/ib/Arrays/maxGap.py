import sys,math
def maxGap(arr):
    size=len(arr)
    maxVal=arr[0]
    minVal=arr[0]

    for x in  arr:
        maxVal=max(maxVal,x)
        minVal=min(minVal,x)

    maxBucket=[-sys.maxsize]*size
    minBucket=[sys.maxsize]*size


    delta=(maxVal-minVal)/size

    for i in range(0,size):
        if(arr[i]==maxVal or arr[i]==minVal):
            continue
    #finding index of bucket
        index=round((arr[i]-minVal)/delta)

    #filling and updating max val
        if(maxBucket[index]==-sys.maxsize):
            maxBucket[index]=arr[i]

        else:
            maxBucket[index]=max(maxBucket[index],arr[i])

        if(minBucket[index]==sys.maxsize):
            minBucket[index]=arr[i]

        else:
            minBucket[index]=min(minBucket[index],arr[i])

    # Finding maximum difference between maximum value
    #of previous bucket minus minimum of current bucket.
    prev_val = minVal
    max_gap = 0
    for i in range(0,size):
        if (minBucket[i] == sys.maxsize):
            continue
        max_gap = max(max_gap, minBucket[i] - prev_val)
        prev_val = maxBucket[i]


    max_gap = max(max_gap, maxVal - prev_val)
    return max_gap


arr = [1,5, 10, 15,26]
print(maxGap(arr))
