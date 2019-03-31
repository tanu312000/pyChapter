class Sort:
    def insertion_sort(A):
        for j in range(1, len(A)):
            i = j - 1
            key = A[j]
            while (i >= 0 and key < A[i]):
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = key

    def bubble_sort(A):
        size = len(A)
        for i in range(len(A)):
            print(len(A))
            for j in range(size - i - 1):
                if (A[j] > A[j + 1]):
                    A[j], A[j + 1] = A[j + 1], A[j]

    def merge_sort(A):
        size = len(A)
        for i in range(len(A)):
            print(len(A))
            for j in range(size - i - 1):
                if (A[j] > A[j + 1]):
                    A[j], A[j + 1] = A[j + 1], A[j]


