string = "Coding challenges are the best"
num = '50'
lookfor = 'are'

print (string)
print (string.replace(lookfor, 'are not')) # replace the string
print(string.swapcase()) # swap the case of string
print(string[::-1])

len(string) # lenght of string
print(num.isalnum()) # check if string is alphanumeric 
print(string.isalpha()) # check if string is alphabetic
print(string.isdigit()) # 
print(string.find(lookfor)) # find the index of the string
print(string[string.find(lookfor):18]) # find the chatacter in index 
print(string.istitle()) # check if string is title
print(list(string)) # convert string to list
print(string.isupper()) # check if string is title
