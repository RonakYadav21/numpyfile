import numpy as np
c=np.add([1,3,6,8],[3,2,1,8])
print(c)
a=[[5,7,12,34],[34,12,11,1]]
d=np.subtract(a,[[34,1,7,3],[4,7,8,1]])
print(d)
print(type(d))
a=np.array([3,5,12,34])
b=np.array([5,6,8,1])
c=np.power(a,b)
print(c)
a=[1,1,1,1]
r_eciprocal=np.reciprocal(a)
print(r_eciprocal)
var=np.array([3,5,1])
varmod=var%3
print(varmod)
vardivide=var/3
print(vardivide)
varb=np.array([3,4,9])
varadd=var+varb
print(varadd)
varsub=var-varb
print(varsub)
varpower=var**varb
print(varpower)
varpow=np.power(var,varb)
print(varpow)
# for 2D arrays
a=[[3,6,12],[5,78,32]]
b=[[4,6,1],[7,3,2]]
print(np.add(a,b))
print()
print(np.power(a,b))

