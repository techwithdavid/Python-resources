def quick_sort(array, low, high):
  if low < high:
    # Dividir y acomodar pivote
    pi = partition(array, low, high)
  
    quick_sort(array, low, pi - 1)
    quick_sort(array, pi + 1, high)
 
def partition(array, low, high):  
  # Pivote el de la derecha
  pivot = array[high]
  
  # Apuntador del último elemento más pequeño
  i = low - 1
 
  for j in range(low, high):
    if array[j] <= pivot:
      # Avanzar apuntador
      i = i + 1
      # Intercambiar elementos
      (array[i], array[j]) = (array[j], array[i])
  
  # Al final intercambiar el pivote
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  
  # Regresa la posición final del pivote
  return i + 1
 
arr = [4,6,2,5,8,9,5,10]
print(arr)
quick_sort(arr, 0, len(arr)-1)
print(arr)