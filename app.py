from flask import Flask, render_template, request

from password_gen import build_character_set, generate_password, get_password_strength

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    errors = []

    use_letters = "letters" in request.form
    use_numbers = "numbers" in request.form
    use_symbols = "symbols" in request.form

    if not (use_letters or use_numbers or use_symbols):
        errors.append("Please select at least one character type.")

    try:
        length = int(request.form.get("length", ""))
        if length < 1:
            errors.append("Password length must be at least 1.")
        elif length > 128:
            errors.append("Password length must be at most 128.")
    except (ValueError, TypeError):
        errors.append("Please enter a valid password length.")
        length = None

    try:
        count = int(request.form.get("count", ""))
        if count < 1 or count > 10:
            errors.append("Number of passwords must be between 1 and 10.")
    except (ValueError, TypeError):
        errors.append("Please enter a valid number of passwords.")
        count = None

    if errors:
        return render_template(
            "index.html",
            errors=errors,
            form=request.form,
        )

    characters = build_character_set(use_letters, use_numbers, use_symbols)
    passwords = [generate_password(characters, length) for _ in range(count)]
    strength = get_password_strength(length, use_letters, use_numbers, use_symbols)

    return render_template(
        "index.html",
        passwords=passwords,
        strength=strength,
        form=request.form,
    )


if __name__ == "__main__":
    app.run()
