name = "Akash" # single line string 
name1 = '''Akash 
			Kumar''' # multi line string

# string is immutable
# name[0] = "a" # this will give an error	


nameshort = name[0:3] # slashing
print(nameshort)

print(name[-4:-1])
print(name[1:4])

print(name[:3]) # this will give the same result as name[0:3]
print(name[1:]) # this will give the same result as name[1:len(name)]
print(name[:]) # this will give the same result as name[0:len(name)]

# slicing with  skip value 
print(name1[1:4:2]) # this will give the same result as name[0:4:2]
