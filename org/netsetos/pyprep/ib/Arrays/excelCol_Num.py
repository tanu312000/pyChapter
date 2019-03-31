def titleToNumber( A):
    size = len(A)
    result = 0
    for i in range(0, size):
        num = ord(A[i]) - ord('A') + 1
        result = result + num * pow(26, size - 1)
        size = size - 1
    return result


test=titleToNumber("CDA")
print(test)