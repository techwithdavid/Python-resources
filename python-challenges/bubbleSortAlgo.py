def bubbleSort(x):

n = len(x)

# Traverse through all array elements

for i in range(n-1):

for j in range(0, n-i-1):


if x[j] > x[j+1] :

x[j], x[j+1] = x[j+1], x[j]

# Driver code to test above

arr = [25, 34,47, 21, 22, 11,37]

bubbleSort(arr)

print ("Sorted array is:")

for i in range(len(arr)):

print ("%d" %arr[i]),