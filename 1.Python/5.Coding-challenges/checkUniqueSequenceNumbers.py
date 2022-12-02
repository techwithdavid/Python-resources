def check_distinct(data_list):
 if len(data_list) == len(set(data_list)):
   return True
 else:
   return False


print(check_distinct([1, 6, 5, 8]))  # Prints True
print(check_distinct([2, 2, 5, 5, 7, 8]))  # Prints False
