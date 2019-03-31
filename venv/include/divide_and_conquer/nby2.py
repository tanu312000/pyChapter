import math
class dup:
    def nby2(arr):
        size = len(arr)
        arr = arr.sort()
        for i in range(0, (size / 2)+1):
            if (arr[i] == arr[i + math.floor(size / 2)]):
                return arr[i]




if __name__=="__main__":
    arr = [1, 1, 1, 1, 2, 3, 4]
    fp=dup
    str="sarthakkumar"
    str=fp.nby2(arr)
    print(arr)

arr=[1,1,1,1,2,3,4]