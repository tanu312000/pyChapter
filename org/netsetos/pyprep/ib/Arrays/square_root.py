import math
def sqrt(A):
    if (A == 0 or A == 1):
        return A
    low = 2
    high = math.floor(A / 2)
    mid = low + (high - low) / 2
    while (low <= high):
        mid = int(low + (high - low) / 2)
        if (mid * mid == A):
            return mid
        elif (mid * mid > A):
            high = mid - 1
        else:
            low = mid + 1
    if (mid * mid > A):
        mid = mid - 1
    return mid

S=81
s=sqrt(S)
print(s)

