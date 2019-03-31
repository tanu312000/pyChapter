def mergeSort(A):

    if len(A)>1:
        mid = len(A)//2
        nL = A[:mid]
        nR = A[mid:]

        mergeSort(nL)
        mergeSort(nR)

        i=0
        j=0
        k=0
        while i < len(nL) and j < len(nR):
            if (nL[i] < nR[j]):
                A[k]=nL[i]
                i=i+1
            else:
                A[k]=nR[j]
                j=j+1
            k=k+1

        while i < len(nL):
            A[k]=nL[i]
            i=i+1
            k=k+1

        while j < len(nR):
            A[k]=nR[j]
            j=j+1
            k=k+1
    print("Merging ",A)

A = [54,26,93,17,77,31,44,55,20]
mergeSort(A)
print(A)