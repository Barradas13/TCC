import numpy as np

l = np.array([1, 2, 3, 4, 5]) #array not like python // faster but typable

a = np.zeros((3,5), dtype=int)
a[a == 0] = 3

x1 = np.ones((3,5))
# ndim = 2 (2d) shape = (3,5) size = 3 * 5 = 15 itemsize = 8 bytes nbytes = 15 * 5 bytes
# x1[2, 2] = element [2][2]

print(x1)
print(x1[0:2, :3])

print(x1.reshape(15)) #becames a line

print(np.split(x1, [2])) #split the first 2 rows from the 3°

print(1/a)

print(np.arange(1, 6))

print(np.empty((2,3)))