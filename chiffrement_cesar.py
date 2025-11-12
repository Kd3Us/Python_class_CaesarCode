import string
import re

def caesar_transform(text, shift):
    result = []
    
    for character in text:
        unicode_value = ord(character)
        shifted_value = (unicode_value + shift) % 1114112
        result.append(chr(shifted_value))
    
    return ''.join(result)

def caesar_cipher(text, shift):
    return caesar_transform(text, shift)

print("\n")
caesar_text = input("Entrez le texte à chiffrer avec César: ")
caesar_shift = int(input("Entrez le décalage pour César: "))
encrypted_caesar = caesar_cipher(caesar_text, caesar_shift)
print(f"Texte chiffré: {encrypted_caesar}")
print("\n")

def caesar_decipher(encrypted_text, shift):
    return caesar_transform(encrypted_text, -shift)

def is_latin_text(text):
    latin_pattern = re.compile(r'^[a-zA-ZÀ-ÿ\s\.,;:!?\'"()-]+$')
    return latin_pattern.match(text) is not None

def brute_force_caesar(encrypted_text):
    print(f"Brute force on: '{encrypted_text}'")
    for shift in range(1, 1114112):
        result = caesar_decipher(encrypted_text, shift)
        if is_latin_text(result):
            print(f"Shift {shift:7d}: {result}")
    print(f"End of Brut force")
    print(f"\n")

brute_force_caesar(encrypted_caesar)

def vigenere_transform(text, key, encrypt):
    result = []
    key_index = 0
    
    for character in text:
        shift = ord(key[key_index % len(key)])
        if not encrypt:
            shift = -shift
        result.append(caesar_transform(character, shift))
        key_index += 1
    
    return ''.join(result)

def vigenere_cipher(text, key):
    return vigenere_transform(text, key, True)

vigenere_text = input("Entrez le texte à chiffrer avec Vigenère: ")
vigenere_key = input("Entrez la clé pour Vigenère: ")
encrypted_vigenere = vigenere_cipher(vigenere_text, vigenere_key)
print(f"Texte chiffré: {encrypted_vigenere}")

def vigenere_decipher(encrypted_text, key):
    return vigenere_transform(encrypted_text, key, False)

print(f"Texte déchiffré: {vigenere_decipher(encrypted_vigenere, vigenere_key)}")