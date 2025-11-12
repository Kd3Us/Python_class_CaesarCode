import string

def caesar_cipher(text, shift):
    alphabet = string.ascii_lowercase
    encrypted_text = ""
    
    for character in text:
        if character in alphabet:
            current_position = alphabet.index(character)
            new_position = (current_position + shift) % 26
            new_letter = alphabet[new_position]
            encrypted_text += new_letter
        elif character in string.ascii_uppercase:
            current_position = string.ascii_uppercase.index(character)
            new_position = (current_position + shift) % 26
            new_letter = string.ascii_uppercase[new_position]
            encrypted_text += new_letter
        else:
            encrypted_text += character
    
    return encrypted_text

print("\n")
print(caesar_cipher("Hello World", 3))
print("\n")

def caesar_decipher(encrypted_text, shift):
    alphabet = string.ascii_lowercase
    decrypted_text = ""
    
    for character in encrypted_text:
        if character in alphabet:
            current_position = alphabet.index(character)
            new_position = (current_position - shift) % 26
            new_letter = alphabet[new_position]
            decrypted_text += new_letter
        elif character in string.ascii_uppercase:
            current_position = string.ascii_uppercase.index(character)
            new_position = (current_position - shift) % 26
            new_letter = string.ascii_uppercase[new_position]
            decrypted_text += new_letter
        else:
            decrypted_text += character
    
    return decrypted_text

print(caesar_decipher("Khoor Zruog", 3))
print("\n")

def brute_force_caesar(encrypted_text):
    print(f"=== Brute force on: '{encrypted_text}' ===")
    for shift in range(1, 26):
        result = caesar_decipher(encrypted_text, shift)
        print(f"Shift {shift:2d}: {result}")
    print(f"=== End of Brut force ===")
    print(f"\n")

brute_force_caesar("Wklv Lv D Vhfuhw")

def vigenere_cipher(text, key):
    alphabet = string.ascii_lowercase
    encrypted_text = ""
    key_index = 0
    
    for character in text:
        if character in alphabet or character in string.ascii_uppercase:
            shift = alphabet.index(key[key_index % len(key)].lower())
            encrypted_char = caesar_cipher(character, shift)
            encrypted_text += encrypted_char
            key_index += 1
        else:
            encrypted_text += character
    
    return encrypted_text

print(vigenere_cipher("Hello World", "key"))

def vigenere_decipher(encrypted_text, key):
    alphabet = string.ascii_lowercase
    decrypted_text = ""
    key_index = 0
    
    for character in encrypted_text:
        if character in alphabet or character in string.ascii_uppercase:
            shift = alphabet.index(key[key_index % len(key)].lower())
            decrypted_char = caesar_decipher(character, shift)
            decrypted_text += decrypted_char
            key_index += 1
        else:
            decrypted_text += character
    
    return decrypted_text

encrypted = vigenere_cipher("Hello World", "key")
print(f"Encrypted: {encrypted}")
print("\n")
print(f"Decrypted: {vigenere_decipher(encrypted, 'key')}")