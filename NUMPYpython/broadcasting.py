
import numpy as np
# broadcasting numpy arrays
arr1=np.array([2,5])
arr2=np.array([5,7,9])
var2=np.array([[1],[5],[9]])
print("dimension of var2 is :",var2.ndim)
print(var2+arr2)
print(arr1+var2)
#rules for broadcasting
# 1) same dimension
# 2) it should be like 1x3 and 3x1 ,1x2 and 3x1
