# This program calculates the square of a number
# and prints the result to the console.

# Define a function to calculate the square
def calculate_square(number):
	return number ** 2

# Input: Get a number from the user
num = int(input("Enter a number: "))

# Process: Calculate the square of the number
square = calculate_square(num)

# Output: Display the result
print(f"The square of {num} is {square}")