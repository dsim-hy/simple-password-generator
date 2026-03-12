# Importing Modules
import secrets
import string


def get_yes_no(prompt):
    """Ask a yes/no question and return True or False."""
    print(prompt)
    while True:
        response = input("Answer (Y/N): ").strip().lower()
        if response in ("y", "yes"):
            return True
        elif response in ("n", "no"):
            return False
        print("Please enter Y or N.")


def get_character_types():
    """Ask user which character types to include; return (use_letters, use_numbers, use_symbols)."""
    while True:
        use_letters = get_yes_no("Do you want alphabets (A-Z) in your password?")
        use_numbers = get_yes_no("Do you want numbers (0-9) in your password?")
        use_symbols = get_yes_no("Do you want symbols in your password?")
        if not (use_letters or use_numbers or use_symbols):
            print("You need to have at least one type of character.")
        else:
            return use_letters, use_numbers, use_symbols


def build_character_set(use_letters, use_numbers, use_symbols):
    """Build and return the pool of characters based on selected types."""
    return "".join([
        string.ascii_letters if use_letters else "",
        string.digits if use_numbers else "",
        string.punctuation if use_symbols else "",
    ])


def get_password_length():
    """Prompt the user for a password length and validate it (1–128)."""
    while True:
        length_input = input("Enter the password length (Minimum 1, Maximum 128): ").strip()
        if length_input.isnumeric():
            length = int(length_input)
            if length <= 0:
                print("Minimum 1 character is required.")
            elif length > 128:
                print("Maximum of 128 characters is allowed.")
            else:
                return length
        else:
            print("Please enter a valid number.")


def get_num_passwords():
    """Ask how many passwords to generate (1–10)."""
    while True:
        count_input = input("How many passwords do you want to generate? (1–10): ").strip()
        if count_input.isnumeric():
            count = int(count_input)
            if 1 <= count <= 10:
                return count
            print("Please enter a number between 1 and 10.")
        else:
            print("Please enter a valid number.")


def generate_password(characters, length):
    """Generate a single cryptographically secure password."""
    return "".join(secrets.choice(characters) for _ in range(length))


def get_password_strength(length, use_letters, use_numbers, use_symbols):
    """Return a human-readable password strength label."""
    variety = sum([use_letters, use_numbers, use_symbols])
    if length >= 12 and variety == 3:
        return "Strong"
    elif length >= 8 and variety >= 2:
        return "Moderate"
    else:
        return "Weak"


def main():
    use_letters, use_numbers, use_symbols = get_character_types()
    characters = build_character_set(use_letters, use_numbers, use_symbols)
    length = get_password_length()
    count = get_num_passwords()
    strength = get_password_strength(length, use_letters, use_numbers, use_symbols)

    print()
    for i in range(count):
        password = generate_password(characters, length)
        label = f"Password {i + 1}:" if count > 1 else "Generated Password:"
        print(f"{label} {password}")
    print(f"Password Strength:  {strength}")


if __name__ == "__main__":
    main()