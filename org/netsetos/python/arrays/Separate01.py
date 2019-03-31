class separate0_1:

    def sep0_1(arr):
        size=len(arr)
        leftindex=0
        rightindex=size-1

        while(leftindex<rightindex):
            while(arr[leftindex]==0 and leftindex<rightindex):
                leftindex+=1
            while (arr[rightindex] ==1 and leftindex < rightindex):
                rightindex -= 1

            if(leftindex<rightindex):
                temp=arr[leftindex]
                arr[leftindex]=arr[rightindex]
                arr[rightindex]=temp
                leftindex+=1
                rightindex-=1

        return(arr)

    def sepeven_odd(arr):
        size=len(arr)
        leftindex=0
        rightindex=size-1

        while(leftindex<rightindex):
            while((arr[leftindex]%2==0) and leftindex<rightindex):
                leftindex+=1
            while((arr[rightindex]%2!=0) and leftindex < rightindex):
                rightindex -= 1

            if(leftindex<rightindex):
                temp=arr[leftindex]
                arr[leftindex]=arr[rightindex]
                arr[rightindex]=temp
                leftindex+=1
                rightindex-=1

        return(arr)

    arr=[1,0,1,0,1,0,0,1]
    data=sep0_1(arr)
    # arr = [1, 2, 1, 4, 3, 6,7, 1]
    # data =sepeven_odd(arr)
    print(data)
