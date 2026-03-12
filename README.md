# Simple Password Generator

A simple command-based password generator made with Python. This program can generate a random set of passwords based on the user's criteria.

## Features

- Choose which character types to include:
  - Alphabets (A-Z, a-z)
  - Numbers (0-9)
  - Symbols (punctuation)
- Set password length (1–128 characters)
- Generate up to 10 passwords in one run
- Password strength indicator (Weak / Moderate / Strong)
- Cryptographically secure randomness via the `secrets` module

## Prerequisites

To run the script, you will need to have [Python (3.6 and above)](https://python.org/) installed on your local machine.

## Instructions

Follow these steps to run the password generator:
1. Download or clone this repository to your local machine
2. Open your command prompt or terminal and navigate to the location of the files
3. Enter the following command: `python password_gen.py`
4. Follow the on-screen prompts to choose your password criteria
5. The generated password(s) and strength rating will be displayed

## Running the Tests

Unit tests are provided in `test_password_gen.py`. Install [pytest](https://pytest.org/) and run:

```bash
pip install pytest
pytest test_password_gen.py -v
```

## Example

```
$ python password_gen.py
Do you want alphabets (A-Z) in your password?
Answer (Y/N): y
Do you want numbers (0-9) in your password?
Answer (Y/N): y
Do you want symbols in your password?
Answer (Y/N): y
Enter the password length (Minimum 1, Maximum 128): 16
How many passwords do you want to generate? (1–10): 3

Password 1: aR8!vZ#2qL@5mW0s
Password 2: 7Kp$eN1!uX3bYh6@
Password 3: dT4#wQ9!rJ2nMv8&
Password Strength:  Strong
```
