DICT = {'a':1, 'b':3, 'c':4, 'd':6, 'e':"efg"}

print(DICT.items())
print(DICT.keys())
DICT.update({'a':9,})
print(DICT)

print(DICT.get('a2')) # it give none get method is used to get the value of a key in the dictionary 
print(DICT["a"]) # it give error   method is used to get the value of a key in the dictionary
print(DICT.pop('a')) # it remove the key and value from the dictionary
print(DICT)
print(DICT.popitem()) # it remove the last key and value from the dictionary
print(DICT)
print(DICT.setdefault('a', 5)) # it set the value of a key in the dictionary if the key is not present in the dictionary