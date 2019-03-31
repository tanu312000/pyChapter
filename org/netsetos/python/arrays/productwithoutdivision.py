class productwithoutdivision:

    def productarray(arr):
        size=len(arr)
        temp=1
        product=[0] * size

        for index in range(size):
            product[index]=temp
            temp*=arr[index]
        temp=1
        for index in range(size-1,-1,-1):
            product[index]*=temp
            temp = temp * arr[index]

        return product



    def productarraywith(arr):
        size = len(arr)
        temp = 1
        productL = [0] * size

        for index in range(size):
            temp=temp*arr[index]
            productL[index]=temp
        print(productL)



        temp=1
        productR= [0] * size
        for index in range(size-1,0,-1):
            temp=temp*arr[index]
            productR[index] = temp
        print(productR)

        arr[0]=productR[1]
        arr[size-1] = productL[size-2]
        for i in range(1,size-1):
            arr[i]=productR[i+1]*productL[i-1]



        print(arr)








    arr = [10, 3, 5, 6, 2,1]
    data = productarraywith(arr)
    print(data)