import numpy as np

# a = np.array([1,2,3])
# print(a)
# print(type(a))
# print(a.dtype)

# a = [[1,2,3],[4,5,6]]
# print(a)
# print(type(a))

# m = np.matrix(a)
# print(m)
# print(type[m])
# print(m.ndim)

# three_dim =[[[1,2,3],[5,6,7],[7,8,9]]]
# print(np.array(three_dim).ndim)

# #zero matrix
# print(np.zeros(3,dtype='int'))
# print(np.zeros((3,3)))

# #identity matrix
# print(np.ones(3,dtype='int'))
# print(np.ones((3,3,2)))

# number_list = [1,2,3,4]
# print(number_list*2)

# numpy_array = np.array(number_list)
# print(number_list*2)

# identity matrix
# print(np.eye(3,dtype='int'))

#arange creates 1d array
# print(np.array(2,30))

for j in range(1,30,3):
   print(j)

#changed into 
print(np.arange(25)) 
#reshape converts into 2D array
reshaped_matrix = (np.arange(25).reshape(5,5)) 
print(reshaped_matrix)

