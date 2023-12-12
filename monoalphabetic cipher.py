alphabets = {
    'a': 'm', 'b': 'n', 'c': 'b', 'd': 'v', 'e': 'c', 'f': 'x', 'g': 'z',
    'h': 'a', 'i': 's', 'j': 'd', 'k': 'f', 'l': 'g', 'm': 'h', 'n': 'j',
    'o': 'k', 'p': 'l', 'q': 'p', 'r': 'o', 's': 'i', 't': 'u', 'u': 'y',
    'v': 't', 'w': 'r', 'x': 'e', 'y': 'w', 'z': 'q',
}


def encrypt(plain_text):
    cipher_text = ''
    for letter in plain_text:
        if letter.isupper():
            cipher_text += alphabets[letter.lower()].upper()
        elif letter.islower():
            cipher_text += alphabets[letter]
        else:
            cipher_text += letter
    return cipher_text


def decrypt(cipher_text):
    plain_text = ''
    for letter in cipher_text:
        if letter.isupper():
            index = list(alphabets.values()).index(letter.lower())
            plain_text += list(alphabets.keys())[index].upper()
        elif letter.islower():
            index = list(alphabets.values()).index(letter)
            plain_text += list(alphabets.keys())[index]
        else:
            plain_text += letter
    return plain_text


while True:
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Quit")
    user_input = input("Enter your choice : ")
    choice = user_input.strip()

    if choice == "1":
        text = input("Enter text to encrypt: ")
        cipher_text = encrypt(text)
        print(f"Cipher Text: {cipher_text}")
    elif choice == "2":
        text = input("Enter text to decrypt: ")
        plain_text = decrypt(text)
        print(f"Plain Text: {plain_text}")
    elif choice == "3":
        break
    else:
        print("Invalid option! Please try again")
    print()
