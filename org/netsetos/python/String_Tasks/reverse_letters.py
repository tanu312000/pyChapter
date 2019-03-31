import math
class Reverse():
    def Reverse_letter(self,str):
        n=len(str)
        for i in range(0,math.floor((n)/2)):
            str[i],str[n-1]=str[n-1],str[i]
            n=n-1
        print(str)

dp=Reverse()
str=['The','Aunt','is','Happy']

p=dp.Reverse_letter(str)
