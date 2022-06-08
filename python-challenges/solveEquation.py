ax + by = c
mx + ny = o

a, b, c, m, n, o = 5, 9, 4, 7, 9, 4
temp = a*n - b*m
if n != 0:
   x = (c*n - b*o) / temp
   y = (a*o - m*c) / temp
   print(str(x), str(y))
