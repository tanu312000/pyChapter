import sys
def minXOR(A):
    A = sorted(A)
    size = len(A)
    minXor = float('inf')
    #minXor=int(sys.float_info.max)
    val = 0
    for i in range(size-1):
        val = A[i] ^ A[i+1]
        minXor = min(minXor,val)

    return minXor

arr = [0,4,7,9]
print (minXOR(arr))