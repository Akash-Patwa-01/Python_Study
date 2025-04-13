a  = int(input("Enter your age:"))

# if statement no :1
if(a%2 == 0):
	print("a is even")  # if is independent

# End of statement no :1
else:
	print("a is odd")

# if statement no:2	
if(a>=18):
	print("You are above the age of consent")
	print("You are eligible to vote")

elif(a<0):
	print("You are not borned yet")
	print(f"You will aftar after {abs(a)} years")

elif(a>=80):
	print("You are above the age of consent")
	print("You are eligible to vote")
	print("You are a senior citizen")

else:
	print("You are not above the age of consent")
	print("You are not eligible to vote")

# End the statement no: 2	

 
print("End of program") 