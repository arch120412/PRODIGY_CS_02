from PIL import Image
import numpy as np

def encrypt_image(image_path, encryption_key, output_path):
    try:
        # Open the image
        image = Image.open(image_path)
        image_array = np.array(image)

        # Pixel addition
        encrypted_array = (image_array + encryption_key) % 256

        # Create encrypted image
        encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))

        # Save the encrypted image
        encrypted_image.save(output_path)
        print(f"Encrypted image saved to {output_path}")
    except FileNotFoundError:
        print(f"File not found: {image_path}")

def decrypt_image(image_path, decryption_key, output_path):
    try:
        # Open the encrypted image
        image = Image.open(image_path)
        image_array = np.array(image)

        # Subtract decryption key
        decrypted_array = (image_array - decryption_key) % 256

        # Generate decrypted image
        decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))

        # Save the decrypted image
        decrypted_image.save(output_path)
        print(f"Decrypted image saved to {output_path}")
    except FileNotFoundError:
        print(f"File not found: {image_path}")


if __name__ == "__main__":

   
    operation = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").strip().lower()
    
    if operation == 'e':
        image_path = input("Enter the path of the image to encrypt: ").strip()
        encryption_key = int(input("Enter the encryption key (an integer): ").strip())
        output_path = input("Enter the output path for the encrypted image: ").strip()
        encrypt_image(image_path, encryption_key, output_path)
        
    elif operation == 'd':
        image_path = input("Enter the path of the image to decrypt: ").strip()
        decryption_key = int(input("Enter the decryption key (an integer): ").strip())
        output_path = input("Enter the output path for the decrypted image: ").strip()
        decrypt_image(image_path, decryption_key, output_path)
    else:
        print("Invalid operation. Please enter 'E' for encryption or 'D' for decryption.")
