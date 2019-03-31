def Combination(self,A,B):
    curr = []
    ans = []
    self.comb_helper(ans,curr, A, B,1)
    ans.sort()
    return ans


def comb_helper(self,ans,curr, A, B,start):
    # print start, end , k
    if (B == 0):
        ans.append(list(curr))

    elif (start<= B):
        curr.append(start)
        self.comb_helper(ans,curr, A, B-1,start+1)
        curr.pop()
        self.comb_helper(ans,curr, A, B,start+1)

A=4
B=2
test=Combination(A,B)
print(test)


