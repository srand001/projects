# Palindrome
# A palindrome is a word, number, phrase, or other sequence of symbols that reads the same forwards and backwards

def reverse_word(word):
	reversed = ""
	for letter in word:
		reversed = letter + reversed
	return reversed

def check_all_words(arr):
	for word in arr:
		if reverse_word(word) != word:
			return False
	return True
	
arr1 = ["madam", "rotor" ]
arr2 = ["madam", "rotor", "apple" ]

# Print 'True' if all words are palindomes

print ('Palindrome test 1:', check_all_words(arr1))
print ('Palindrome test 2:', check_all_words(arr2))