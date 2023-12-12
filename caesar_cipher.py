def encrypt(plain_text, key):
    cipher_text = ""
    for letter in plain_text:
        if letter.isalpha():
            base = 97 if letter.islower() else 65
            cipher_text += chr((ord(letter) + key - base) % 26 + base)
        else:
            cipher_text += letter
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""
    for letter in cipher_text:
        if letter.isalpha():
            base = 97 if letter.islower() else 65
            plain_text += chr((ord(letter) - key - base) % 26 + base)
        else:
            plain_text += letter
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
        if key < 0 or 25 < key:
            print("Key should not be less than 0 or more than 25")
            print("")
            continue
        cipher_text = encrypt(text, key)
        print(f"Cipher Text: {cipher_text}")
    elif choice == "2":
        text = input("Enter the text to decrypt: ")
        key = int(input("Enter key : "))
        if key < 0 or 25 < key:
            print("Key should not be less than 0 or more than 25")
            print("")
            continue
        plain_text = decrypt(text, key)
        print(f"Plain Text: {plain_text}")
    elif choice == "3":
        break
    else:
        print("Invalid option! Please try again")
    print()
