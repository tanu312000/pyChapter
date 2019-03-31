def anagram(A):
    if(A==None):
        return A
    d={}
    list_of_grp=[]
    grp=0
    for i in range(len(A)):
        s=''.join(sorted(A[i]))
        if(s not in d):
            list_of_grp.append([i+1])
            d[s]=grp
            grp=grp+1
        else:
            list_of_grp [d[s]].append(i+1)
    return list_of_grp

A=["cat","dog","tac","god","act"]
test=anagram(A)
print(test)


