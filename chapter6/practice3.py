p1 = "make a lot of money"
p2 = "subscribe this"
p3 = "buy now"
p4 = "click link"


message = input("Enter a message: ")


if((p1 in message) or (p2 in message) or (p1 in message)):
	print("This comments is a spam")

else:
	print("This is not a spam")


