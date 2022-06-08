def print_pairs(arr, N):
   # hash set
   hash_set = set()

   for i in range(0, len(arr)):
       val = N-arr[i]
       if (val in hash_set):  # check if N-x is there in set, print the pair
           print("Pairs " + str(arr[i]) + ", " + str(val))
       hash_set.add(arr[i])


# driver code
arr = [1, 2, 40, 3, 9, 4]
N = 3
print_pairs(arr, N)
