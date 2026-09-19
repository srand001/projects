#----------------------------------------------------------------------
# Check if a word is an anagram of another word
#----------------------------------------------------------------------

def isAnagram(word1, word2):
 		# Convert to lowercase to make the check case-insensitive
    word1 = word1.lower()
    word2 = word2.lower()
    
    print(f"{word1}, {word2} : ", end = "")
    
    # Check if the sorted characters of both words match
    if sorted(word1) == sorted(word2):
      print("True")
    else:
      print("False")

isAnagram("abc","ccc")
isAnagram("abc","cba")
isAnagram("abc","acb")
isAnagram("abc","cba")

# -->
# False
# True
# True
# True

        