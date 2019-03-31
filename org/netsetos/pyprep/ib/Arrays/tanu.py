def simplifyPath(A):
        stack=[]
        new_A=A.split('/')
        new_A=list(filter(lambda x:x!='',new_A))
        print(new_A)
        i=0
        while(i<len(new_A)):
            if(new_A[i]=='.'):
                pass
            elif(new_A[i]=='..'):
                stack=stack[:-1]
            else:
                stack.append(new_A[i])
            i=i+1
        s='/'.join(stack)
        return '/'+s

A1="/a/./b/../../c/"
A="//a//.//b//..//..//c//"
sd=simplifyPath(A)
print(sd)