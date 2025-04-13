a1 = int(input("Enter your number1:"))
a2 = int(input("Enter your number2:"))
a3 = int(input("Enter your number3:"))
a4 = int(input("Enter your number4:"))


if(a1>a2 and a1>a3 and a1>a4):
	print(f"{a1} is the largest number")
elif(a2>a1 and a2>a3 and a2>a4):
	print(f"{a2} is the largest number")
elif(a3>a1 and a3>a2 and a3>a4):
	print(f"{a3} is the largest number")
else:
	print(f"{a4} is the largest number")