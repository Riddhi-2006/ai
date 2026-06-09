import numpy as np
# arr = np.array([[1,2,3]])
# r1 = np.repeat(arr,2,axis = 1)
# print(r1)
# output = np.ones((5,5))
# print(output)
# z = np.zeros((3,3))
# z[1,1] = 9
# print(z)
# output[1:4,1:4] = z#can replace 4 to -1
# print(output)

# a = np.array([1,2,3])
# b = a.copy()
# b[1] = 200
# print(a,b)

#mathematics

# a = np.array([1,2,3])
# print(a)
# print(a+2)
# print(a-2)
# print(a*2)
# print(a/2)
# b = np.array([2,3,4])
# print(a+b)
# print(a**2)
# print(np.sin(a))

#linear algebra

# a = np.full((2,3),3)
# b = np.ones((3,2))
# print(np.matmul(a,b))

# c = np.identity(3)
# print(np.linalg.det(c))

#statistics

# stats = np.array([[1,2,3],[2,3,4]])
# print(stats)
# print(np.min(stats))
# print(np.max(stats, axis = 1))
# print(np.sum(stats))

# reorganizing arrays

# a = np.array([[1,2,3],[4,5,6]])
# print(a)
# b = a.reshape((3,2))
# print(b)

# #vertically stacking matrices
# v1 =np.array([1,2,3])
# v2 =np.array([3,4,5])
# print(np.vstack([v1,v2,v1,v2]))
# v3 = np.ones((3,1))
# v4 = np.zeros((3,1))
# print(np.hstack((v3,v4,v3,v4)))

#Miscellaneous
#load data from file
filedata = np.genfromtxt('data.txt',delimiter=',')
print(filedata)
print(filedata.astype('int32'))

#boolean masking and advanced indexing
print(filedata<5)
print(filedata[filedata<5])
print(np.any(filedata < 5 , axis = 0))
print(np.all(filedata < 5 , axis = 0))
print(np.all(filedata < 5 , axis = 1))
print((filedata < 5) & (filedata > 2))

# you can indeex with a list  in numpy
a = np.array([1,2,3,4,5,6,7,8])
print(a[[1,5,6]])

a=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(a[[0,1,2,3],[1,2,3,4]])
print(a[[0,4,5],3:])

