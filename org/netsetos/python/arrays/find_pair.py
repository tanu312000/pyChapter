# class Find_Pair:
#
#     def __init__(self):
#         print('sfg')
#
#     def findPair(arr, n, sum):
#         count=0
#         n=len(arr)
#         for i in range(0, n):
#             for j in range(i + 1, n):
#                 findSum=arr[i]+arr[j]
#                 if(findSum==sum):
#                     print(arr[i],arr[j])
#                     count += 1
#
#         return count
#
#
#
#
#
#     print(findPair([5,4,2,6,7,3],6,8))
         #Order-n2

# class Find_Pair:
#
#     def findPair(arr, size, sum):
#         hash_map = {}
#         for i in range(size):
#             temp=sum-arr[i]
#
#             if(temp>0 and hash_map.get(temp)==1):
#
#                 print("Found the pair",temp,arr[i])
#             hash_map[arr[i]]=1
#
#     findPair((5,4,2,6,7,3),6,8)

class Find_Pair:

    def findPairsum_left_right(self,arr,sum):
        n = len(arr)
        #f=Find_Pair()
        self.insertion_sort(arr)

        left=0
        right=n-1

        while(left<right):
            curr_ele=arr[left] + arr[right]
            if(curr_ele==sum):
                print(arr[left],arr[right])
            if(curr_ele > sum):
                right=right-1
            else:
                left=left+1
        return -1

    def insertion_sort(self,A):
        for j in range(1, len(A)):
            i = j - 1
            key = A[j]
            while (i >= 0 and A[i] > key):
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = key

if __name__ == "__main__":
    fp=Find_Pair()
    data=fp.findPairsum_left_right([5, 4, 2, 6, 7, 3], 8)
    print(data)