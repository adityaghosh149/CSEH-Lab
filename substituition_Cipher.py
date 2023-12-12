def encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - shift + key) % 26 + shift)
            cipher_text += shifted_char
        else:
            cipher_text += char
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - shift - key) % 26 + shift)
            plain_text += shifted_char
        else:
            plain_text += char
    return plain_text


while True:
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Quit")
    user_input = input("Enter your choice : ")
    choice = user_input.strip().lower()

    if choice == "1":
        text = input("Enter the text to encrypt: ")
        key = int(input("Enter key : "))
        cipher_text = encrypt(text, key)
        print(f"Cipher Text: {cipher_text}")
    elif choice == "2":
        text = input("Enter the text to decrypt: ")
        key = int(input("Enter key : "))
        plain_text = decrypt(text, key)
        print(f"Plain Text: {plain_text}")
    elif choice == "3":
        break
    else:
        print("Invalid option! Please try again")
    print()
