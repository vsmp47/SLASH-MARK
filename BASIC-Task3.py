import random

def make_password(length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    password = ""

    for i in range(length):
        next_letter_index = random.randrange(len(alphabet))
        password += alphabet[next_letter_index]

    password = add_number(password)
    password = add_uppercase_letter(password)

    return password

def add_number(word):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(word)//2)
        word = word[0:replace_index] + str(random.randrange(10)) + word[replace_index+1:]
    return word

def add_uppercase_letter(word):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(word)//2, len(word))
        word = word[0:replace_index] + word[replace_index].upper() + word[replace_index+1:]
    return word

def main():
    num_passwords = int(input("How many passwords do you want to make? "))
    print("Making " + str(num_passwords) + " passwords")

    password_lengths = []

    print("Minimum password length is 3")

    for i in range(num_passwords):
        length = int(input("How long should Password #" + str(i+1) + " be? "))
        if length < 3:
            length = 3
        password_lengths.append(length)

    passwords = []

    for length in password_lengths:
        passwords.append(make_password(length))

    for i, password in enumerate(passwords):
        print("Password #" + str(i+1) + " is " + password)

main()
