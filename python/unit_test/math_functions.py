import math # Needed for square root function


# Add two numbers
def add(x,y):
	return x + y


# Multiply two numbers
def multiply(x, y):
	return x * y
	
# Divide numbers
def divide(x, y):
	if y == 0:
		return None # Invalid, cannot divide by zero !
	else:
		return x / y


# Square root	
def square_root(x):
	if x < 0:
		return None # Invalid, cannot have a negative sqaure root !
	else:
		return math.sqrt(x)
	
