#----------------------------------------------------------------------
# Reverse a string in Python
# 
# Shows 3 different methods to reverse a string.
#
# Designed by Surjit Randhawa 2026
#----------------------------------------------------------------------

# Reverse string one letter at a time
def reverse1(string):
	reverse = ""
	for c in string:
		reverse = c + reverse
	return reverse

# Note: Use the slicing method.
# Set the step equal to -1, then you can build a slice that retrieves all the characters in reverse order
def reverse2(string):
	reverse = string.upper()[::-1]	
	return reverse


# Note: reversed() function in Python returns an iterator that accesses elements in reverse order.
# So we need to join the elements back together to make a string
def reverse3(string):
	reverse = "".join(reversed(string))
	return reverse
	


example = "123"
print("Reverse1: ", reverse1(example))
print("Reverse2: ", reverse2(example))
print("Reverse3: ", reverse3(example))
		