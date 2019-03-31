class Equilibrium:
    def equilibrium_index(arr):
        sum=0
        leftsum=0
        size=len(arr)
        for i in range(size):
            sum=sum+arr[i]
        for i in range(size):
            sum=sum-arr[i]
            if(leftsum == sum):
                print("Equilibrium index is",i)
            leftsum=leftsum+arr[i]




    arr=[7,2,1,4,6,4,0]
    data=equilibrium_index(arr)
    print(data)