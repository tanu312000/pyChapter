def reverse(A):
    a = 0
    for i in range(32):
        a <<= 1
        a =a|A & 1
        A >>= 1
    return a



test=reverse(3)
print(test)