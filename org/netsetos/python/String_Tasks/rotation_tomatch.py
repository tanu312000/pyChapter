class RotationString:
    def RotationString(self,str):
        n=len(str)
        i=n
        while(i>0):
            temp=str[0]
            for j in range(0,n-1):
                str[j]=str[j+1]
            str[n-1]=temp
            i=i-1
            print(str)


dp=RotationString()
arr="TANU"
p=dp.RotationString(arr)
print(p)

