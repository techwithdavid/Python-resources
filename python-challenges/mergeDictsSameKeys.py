from collections import Counter
d1 = {'key1': 50, 'key2': 100, 'key3': 200}
d2 = {'key1': 200, 'key2': 100, 'key4': 300}
new_dict = Counter(d1) + Counter(d2)
print(new_dict)
