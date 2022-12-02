arr = [5,3,4,,8,7,5,1,2,3]
print(arr)

for j in range(1, len(arr)):
    actual = arr[j]

    i = j-1
    while i >= 0 and arr[i]> actual:
        arr[i+1] = arr[i]
        i -= 1
    arr[i + 1] = actual
    
print(arr)