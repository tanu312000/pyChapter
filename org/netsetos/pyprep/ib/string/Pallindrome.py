def isPalindrome(A):
    i = 0
    j = len(A) - 1
    n = len(A)
    while (i < j):

        if(A[i].isalnum() and A[j].isalnum()):
            if(A[i].lower() != A[j].lower()):
                return 0
            else:
                i = i + 1
                j = j - 1
        elif not A[i].isalnum():
            i=i+1
        elif not A[j].isalnum():
            j=j-1
    return 1



A=".,"
d=isPalindrome(A)
print(d)