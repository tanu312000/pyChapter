# def Matrix_Median(M,N):
#     N=4
#     if (N % 2 != 0):
#         return M[N / 2][N / 2]
#
#     if (N % 2 == 0):
#         return (M[(N - 2) / 2][N - 1] + M[N / 2][0]) / (2.0)
#     return 0


import numpy as np

# 2D array
arr = [[14, 17, 12, 33, 44],
       [15, 6, 27, 8, 19],
       [23, 2, 54, 1, 4, ]]

# median of the flattened array
print(np.median(arr))

# median along the axis = 0
print("\nmedian of arr, axis = 0 : ", np.median(arr, axis=0))

# median along the axis = 1
print("\nmedian of arr, axis = 1 : ", np.median(arr, axis=1))

out_arr = np.arange(3)
print("\nout_arr : ", out_arr)
print("median of arr, axis = 1 : ",
      np.median(arr, axis=1, out=out_arr))

# arr =[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
# print("Median : ",Matrix_Median(M,N))