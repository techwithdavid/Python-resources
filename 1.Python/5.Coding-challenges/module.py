print(7/3)
print(7/3.0)
print(8 / 3)
print(8 % 3)

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(isEven(151))

def convertToHM(mins):
    hours = mins / 60
    minutes = mins % 60
    return str(hours) + ':' + str(minutes)

print(convertToHM(1024))