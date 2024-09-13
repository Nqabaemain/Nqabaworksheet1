# Variable Declaration
a = 15
b = 12

# Print the types of variables a and b
print("Type of a:", type(a))
print("Type of b:", type(b))

# Perform Addition
result_add = a + b

# Print the Result
print("Addition (a + b):", result_add)

# Perform Subtraction
result_subtract = a - b

# Print the Result
print("Subtraction (a - b):", result_subtract)

# Perform Multiplication
result_multiply = a * b

# Print the Result
print("Multiplication (a * b):", result_multiply)

# Perform Division
result_divide = a / b

# Print the Result
print("Division (a / b):", result_divide)

# Perform Division and Ensure c is of type integer
c = int(a // b)

# Print the value and type of c
print("Value of c:", c)
print("Type of c:", type(c))

# Convert c to a float
c_float = float(c)

# Print the new value and type of c_float
print("Value of c as float:", c_float)
print("Type of c as float:", type(c_float))
# Perform Division and Ensure c is of type integer
c = a // b  # Using integer division to get an integer result

# Declare a string variable
message = "The result of a divided by b is:"

# Concatenate the message with the value of c (converted to a string) and print the result
result_message = message + " " + str(c)
print(result_message)
# Compare if an is greater than b
result_greater = a > b

# Print the result (True/False)
print("a > b:", result_greater)
# Check if an is equal to b
result_equal = a == b

# Print the result (True/False)
print("a == b:", result_equal)