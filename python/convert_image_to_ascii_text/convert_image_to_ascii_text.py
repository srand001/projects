
#----------------------------------------------------------------------------------------------
# Convert an image to a black and white ASCII code text only.
#
# Notes:
#
# Images with strong distinctions between light highlights and deep shadows 
# produce the best text art.
#
# Make sure you open the generated .txt file using a monospaced (fixed-width) font like 
# Courier New, Consolas, or Fira Code, otherwise the rows will not align correctly.
# 
# Requires the 'Pillow' image library.
#
# pip install Pillow
#
# Designed by Surjit Randhawa 2026
#----------------------------------------------------------------------------------------------

import sys
from PIL import Image

# ASCII characters ordered from darkest (heavy display weight) to lightest (blank spaces)
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    # Resize the image while maintaining aspect ratio and adjusting for character height.
    orig_width, orig_height = image.size
    
    # Calculate aspect ratio
    aspect_ratio = orig_height / orig_width
    
    # Text characters are taller than they are wide. 
    # A multiplier of 0.55 compensates for this vertical stretching.
    new_height = int(new_width * aspect_ratio * 0.55)
    
    return image.resize((new_width, new_height))

def grayscale_image(image):
    #Converts the image to grayscale (luminance 'L' mode).
    return image.convert("L")

def pixels_to_ascii(image):
    # Maps grayscale pixel values to corresponding ASCII characters.
    pixels = image.getdata()
    ascii_str = ""
    
    # Divide 256 grayscale values evenly across the available ASCII characters
    num_chars = len(ASCII_CHARS)
    
    for pixel_value in pixels:
        # Map 0-255 range directly to the index of our ASCII array
        index = pixel_value * num_chars // 256
        ascii_str += ASCII_CHARS[index]
        
    return ascii_str

def convert_image_to_ascii(image_path, new_width=100):
    # Main control function to execute the conversion pipeline.
    try:
        # Open the image file
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error: Unable to open image file '{image_path}'. {e}")
        return None

    # Step 1: Resize the image
    resized_image = resize_image(image, new_width)
    
    # Step 2: Convert to black and white grayscale
    gray_image = grayscale_image(resized_image)
    
    # Step 3: Get ASCII character string
    ascii_data = pixels_to_ascii(gray_image)
    pixel_count = len(ascii_data)
    
    # Step 4: Construct the final layout by splitting the string into rows
    ascii_image = "\n".join(
        [ascii_data[index : index + new_width] for index in range(0, pixel_count, new_width)]
    )
    
    return ascii_image

if __name__ == "__main__":
    IMAGE_PATH = "image.jpg" # Path to image file
   
    OUTPUT_FILE = "ascii_art.txt"  # Output file where the text will be saved
    
    OUTPUT_WIDTH = 120 # Determine the character width of your text file output

    print(f"Converting '{IMAGE_PATH}' to ASCII art...")
    ascii_art = convert_image_to_ascii(IMAGE_PATH, new_width=OUTPUT_WIDTH)
    
    if ascii_art:
        print(ascii_art)        # Print directly to the terminal console
        
        # Save the string array to a plain ASCII text file
        with open(OUTPUT_FILE, "w") as f:
            f.write(ascii_art)
        print(f"\nASCII art saved to '{OUTPUT_FILE}'")

