def isDecent(n):
    count=0
    for i in range(0,n):
        count=count+1
        if(count%2==0):
            s = set([ x for x in str(n)])
            if (len(s) > 2):
                return False

    return [False,True]['1' in s or '2' in s]









d=isDecent(12221)
print(d)