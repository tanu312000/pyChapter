def PlusOne1(digits):
    size=len(digits)
    for i in range(size-1,-1,-1):
        if(digits[i]<9):
            digits[i]=digits[i]+1
            return digits

        digits[i]=0
    result=(size+1)*[0]
    result[0]=1
    return result

arr=[0,3,7,6,4,0,5,5,5]
d=PlusOne1(arr)
print(d)