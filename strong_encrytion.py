from cryptography.fernet import Fernet  
  
# Generate a key  
key = Fernet.generate_key()  
cipher_suite = Fernet(key)  
  
# Function to encrypt a message  
def encrypt(message):  
    cipher_text = cipher_suite.encrypt(message)  
    return cipher_text  
  
# Function to decrypt a message  
def decrypt(cipher_text):  
    plain_text = cipher_suite.decrypt(cipher_text)  
    return plain_text  
  
# Test the code  
message = b'HELLO WORLD'  
print("Original message:", message)  
encrypted_message = encrypt(message)  
print("Encrypted message:", encrypted_message)  
print("Decrypted message:", decrypt(encrypted_message))  
