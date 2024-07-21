# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import numpy as np
arr=np.array([4,6,1,2,3,4,56,78,4])
#search in a array
x=np.where(arr==2)
y=np.where(arr%2==0)
print(y)
print(x)
# search sorted array:performs binary search in array and return the index where the specified value would be inseted to maintain  the search order.
var=np.array([1,2,4,6,9])
x=np.searchsorted(var,[3])
print(x)
var1=np.array([1,4,6,8,9,10])
y=np.searchsorted(var1,[2,5,7] ,side="right")
print("y",y)

#sort :sorting a array
arr1=np.array([2,5,3,4,1,7,6])
print(np.sort(arr1))
string1=np.array(['a','g','e'])
print(np.sort(string1))
ar=np.array([[3,5,12,5],[6,8,34,7]])
s=print(np.sort(ar))
#filtet array=getting some element out of an existing array and creating a new array out of them  (can also be done by slicing also)
var3=np.array(['a','g','t','r'])
f=[True,False,False,True]
newarr=var3[f]
print(newarr)

