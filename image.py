from PIL import Image
import numpy as np
import os

# Function to encrypt an image by shifting pixel values
def encrypt_image(image_path, shift, output_path):
    # Check if the input image file exists
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
        return
    
    # Open the image and convert it to a NumPy array
    image = Image.open(image_path)
    image_array = np.array(image)

    # Encrypt the image by adding the shift value to each pixel and wrapping around using modulo 256
    encrypt_array = (image_array + shift) % 256

    # Convert the encrypted array back to an image and save it
    encrypt_image = Image.fromarray(encrypt_array.astype('uint8'))
    encrypt_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

# Function to decrypt an image by reversing the pixel value shift
def decrypt_image(image_path, shift, output_path):
    # Check if the input image file exists
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
        return
    
    # Open the image and convert it to a NumPy array
    image = Image.open(image_path)
    image_array = np.array(image)

    # Decrypt the image by subtracting the shift value from each pixel and wrapping around using modulo 256
    decrypt_array = (image_array - shift) % 256

    # Convert the decrypted array back to an image and save it
    decrypt_image = Image.fromarray(decrypt_array.astype('uint8'))
    decrypt_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# Main function to handle user interaction
def main():
    while True:
        # Display menu options
        print("\nImage Encryption/Decryption Tool")
        choice = input("Type 'e' to encrypt an image, 'd' to decrypt an image, or 'q' to quit: ").lower()

        # Exit the loop and program if user chooses 'q'
        if choice == 'q':
            print("Exiting the program.")
            break
        # Handle encryption and decryption choices
        elif choice in ('e', 'd'):
            # Prompt user for necessary inputs
            image_path = input("Enter the path to the image: ")
            shift = int(input("Enter the shift value: "))
            output_path = input("Enter the output path for the processed image: ")

            # Encrypt or decrypt based on user choice
            if choice == 'e':
                encrypt_image(image_path, shift, output_path)
            else:
                decrypt_image(image_path, shift, output_path)
        else:
            print("Invalid choice. Please try again.")

# Entry point for the program
if __name__ == "__main__":
    main()
