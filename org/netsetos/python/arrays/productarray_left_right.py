def productarraywithoutdivision(arr):
    size=len(arr)
    temp=1
    product=size*[0]
    for index in range(0,size):
        product[index]=temp
        temp=temp*arr[index]
    temp=1
    for index in range(size-1,-1,-1):
        product[index]=product[index]*temp
        temp=temp*arr[index]
    print( product)

arr=[10,20,30,40]
productarraywithoutdivision(arr)