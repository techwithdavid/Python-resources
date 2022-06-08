import numpy as np
#inputs
inputArray = np.array([[35, 53, 63], [72, 12, 22], [43, 84, 56]])
new_col = np.array([[20, 30, 40]])
# delete 2nd column
arr = np.delete(inputArray, 1, axis=1)
#insert new_col to array
arr = np.insert(arr, 1, new_col, axis=1)
print(arr)
