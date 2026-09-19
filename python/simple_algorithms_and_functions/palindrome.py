#--------------------------------------------------------------------------------------
# A palindrome is a word, number, phrase, or other sequence of symbols that reads the 
# same forwards and backwards. Check if a string is a palindrome.
#--------------------------------------------------------------------------------------
def palindrome(string):
	string1 = string.upper() # Uppercase
	string2 = string.upper()[::-1] # Uppercase and reversed
	
	print(f"{string} : ", end="")

	if (string1 == string2):
		print("True")
	else:
		print("False")
	
 
# Run tests
palindrome("orange")
palindrome("apple")
palindrome("madam")
palindrome("Pip")
palindrome("0770")