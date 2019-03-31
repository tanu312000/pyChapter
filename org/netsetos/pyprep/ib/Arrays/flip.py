def fliparray(arr,n):
    orig_zero_count=0
    max_diff=0
    curr_max=0
    for i in range(0,n):
        if(arr[i]==1):
            orig_zero_count=orig_zero_count+1
        if(arr[i]==1):
            val=1
        else:
            val=-1

        if(val<curr_max+val):
            curr_max=curr_max+val
        else:
            curr_max=val

        if(max_diff<curr_max):
            max_diff=curr_max
        else:
            max_diff=max_diff


    if(max_diff<0):
        max_diff=0


    return orig_zero_count+max_diff

arr=[0,1,0,0,1,1,0]
data=fliparray(arr,7)
print(data)
