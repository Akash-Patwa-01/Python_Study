# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = int(input("Enter c : "))

a = 1
b = 5
c = 2

def greatest(a ,  b , c):
	if(a>b and a>c):
		return a 
	elif(b>a and b>c):
		return b
	else:
		return c
	
print(greatest(a , b , c))
  