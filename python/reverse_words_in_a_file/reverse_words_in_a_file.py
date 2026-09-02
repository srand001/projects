def reverse_words_in_file(input_file, output_file):
    # Open the source file for reading and the new file for writing
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        
        # Process the file line by line to keep it memory-efficient
        for line in infile:
            # Strip the trailing newline character, if it exists
            stripped_line = line.rstrip('\n')
            
            # Split the line into individual words
            words = stripped_line.split(' ')
            
            # Reverse the letters of each word
            reversed_words = [word[::-1] for word in words]
            
            # Join the reversed words back into a sentence
            new_line = ' '.join(reversed_words)
            
            # Write the modified line with its original newline character back
            outfile.write(new_line + '\n')

input_file = "harry_potter.txt" # This is the file to be read
output_file = "output.txt"      # This is the output file
reverse_words_in_file(input_file, output_file)

