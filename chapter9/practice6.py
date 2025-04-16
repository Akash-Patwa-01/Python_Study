with open("log.txt.html") as f:
	content = f.read()

if("python" in content):
	print("Yes python is pesent")

else:
	print("No python is present")