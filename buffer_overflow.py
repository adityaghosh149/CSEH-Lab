def is_valid(password):
    if len(password) < 8:
        print("Password has less than 8 character!")
        return False

    if not password[0].isupper():
        print("First character of the password is not uppercase!")
        return False

    contain_digit = False
    for letter in password:
        if letter.isdigit():
            contain_digit = True
            break
    if not contain_digit:
        print("Password does not contain any digit!")
        return False

    if not password[-1].islower():
        print("Last character of the password is not lowercase!")
        return False

    return True


valid = False
while not valid:
    password = input("Enter password : ")
    valid = is_valid(password)
    if valid:
        print("Success!")
    else:
        print("Try Again!")
    print()

