# Function to encrypt the string  
def encrypt(text, s):  
    result = ""  
  
    # Traverse the text  
    for i in range(len(text)):  
        char = text[i]  
  
        # Encrypt uppercase characters  
        if (char.isupper()):  
            result += chr((ord(char) + s - 65) % 26 + 65)  
  
        # Encrypt lowercase characters  
        else:  
            result += chr((ord(char) + s - 97) % 26 + 97)  
  
    return result  
  
# Function to decrypt the string  
def decrypt(text, s):  
    result = ""  
  
    # Traverse the text  
    for i in range(len(text)):  
        char = text[i]  
  
        # Decrypt uppercase characters  
        if (char.isupper()):  
            result += chr((ord(char) - s - 65) % 26 + 65)  
  
        # Decrypt lowercase characters  
        else:  
            result += chr((ord(char) - s - 97) % 26 + 97)  
  
    return result  
  
# Test the code  
text = "HELLO WORLD"  
s = 4  
print("Text: " + text)  
print("Shift: " + str(s))  
print("Cipher: " + encrypt(text, s))  
print("Decipher: " + decrypt(encrypt(text, s), s))  
