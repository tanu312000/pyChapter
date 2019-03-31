import math
def min_reversal(A):
    stack=[]
    if(len(A)%2!=0):
        return -1
    for i in range(0,len(A)):
        if(A[i]=='}' and stack[-1]!=-1):
            x=stack[-1]
            if(x=='{'):
                stack.pop()
            else:
                stack.append(A[i])
        else:
            stack.append(A[i])
    un_bal=stack[-1]
    n=0
    while(stack[-1]!=-1 and stack[-1]=='{'):
        stack.pop()
        n=n+1
    return math.ceil(un_bal/2 + n % 2)






s=["}","}","{","{","}","}","{","{"]
target=9
test=min_reversal(s)
print(test)