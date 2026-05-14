import numpy as np

#we use np.array to change it ito numpy array which takes less memory and results in faster perfomance
#than standard python list

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

# for j in range(1,30,3):
#    print(j)

# #changed into 
# print(np.arange(25)) 
# #reshape converts into 2D array
# reshaped_matrix = (np.arange(25).reshape(5,5)) 
# print(reshaped_matrix)

#mylist = np.array([1,2,3,4])
# new_copied_list = mylist.copy()
# #in python list 5 is added as element but in numpy each element is increased by 5
# new_copied_list += [5]
# print(f'Copied List: {new_copied_list}')
# print(f'original list:{mylist}')
# print(f'Id Copied List: {id(new_copied_list)}')
# print(f'Id original list:{id(mylist)}')

# import numpy as np
# #para : low,high,number
# ran_arr = np.random.randint(0,50,10)
# print(ran_arr)
# print(f'Maximum number -> {ran_arr.max()}')
# print(f'Positive of maximum number -> {ran_arr.argmax()}')
# #slicing
# print(ran_arr[:3])

# #broadcasting
# ran_arr[:3] = 0
# print(ran_arr[:3])
# print(ran_arr)

# mylist = [0,1,2,3]
# print(mylist[0:-1])
# print(mylist[:])

#neural networking
import numpy as np

first_array = np.array([[1,2,3],
                        [3,4,5]])

second_array = np.array([[1,1],
                         [2,2],
                         [3,3]])

print("Element-wise multiplication:")
print(first_array * first_array)

print("\nMatrix multiplication:")
print(np.dot(first_array, second_array))

#print(first_array@second_array)
#print(np.dmatmul(x,y))
#for transpose
#print(first_array,T)

  