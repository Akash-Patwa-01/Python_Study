marks1 = int(input("Enter your marks1 : "))
marks2 = int(input("Enter your marks2 : "))
marks3 = int(input("Enter your marks3 : "))	

total_percentage = (marks1 + marks2 + marks3)/300 *100

if(total_percentage >= 40 and marks1 >=33 and marks2>= 33 and marks3>= 33):
	print(f"you are passed with {total_percentage} %")

else:
	print(f"you are failed, {total_percentage} try next time keep growing")

