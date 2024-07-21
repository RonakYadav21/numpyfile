#datatype
import numpy as np
var=np.array([3,5,7,8])
print(type(var))
print(var.dtype)
#we can also create a array using dtype
a=np.array([1,2,6,5,6],dtype=float)
print(a.dtype)
print(a)
s=np.array(['s','b'])
print(s.dtype)
s1=np.array(['s','b',5,7])
print(s1.dtype)
s1=s1.astype(float) 
#convert to another datatype
a=np.array([1,2,6,5,6],dtype=np.int8)
print(a.dtype)


