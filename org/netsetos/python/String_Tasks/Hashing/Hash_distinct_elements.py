def Hash_distinct_elements(arr):
    k=3
    n=len(arr)
    for i in range(0,n-k+1):
        dict={}
        count=0
        for j in range(i,i+k):
            key=arr[j]
            if(key not in dict):
                dict[key]=1
                count=count+1
            else:
                dict[key]=dict[key]+1
                count=count-1
        print(count)


arr=[10,10,20,30,30,40,10]
Hash_distinct_elements(arr)



