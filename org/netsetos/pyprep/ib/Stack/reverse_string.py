def reverseString(A):
    n = len(A)
    stack1 = []
    s1 = ""
    for i in range(0, n):
        stack1.append(A[i])
    print(stack1)
    print(len(stack1))
    while (len(stack1) >0):

        s1 = s1 + stack1.pop()
        print(s1)
    return s1

A="abc"
test=reverseString(A)
print(test)