class RotationString:
    def RotationString(self,str,str1):
        n=len(str)
        s=str+str
        if(s.count(str1)>0):
            print(str,"is matched with",str1)
        else:
            print(str,"is not matched with",str1)

dp=RotationString()
str="TANU"
str1="SNUT"
p=dp.RotationString(str,str1)

