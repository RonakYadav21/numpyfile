import numpy as np
arr=np.array([3,5,12,43,67])
#shuffle:used to suffle data this  method changes the original list, it does not return a new list
np.random.shuffle(arr)
print(arr)
ar=np.array([1,2,4,5,5,2,4])
x=np.unique(ar,return_index=True,return_counts=True)
print(x)
ar=np.array([1,2,4,5,5,2,4])
z=np.resize(ar,(2,3))
print(z)




