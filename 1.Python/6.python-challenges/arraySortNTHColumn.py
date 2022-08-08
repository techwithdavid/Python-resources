import numpy as np
arr = np.array([[8, 3, 2],
                [3, 6, 5],
                [6, 1, 4]])
#Let us try to sort the rows by the 2nd column so that we get:

[[6, 1, 4],
 [8, 3, 2],
 [3, 6, 5]]

#We can do this by using the sort() method in numpy as:

arr = np.array([[8, 3, 2],
                [3, 6, 5],
                [6, 1, 4]])
                
#sort the array using np.sort

arr = np.sort(arr.view('i8,i8,i8'),
              order=['f1'],
              axis=0).view(np.int)
