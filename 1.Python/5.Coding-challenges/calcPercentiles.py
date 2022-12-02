import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7])
# Returns the 50th percentile which is also the median
p = np.percentile(a, 50)
print(p)
