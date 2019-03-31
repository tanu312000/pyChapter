def value(num):
    if(num == 'X'):
        return 10
    if(num == 'I'):
        return 1
    if(num == 'V'):
        return 5
    if(num == 'L'):
        return 50
    if(num == 'C'):
        return 100
    if(num == 'D'):
        return 500
    if(num == 'M'):
        return 1000

def romantoInt(A):
    i=1
    n=len(A)-1
    ans=0
    p=0

    for i in range(n,-1,-1):
        if(value(A[i])>=p):
            ans=ans+value(A[i])
        else:
            ans=ans-value(A[i])
    p=value(A[i])
    return ans

# def romanToInt(A):
#     s = []
#     num = 0
#     d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#
#     i = 1
#
#     while i < len(A) + 1:
#         # print i
#         num += d[A[-i]]
#         if i < len(A) and ((A[-i - 1] == 'I' and (A[-i] == 'V' or A[-i] == 'X'))
#                            or (A[-i - 1] == 'X' and (A[-i] == 'L' or A[-i] == 'C'))
#                            or (A[-i - 1] == 'C' and (A[-i] == 'D' or A[-i] == 'M'))):
#             i += 1
#             num -= d[A[-i]]
#         # print num
#         i += 1
#
#     return num


roman = "XXXIV"
print(romantoInt(roman))