import numpy as np
# a = np.array([1,2,3] , dtype = 'int16')
# print(a)
b = np.array([[9,6,7],[8,2,3]])
# print(b)
# print(a.ndim) #get dimension
# print(a.shape) #get shape
# print(a.dtype)
# print(a.itemsize)#get size
# print(a.size)
# print(b[1,0])# get specific element
# print(b[0,:]) #get a specific row
# print(b[:,1]) #get aspecific column
# print(b[0, 1:2:]) # get fancy
# b[1,2] = 20
# print(b)
# b[ : ,2] = 5
# print(b)

c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(c[0,1,1])
# print(c[:,1,:])
# c[:,1,:] = [[1,1],[2,3]]
# print(c[:,1,:])

#INITIALIZING DIFFERENT TYPES OF ARRAYS
# print(np.zeros((2,3,3,2)))
# print(np.ones((2,3,3,2)))
# print(np.full((2,3,3,2),99))
print(np.full_like(c,4))
print(np.random.rand(2,2))#random decima numbers
print(np.random.randint(7,size = (3,3)))
print(np.identity(6))





import numpy as np

# ---- ARRAYS ----
a = np.array([1, 2, 3, 4, 5])
print(a)
print(type(a))

# 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.shape)

# ---- ARRAY CREATION ----
print(np.zeros((3, 3)))
print(np.ones((2, 4)))
print(np.eye(3))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))

# ---- INDEXING & SLICING ----
a = np.array([10, 20, 30, 40, 50])
print(a[0])
print(a[-1])
print(a[1:4])
print(a[::2])

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b[0, 0])
print(b[1, 2])
print(b[:, 1])
print(b[0, :])

# ---- MATH OPERATIONS ----
a = np.array([1, 2, 3, 4])
print(a + 10)
print(a * 2)
print(a ** 2)
print(np.sqrt(a))

b = np.array([10, 20, 30, 40])
print(a + b)
print(a * b)

# ---- USEFUL FUNCTIONS ----
a = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))
print(np.sort(a))
print(np.std(a))