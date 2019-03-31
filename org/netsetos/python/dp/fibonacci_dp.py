# def fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         for i in range(2, n + 1):
#             c = a + b
#             a = b
#             b = c
#         return b
#
#     # Driver Program

# def fib_bottom_up(n):  #best Complexity(faster)
#     bottom_up=(n+1)*[0]
#     if(n==1 or n==2):
#         return 1
#
#     bottom_up[0]=1
#     bottom_up[1]=1
#
#     for i in range(2,n+1):
#         bottom_up[i]=bottom_up[i-1]+bottom_up[i-2]
#     return bottom_up[n]


def fib_memo(n,memo):
    if(memo[n] is not None):
        return memo[n]

    if(n==1 or n==2):
        result= 1

    else:
        result=fib_memo(n-1,memo)+ fib_memo(n-2,memo)
    memo[n]=result
    return result

def fib2(n):
    memo=[None]*(n+1)
    return fib_memo(n,memo)







print(fib2(1000))
