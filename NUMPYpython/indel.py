import numpy as np           
arr=np.array([3,5,12,3,4])    
v=np.insert(arr,3,23) 
print(v)                    
w=np.insert(arr,(2,4),40)                             
print(w)
var=np.array([[3,5,1],[6,8,9]])             
v1=np.insert(var,2,[23,5,1],axis=0)
print(v1)                                    
# we can also use append()          
# delete data
d=np.delete(arr,2)
print(d)