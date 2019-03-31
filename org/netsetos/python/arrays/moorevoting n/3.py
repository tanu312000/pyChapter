def repeatedNumber(self, A):
    size = len(A)
    count1 = 0
    count2 = 0
    first = sys.maxsize
    second = sys.maxsize

    for i in range(0, size):
        if (first == A[i]):
            count1 = count1 + 1
        elif (second == A[i]):
            count2 = count2 + 1
        elif (count1 == 0):
            count1 = count1 + 1
            first = A[i]
        elif (count2 == 0):
            count2 = count2 + 1
            second = A[i]
        else:
            count1 = count1 - 1
            count2 = count2 - 1

        count1 = 0
        count2 = 0

        for i in range(size):
            if (A[i] == first):
                count1 = count1 + 1
            if (A[i] == second):
                count2 = count2 + 1
        if (count1 >= size / 3):
            return first
        elif (count2 > size / 3):
            return second
        return -1