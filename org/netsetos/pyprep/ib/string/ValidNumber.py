def isNumber(A):
    A = A.strip()
    n = len(A)
    if (n == 0):
        return 0
    if (A[0] == '+' or A[0] == '-'):
        A = A[1:]
        n = n - 1
        if (n == 0):
            return 0
    i = 0
    dotEncount = False
    eCount = False
    while (i < n):
        if (A[i] >= '0' and A[i] <= '9'):
            i = i + 1
            continue
        if (A[i] == '.'):
            if (dotEncount):
                return 0
            dotEncount = True
            i = i + 1
            if (i >= n):
                return 0
            elif (A[i] == 'e'):
                return 0
        elif (A[i] == 'e'):
            if (eCount):
                return 0
            eCount = True
            dotEncount = True
            i = i + 1

            if (i < n and (A[i] == '-' or A[i] == '+')):
                i = i + 1
        else:
            return 0
        return 1

A=01.1e-10
test=isNumber(A)
print(test)