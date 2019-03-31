class pallin:
    def partition(self,str):

        self.result=[]
        self.curr_result=[]
        self.helper(str)
        return self.result

    def helper(self,str):
        l=len(str)
        if(l==1):
            self.curr_result.append(str)
            self.result.append(list(self.curr_result))
            self.curr_result.pop()
            return
        if(l==0):
            self.result.append(list(self.curr_result))
            return
        for i in range(1,l+1):
            left=str[0:i]

            if(self.ispallin(left)):
                self.curr_result.append(left)
                self.helper(str[i:])
                self.curr_result.pop()




    def ispallin(self,s):
        if(s==s[::-1]):
            return True
        return False


s="aab"
obj=pallin()
test=obj.partition(s)
print(test)


