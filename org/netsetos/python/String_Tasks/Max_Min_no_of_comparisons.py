def max_min(a):
    if(a[0] < a[1]):
        max=a[0]
        min=a[1]

    n = len(a)
    for i in range(2,n):

        if(a[i]>max):
            max=a[i]
        elif(a[i]<min):
            min=a[i]
    return(max,min)

a=[1,2,3,4,5]
print(max_min(a))