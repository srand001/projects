# Palindrome
# A palindrome is a word, number, phrase, or other sequence of symbols that reads the same forwards and backwards.
# Check if a string is a palindrome.
# Use slicing notation to reverse the string
# [::-1] is advanced slicing. [a:b:c] means slice from a (inclusive) to b (exclusive) with step size c
# This is a case insensitive function

def palindrome(string): 
  return (string.upper() == string.upper()[::-1]) 
  
  
# Run tests
print("test 1 : ", palindrome("apple"))
print("test 2 : ", palindrome("madam"))
