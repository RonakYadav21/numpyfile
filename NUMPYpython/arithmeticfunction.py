import numpy as np
var=np.array([34,5,1,2])
print("minimun number is ",np.min(var))
print("maximun number is ",np.max(var))
print("square root",np.sqrt(var))
print("sin",np.sin(var))
print("cos",np.cos(var))
print("index of minimum number in array",np.argmin(var)) # give index of min number in array
print("index of maximun number in array",np.argmax(var))
var2=np.array([[3,5,1],[4,2,7]])
print(type(var2))
print("var2",var2)
print(np.min(var2,axis=0))
print(np.argmax(var2,axis=1))
print(np.cumsum(var))
print(np.cumsum(var2))
