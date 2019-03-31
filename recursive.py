def add(n):
    if n==0 :
        return 1
    else:
        r=n+add(n-1)

    return r


print(add(10))