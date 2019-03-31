class Reverse():
    def Reversestring(self,str):
        new_strings=[]

        index=len(str)
        while(index):
            index=index-1
            new_strings.append(str[index])
        return ''.join(new_strings)

    def Reversesentence_without(self,s):
        splitstring = s.split()
        n = len(splitstring)
        print(splitstring)
        str3=""
        for word in range(0,n):
            str2=self.Reversestring(splitstring[word])
            #print(splitstring[word],str2)
            str3=str3+str2+" "
        print(str3)
        str4=self.Reversestring(str3)
        print(str4)







p=Reverse()
str="Sarthak is a good boy"
t=p.Reversesentence_without(str)



