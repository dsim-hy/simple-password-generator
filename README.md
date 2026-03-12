# Simple Password Generator

A password generator with both a web interface (Flask) and a command-line interface. Generate secure, random passwords based on your criteria.

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

- [Python 3.6+](https://python.org/)
- [Flask](https://flask.palletsprojects.com/) (for the web interface)

## Web Interface (Flask)

Install dependencies and start the server:

```bash
pip install -r requirements.txt
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

![Password Generator UI](https://github.com/user-attachments/assets/16b936ff-8982-4b6e-9a38-e11221dfff51)
![Password Generator Results](https://github.com/user-attachments/assets/2a6fe69c-eae3-46c1-8a6f-dc80af4de752)

## Command-Line Interface

```bash
python password_gen.py
```

Follow the on-screen prompts to choose your password criteria. Example:

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

## Running the Tests

Install [pytest](https://pytest.org/) and run:

```bash
pip install pytest
pytest -v
```
