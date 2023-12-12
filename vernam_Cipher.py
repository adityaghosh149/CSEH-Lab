def encrypt(plain_text, key):
    cipher_text = ""
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            base = ord('A') if plain_text[i].isupper() else ord('a')
            cipher_text += chr((ord(plain_text[i]) - base + ord(key[i]) - base) % 26 + base)
        else:
            cipher_text += plain_text[i]
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            base = ord('A') if cipher_text[i].isupper() else ord('a')
            plain_text += chr((ord(cipher_text[i]) - base - (ord(key[i]) - base) + 26) % 26 + base)
        else:
            plain_text += cipher_text[i]
    return plain_text


while True:
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Quit")
    user_input = input("Enter your choice : ")
    choice = user_input.strip().lower()

    if choice == "1":
        text = input("Enter the text to encrypt: ")
        key = input("Enter key : ")
        if len(text) != len(key):
            print("Length of the key should be same as length of the text")
            print("Try again")
            continue
        cipher_text = encrypt(text, key)
        print(f"Cipher Text: {cipher_text}")
    elif choice == "2":
        text = input("Enter the text to decrypt: ")
        key = input("Enter key : ")
        if len(text) != len(key):
            print("Length of the key should be same as length of the text")
            print("Try again")
            continue
        plain_text = decrypt(text, key)
        print(f"Plain Text: {plain_text}")
    elif choice == "3":
        break
    else:
        print("Invalid option! Please try again")
    print()
