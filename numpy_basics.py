import numpy as np
numbers = np.array([2,4,5,6,7])
print(numbers) # creating Numpy Arrays 
zero_array=np.zeros(4)
one_array=np.ones((2,3))
print(zero_array) #array with zeros 
print(one_array) #array with ones
random_values=np.random.rand(3,2)
print(random_values) # random number array
data = np.array([1,2,3,4,5])
reshaped_data=data.reshape(3,2)
print(reshaped_data)
