class sortusinginsertionkth:
    def sort(arr):
        a=len(arr)
        n=input("How many numbers you want to store: ")
        print("Enter numbers", n)
        for i in range(0,n):
            print(a[i])
        print("Before Sorting : ")
        for i in range(0,n):
            print(a[i])
        for i in range(1,n):
            current=a[i]
            for j in range(i,current,-1):
                if(j>0 and a[j-1]>current):
                    a[j]=a[j-1]
            a[j]=current

        print("After Sorting : ")
        for i in range(n):
            print(a[i])

    arr=[1,2,3,4,9,8]
    data=sort(arr)
    print(data)