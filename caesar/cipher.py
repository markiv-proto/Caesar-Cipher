def caesar_encrypt(text: str, shift: int) -> str:
    result = "" 
    for char in text:
        if char.isupper():
            base = ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        elif char.islower():
            base = ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)

def caesar_bruteforce(text: str) -> dict:
    results = {}
    for shift in range(1, 26):
        results[shift] = caesar_decrypt(text, shift)
    return results