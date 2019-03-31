class Binary_Search:
    def binary_Serch(self,arr, x):
        l=0
        r=0
        while(l <= r):
            mid=l +(r-l)//2
            if(arr[mid]== x):
                return mid
            elif (arr[mid] < x):
                l=mid +1
            else:
                r=mid-1

        return -1

