import numpy as np

arr = np.arange(1,10)
print(arr)
# arr = np.array([1,2,3,4,5,6,7,8,9])
arr[:3]=0
print(arr)


print(arr/arr)
print(np.divide(arr,arr))
print(np.isnan(arr/arr)) #nan means 'not a number'

ran_arr = np.random.rand(3,3)
print(ran_arr)

print(f'row-wise sum {np.sum(ran_arr, axis= 1)}')
print(f'column-wise sum {np.sum(ran_arr, axis= 0)}')
print(f'Array sum {np.sum(ran_arr)}')

first_arr = np.array([[1,2],[3,4]])
second_arr = np.array([[5,6],[7,8]])
print(f'Multiplication: {np.dot(first_arr,second_arr)}')