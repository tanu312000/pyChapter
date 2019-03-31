def isValid(A):
    n = len(A)
    stack = []
    open_lst = ['(', '{', '[']
    close_lst = [')', '}', ']']
    dict={')':'(', '}':'{', ']':'['}
    for i in A:
        if (i in open_lst):
            stack.append(i)
        elif (i in close_lst):
            if (len(stack) > 0 and stack[-1] == dict[i]):
                stack.pop()
            else:
                return 0
    if (len(stack) == 0):
        return 1
A="()[]{}"
test=isValid(A)
print(test)