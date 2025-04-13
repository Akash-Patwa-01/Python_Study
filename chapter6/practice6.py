
Marks = int(input("Enter your percentage: "))

if(Marks >= 90 or Marks == 100):
	print("Grade Ex")
elif(Marks >= 80 or Marks == 89):
	print("Grade A")
elif(Marks >= 70 or Marks == 79):
	print("Grade B")
elif(Marks >= 60 or Marks == 69):
	print("Grade C")
elif(Marks >= 50 or Marks == 59):
	print("Grade D")
else:
	print("Grade F")

print(f"Your percentage is: {Marks}")

