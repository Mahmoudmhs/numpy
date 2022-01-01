import numpy as np
a=np.array([5,6])
b=np.array([2,4])
starts='##################################################################################'

# Dot product
c=np.dot(a,b)
print(c)
print(starts)

# method 2
d=0
for e,f in zip(a,b):
    d+=e*f
print(d)    
print(starts)

# method 3
d=0
for i in range(len(a)):
    d+=a[i]*b[i]
print(d) 
print(starts)

# method 4
d=0
print(a*b)
d= np.sum(a*b)
print(d)
print((a*b).sum())
print(starts)

# method 5   Dot product
d=0
d= a  @ b
print(d)
print(starts)

array_1 = np.array([[1, 2, 7], [3, 4, 8]])
array_2 = np.array([[1, 2], [3, 9], [4, 16]])
print(array_1 @ array_2)
print(starts)

####################################################################
## Matrix
# represent ada list of arrays
L= [[1,2],[3,4]]
print(L)
print(L[0])
print(L[0][1])
H = np.array([[1,2],[3,4]])
print(H)
print(H[0][1])
print(starts)

##column notation  colon means select every number 
print(H[:,0]) # select every row for coloumn 0
print(H[0,:]) # select every column for row 0
#transpose matrix
print(H.T)
# exponential
print(np.exp(H))
#mulitply
G=np.array([[1,2,3],[4,5,6]])
print(H.dot(G))

#determinant of the matrix
print(np.linalg.det(H))

#inverse of the matrix
print(np.linalg.inv(H))

#multiply inverseof  H by H should give identity
print(np.linalg.inv(H).dot(H))

#trace
print(np.trace(H))

#diagonal
print(np.diag(H))  # give matrix return vector of diag
print(np.diag([10,20]))  # give diagonal vector returm matrix

# solve linear equation example  x1+x2=2200  and 1.5x1+4x2=5050
K=np.array([[1,1],[1.5,4]])
M=np.array([2200,5050])
print(np.linalg.solve(K,M))

# Random numbers

# mean and variance and standard deviation


