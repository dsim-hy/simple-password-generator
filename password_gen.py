# Importing Modules
import secrets
import string

# Check True or False answers
def answer():
    while True:
        answer = input("Answer (Y/N): ").lower()
        if answer == "y" or answer == "yes":
            return 1
        elif answer == "n" or answer == "no":
            return 0

# Ask for character type
def add_letters():
    print("Do you want alphabets (A-Z) in your password?")
    return answer()

def add_numbers():
    print("Do you want numbers (0-9) in your password?")
    return answer()

def add_symbols():
    print("Do you want symbols in your password?")
    return answer()

# Defining Password Characters
while True:
    letters = add_letters()
    numbers = add_numbers()
    symbols = add_symbols()
    if not (letters or numbers or symbols):
        print("You need to have at least one type of character.")
    else:
        break

# Defining Password Lengths
while True:
    lengths_input = input("Enter the password length (Minimum 1): ")
    if lengths_input.isnumeric():
        # Convert str into int
        lengths = int(lengths_input)
        if (lengths <= 0):
            print("Minimum 1 character is required.")
        elif (lengths > 129):
            print("Maximum of 128 characters is allowed.")
        else:
            break
    else:
        print("Please enter a number.")

# Make characters based on user's input
characters = "".join([string.ascii_letters if letters else "", string.digits if numbers else "", string.punctuation if symbols else ""])

# Building password based on user defined length
password = ""
for i in range(lengths):
    password += secrets.choice(characters)

# Output Password
print("Generated Password: ", password)