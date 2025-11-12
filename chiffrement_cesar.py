import string

def caesar_transform(text, shift):
    result = ""
    
    for character in text:
        if character in string.ascii_lowercase:
            current_position = string.ascii_lowercase.index(character)
            new_position = (current_position + shift) % 26
            result += string.ascii_lowercase[new_position]
        elif character in string.ascii_uppercase:
            current_position = string.ascii_uppercase.index(character)
            new_position = (current_position + shift) % 26
            result += string.ascii_uppercase[new_position]
        else:
            result += character
    
    return result

def caesar_cipher(text, shift):
    return caesar_transform(text, shift)

print("\n")
print(caesar_cipher("Hello World", 3))
print("\n")

def caesar_decipher(encrypted_text, shift):
    return caesar_transform(encrypted_text, -shift)

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

def vigenere_transform(text, key, encrypt):
    result = ""
    key_index = 0
    
    for character in text:
        if character in string.ascii_lowercase or character in string.ascii_uppercase:
            shift = string.ascii_lowercase.index(key[key_index % len(key)].lower())
            if not encrypt:
                shift = -shift
            result += caesar_transform(character, shift)
            key_index += 1
        else:
            result += character
    
    return result

def vigenere_cipher(text, key):
    return vigenere_transform(text, key, True)

print(vigenere_cipher("Hello World", "key"))

def vigenere_decipher(encrypted_text, key):
    return vigenere_transform(encrypted_text, key, False)

encrypted = vigenere_cipher("Hello World", "key")
print(f"Encrypted: {encrypted}")
print("\n")
print(f"Decrypted: {vigenere_decipher(encrypted, 'key')}")