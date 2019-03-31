def hcf(x,y):
    if(x>y):
        smaller=y
    else:
        smaller=x
    for i in range(0,smaller+1):
        if(x%i==0 and y%i==0):
            hcf=i
    return hcf

def rotate_values(arr,d,size):
    size=len(arr)
    for index1 in range(0,hcf(size,d)):
        temp=arr[index1]
        index2=index1
        while(1):
            index3=index2+d
            if(index3 >= size):
                index3=index3-size
            if(index3==index1):
                break
            arr[index2]=arr[index3]
            index2=index3
        arr[index2]=temp
    return arr

arr=[3,4,5,6,1,2]
d=rotate_values(arr,2,6)
print(d)