def matchPairs(nuts,bolts,low,high):
    if(low<high):
        pivot=partition(nuts,low,high,bolts[high])
        partition(bolts,low,high,nuts[pivot])

        matchPairs(nuts,bolts,low,pivot)
        matchPairs(nuts,bolts,pivot+1,high)

def partition(arr,low,high,pivot):
    i=low
    for j in range(low,high):
        if(arr[j]<pivot):
            arr[j],arr[i]=arr[i],arr[j]
            i=i+1

        elif(arr[j]==pivot):
            arr[j],arr[high]=arr[high],arr[j]
            j=j-1

    arr[i],arr[high]=arr[high],arr[i]
    return i


nuts=['@','#','$','%','^','&']
bolts=['$','%','&','^','@','#']
low=0
high=5
matchPairs(nuts,bolts,low,high)
print(nuts)
print(bolts)