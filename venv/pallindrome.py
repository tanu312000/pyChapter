def pallindrome(n):

    x=n
    s=0
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    if(x==s):
        print("Pallindrome")
    else:
        print("Not a pallindrome")





pallindrome(121)
