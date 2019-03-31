class N_Sort:
    def insertion_sort(self,A):
        for j in range(1, len(A)):
            i = j - 1
            key = A[j]
            while (i >= 0 and A[i] > key):
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = key

        return A

# if __name__ == "__main__":
#     arr=[1,2,3,9,5,6,7,8,4]
#
#     fp = N_Sort()
#     data=fp.insertion_sort(arr)
#     print(data)