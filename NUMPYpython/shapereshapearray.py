import numpy as np
var=np.array([3,6,45,2])
print("shape",var.shape)
print(var.ndim)
var1=np.array([[3,5,2],[5,8,79]])
print(var1.shape)
var2=np.array([5,2,1],ndmin=4)
print(var2)
print(var2.shape)
print(var2.ndim)
# reshape
ary=np.array([3,5,7,12,34,5])
print(ary.ndim)
x=ary.reshape(3,2)
print(x)
print("x dim :",x.ndim)

# reshape to 3d array
var3=np.array([3,5,6,7,12,34,45,67,98,90,11,12])
print(var3.reshape(2,3,2))
#reshape to 1d array from 3d
one=var3.reshape(-1)
print(one)
print(one.ndim)

