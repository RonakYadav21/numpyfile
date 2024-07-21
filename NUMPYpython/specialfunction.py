import  numpy as np
#array with 0's
ar_zero=np.zeros(7)
print(ar_zero)

# to print M-D zero's array
ar_zero1=np.zeros((3,4))
print(ar_zero1)


ar_zero2=np.zeros((3,3,3))
print(ar_zero2)
print()
#array with ones's
onearray=np.ones(6)
print(onearray)
print()
# 2 d ones array
onesarray2d=np.ones((4,5))
print(onesarray2d)


# creat an empty array
ar_empty=np.empty((4,5))
print(ar_empty)


#  array using arange()  give element in given range 
ar_rn=np.arange(5)
print("arange",ar_rn)

#identity array
ar_diag=np.eye(4,4)
ar_dia=np.eye(3)
print(ar_dia)
print(ar_diag)

#linspace
ar_lin=np.linspace(1,10,num=5)
print(ar_lin)