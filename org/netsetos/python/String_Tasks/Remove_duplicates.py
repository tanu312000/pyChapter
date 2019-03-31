class duplicates:
    def toMutable(self,string):
        List =[]
        for i in string:
            List.append(i)
        return List


    def toString(self,List):
        return ''.join(List)

    def removeduphash(self,str):
        size=len(str)
        hash=[0]*256
        curIndex=0
        finIndex=0
        temp=0
        str=self.toMutable(str)
        while(curIndex < size):
            temp=ord(str[curIndex])
            if(hash[temp]==0):
                hash[temp]=1
                str[finIndex]=str[curIndex]
                finIndex=finIndex+1
            curIndex=curIndex+1
        return self.toString(str[0:finIndex])


if __name__=="__main__":
    input_arr=[10,4,2,11,3,15,12,8,7,9,21,14]
    fp=duplicates()
    str="sarthakkumar"
    str=fp.removeduphash(str)
    print(str)




