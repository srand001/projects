#---------------------------------------------------------------------------------------
# This program reads a text file, line by line. 
# Read every line and reverse the words. 
# Then write the new lines to a new file.
#
# Designed by Surjit Randhawa 2026
#---------------------------------------------------------------------------------------

def reverse_words_in_file(file1, file2):
  with open(file1,"r") as f1, open(file2,"w") as f2:
    for l1 in f1:
      words1 = l1.strip()
      arr1 = words1.split()
      arr1.reverse()
      l1 = " ".join(arr1)
      f2.write(l1 + "\n")
      
input_file = "harry_potter.txt" # This is the file to be read
output_file = "output.txt"      # This is the output file
reverse_words_in_file(input_file, output_file)
