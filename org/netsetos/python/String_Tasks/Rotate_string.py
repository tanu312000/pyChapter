class rotation:
    def toMutable(self,string):
        List =[]
        for i in string:
            List.append(i)
        return List


    def toString(self,List):
        return ''.join(List)

    def rotate_elements(self,str):
        size=len(str)
        temp=str[0]
        str = self.toMutable(str)
        str2 = str
        for i in range(1,size):
            str[i-1]=str[i]


            for j in range(0,size):
                while(str[j]!=str2[j]):
                    print("Not Equal")
                    break
        str[size - 1] = temp
        print(str)
        print(str2)

if __name__=="__main__":

    fp=rotation()
    str="tanu"
    str=fp.rotate_elements(str)
    print(str)