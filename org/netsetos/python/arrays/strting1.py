class strting1:
    def find0and1(arr):
        i=0

        result=0
        while(arr[i]!=1):
            result=result^arr[i+1]
            if(result==1):
                print(i+1)
            i=i+1








    def find_0_1_sep(self, arr):
        i = 0
        result = 0
        while (arr[i] != 1):
            result = 1 - result
            result = arr[i + 1] ^ result
            if (result == 1):
                print(i)
            i = i + 1

    arr = [ 0,0,0,1,1,1,1]
    data=find0and1(arr)
    print(data)