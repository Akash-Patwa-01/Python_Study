
# quick quiz 
# if-else statement

age = int(input("Enter your age:"))

if(age>=18):
	print("yes")

else:
	print("no")


# if-elif-else statement


a  = int(input("Enter your age:"))
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

 
print("End of program") # printing outside the if-else block


