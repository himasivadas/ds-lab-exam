import numpy as np
A =np.array([1,2,3,4])
B =np.array([8,7,6,5])
m,n = 4,4
for i in range(min(m,n)):
    print(np.multiply(A,B))
print("matrix multiplication")
print(np.multiply(A,B))
print("transpose of a")
print(A.T)
print("calculate a T b")
print(np.dot(A.T,B.T))
print("last 2 element of 3rd and 4th")
b1=8
b2=7
b3=18
b4=20
print(b3,b4 ,b3,b4)


