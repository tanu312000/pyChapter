def printRepeating(arr):
    size = len(arr)
    print("The Duplicate elements are : \n")
    for i in range(size):
        element = arr[i]
        absolute = abs(element)
        if (arr[absolute] >= 0):
            arr[absolute] = -arr[absolute]
            # print(arr[absolute])
        else:
            print(abs(arr[i]))


arr=[1,2,4,1,5,2]
printRepeating(arr)


