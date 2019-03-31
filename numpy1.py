import numpy as np
a=np.array([[1,2,3,4,5],[6,7,8,9,10],[8,6,5,9,3]])
print(a)
print(a.itemsize)
print(a.size)
print(a.data)
print(a.shape)
print(a.ndim)
print(a.dtype)

for i in a:
    print(i(0))