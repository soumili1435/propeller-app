import numpy as np                  # Import NumPy library

# Creating a 1D NumPy array
numbers = np.array([2, 4, 5, 6, 7]) # Creates an array with given elements
print(numbers)                      # Prints the array

# Creating an array of zeros
zero_array = np.zeros(4)            # Creates a 1D array of size 4 filled with 0
print(zero_array)

# Creating an array of ones
one_array = np.ones((2, 3))         # Creates a 2x3 array filled with 1
print(one_array)

# Creating array with random float values between 0 and 1
random_values = np.random.rand(3, 2) # Creates a 3x2 array of random numbers
print(random_values)

# Reshaping an array
data = np.array([1, 2, 3, 4, 5, 6])  # Creates a 1D array
reshaped_data = data.reshape(3, 2)  # Reshapes it into 3 rows and 2 columns
print(reshaped_data)

# Statistical operations
arr = np.array([10, 20, 30, 40])    # Creates a 1D array
print(np.sum(arr))                  # Calculates sum of all elements
print(np.mean(arr))                 # Calculates mean (average)
print(np.max(arr))                  # Finds maximum value
print(np.min(arr))                  # Finds minimum value
print(np.std(arr))                  # Calculates standard deviation
print(np.var(arr))                  # Calculates variance

# Boolean masking
arr > 5                             # Returns True/False for each element > 5
print(arr[arr > 5])                 # Filters elements greater than 5

# Reshaping and flattening
print(arr.reshape(2, 2))            # Reshapes array into 2x2 matrix
print(arr.flatten())                # Converts to 1D array (returns a copy)
print(arr.ravel())                  # Converts to 1D array (returns a view)

# Creating 2D arrays for matrix operations
a = np.array([[1, 2], [3, 4]])      # Creates a 2x2 matrix
b = np.array([[5, 6], [7, 8]])      # Creates another 2x2 matrix

# Stacking arrays
print(np.vstack((a, b)))            # Vertically stacks arrays
print(np.hstack((a, b)))            # Horizontally stacks arrays
print(np.concatenate((a, b)))       # Concatenates arrays along axis 0

# Splitting arrays
print(np.split(arr, 2))             # Splits array into 2 equal parts

# Copy vs View
copy_arr = arr.copy()               # Creates a deep copy of the array
view_arr = arr.view()               # Creates a shallow copy (view)

# Sorting operations
print(np.sort(arr))                 # Returns sorted array
print(np.argsort(arr))              # Returns indices that would sort array
print(np.argmax(arr))               # Index of maximum value
print(np.argmin(arr))               # Index of minimum value

# Random number generation
print(np.random.randint(1, 10, size=5)) # Random integers between 1 and 9

# Fancy indexing
print(arr[[0, 2]])                  # Selects elements at index 0 and 2

# Masking with condition
mask = arr > 15                     # Creates boolean mask
print(arr[mask])                    # Filters elements greater than 15

# Conditional replacement
print(np.where(arr > 15, 1, 0))     # Replaces condition True with 1 else 0

# Matrix multiplication
print(np.dot(a, b))                 # Dot product of matrices
print(np.matmul(a, b))              # Matrix multiplication
print(a @ b)                        # Matrix multiplication using @ operator

# Linear algebra operations
print(np.linalg.det(a))             # Calculates determinant of matrix
print(np.linalg.inv(a))             # Calculates inverse of matrix
print(np.linalg.eig(a))             # Calculates eigenvalues & eigenvectors

# Statistical functions
print(np.median(arr))               # Finds median
print(np.percentile(arr, 50))       # Finds 50th percentile (median)
