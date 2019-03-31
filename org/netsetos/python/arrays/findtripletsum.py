from org.netsetos.python.search.Binary_Search import Binary_Search
from org.netsetos.python.sorting.N_Sort import N_Sort

class findtripletsum:
    def __init__(self,arr):
        self.arr=arr

    def find_triplet_s(self,sum):
        size=len(self.arr)
        for i in range(size):
            count=0
            for j in range(i+1,size):
                for k in range(j+1,size):
                    checksum=arr[i]+arr[j]+arr[k]

                    if(checksum==sum):
                        print(sum)
                        print("Successful sum",arr[i],arr[j],arr[k])


    def find_triplet_sort_search(self,key):
        bs=Binary_Search()
        bs.size(self.arr)

        size=Binary_Search.size(self.arr)
        print(size)



        ns=N_Sort()
        arr=ns.insertion_sort(self.arr)

        for i in range(size):
            for j in range(i+1,size):
                curr_ele=arr[i]+arr[j]
                diff=key-curr_ele
                bs=Binary_Search()
                data=bs.binary_Search(arr,j+1,size-1,diff)
                if(data != -1):
                    print(arr[i],arr[j],arr[data])

    def find_triplet_left_Right(self, key):
        size = len(self.arr)
        ns = N_Sort()
        self.arr = ns.insertion_sort(self.arr)
        for i in range (size-2):
            left=i+1
            right=size-1
            while(left<right):
                checksum=arr[i]+arr[left]+arr[right]
                if(checksum == key):
                    print("Triplet is",arr[i],arr[left],arr[right])
                    return 1
                if(checksum < key):
                    left=left+1
                else:
                    right=right-1








if __name__ == "__main__":


    arr=[1,2,3,6,8]
    key=6
    fp = findtripletsum(arr)

    fp.find_triplet_sort_search(key)
