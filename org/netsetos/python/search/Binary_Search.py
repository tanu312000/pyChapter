
class Binary_Search:
    count=0

    def binary_Search(self,arr,left,right,key):
        size=len(arr)
        right=size-1
        while(left<=right):
            mid=left+(right-left)//2
            if(arr[mid]==key):
                return mid

            if(arr[mid]< key):
                left=mid+1

            else:
                right=mid-1

        return -1

    @staticmethod
    def size(arr):
        count=len(arr)
        Binary_Search.count=len(arr)





# if __name__ == "__main__":
#     arr=[1,2,3,4,5,6,7,8,9]
#     key=6
#     fp = Binary_Search()
#     data=fp.binary_Search(arr,key)
#     print(data)

