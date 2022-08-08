def sum(num):


if len(num) == 1:
    # with only one element in the list, the sum result will be equal to the element.
return num[0]
else:
return num[0] + sum(num[1:])
print(sum([2, 4, 5, 6, 7]))
