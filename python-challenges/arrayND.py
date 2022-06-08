import numpy as np
ndArray = np.array([1, 2, 3, 4], ndmin=6)
print(ndArray)
print('Dimensions of array:', ndArray.ndim)

#This can be achieved by giving the ndmin attribute. 
# The below example demonstrates the creation of a 6D array:
