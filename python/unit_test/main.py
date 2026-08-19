
# main.py  - Some simple functions to demonstrate unit tests
# Surjit Randhawa 2026


# Function to return "hot" if temperature > 20 else return false
def getWeather(temperature):
	if temperature > 20:
		return "hot"
	else:
		return "cold"

 # Return true if string is a palindrome, else return false
def checkPalindrome(string):
	if string == None:       # Check for Null values
		return False
	else:
	  return (string.upper() == string.upper()[::-1])
 
