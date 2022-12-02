arr = [4,2,7,12,9,4,1]

for i in range(0, len(arr)):
    minimo = 1
    for j in range(i+1, len(arr)):
        if arr[minimo] > arr[j]
            minimo = j

    temp = arr[i]
    arr[i] = arr[minimo]
    arr[minimo] = temp

print(arr)