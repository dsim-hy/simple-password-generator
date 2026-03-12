import string
from unittest.mock import patch

import pytest

from password_gen import (
    build_character_set,
    generate_password,
    get_character_types,
    get_num_passwords,
    get_password_length,
    get_password_strength,
    get_yes_no,
)


# ---------------------------------------------------------------------------
# get_yes_no
# ---------------------------------------------------------------------------
class TestGetYesNo:
    @pytest.mark.parametrize("response", ["y", "Y", "yes", "YES", "Yes"])
    def test_yes_variants(self, response):
        with patch("builtins.input", return_value=response):
            assert get_yes_no("prompt") is True

    @pytest.mark.parametrize("response", ["n", "N", "no", "NO", "No"])
    def test_no_variants(self, response):
        with patch("builtins.input", return_value=response):
            assert get_yes_no("prompt") is False

    def test_invalid_then_valid(self, capsys):
        with patch("builtins.input", side_effect=["maybe", "y"]):
            result = get_yes_no("prompt")
        assert result is True
        captured = capsys.readouterr()
        assert "Please enter Y or N." in captured.out


# ---------------------------------------------------------------------------
# build_character_set
# ---------------------------------------------------------------------------
class TestBuildCharacterSet:
    def test_letters_only(self):
        chars = build_character_set(True, False, False)
        assert chars == string.ascii_letters

    def test_numbers_only(self):
        chars = build_character_set(False, True, False)
        assert chars == string.digits

    def test_symbols_only(self):
        chars = build_character_set(False, False, True)
        assert chars == string.punctuation

    def test_all_types(self):
        chars = build_character_set(True, True, True)
        assert set(chars) == set(string.ascii_letters + string.digits + string.punctuation)

    def test_letters_and_numbers(self):
        chars = build_character_set(True, True, False)
        assert set(chars) == set(string.ascii_letters + string.digits)


# ---------------------------------------------------------------------------
# get_password_length
# ---------------------------------------------------------------------------
class TestGetPasswordLength:
    def test_valid_length(self):
        with patch("builtins.input", return_value="12"):
            assert get_password_length() == 12

    def test_minimum_length(self):
        with patch("builtins.input", return_value="1"):
            assert get_password_length() == 1

    def test_maximum_length(self):
        with patch("builtins.input", return_value="128"):
            assert get_password_length() == 128

    def test_zero_rejected_then_valid(self, capsys):
        with patch("builtins.input", side_effect=["0", "5"]):
            result = get_password_length()
        assert result == 5
        assert "Minimum 1" in capsys.readouterr().out

    def test_over_max_rejected_then_valid(self, capsys):
        with patch("builtins.input", side_effect=["129", "10"]):
            result = get_password_length()
        assert result == 10
        assert "Maximum of 128" in capsys.readouterr().out

    def test_non_numeric_rejected_then_valid(self, capsys):
        with patch("builtins.input", side_effect=["abc", "8"]):
            result = get_password_length()
        assert result == 8
        assert "valid number" in capsys.readouterr().out


# ---------------------------------------------------------------------------
# get_num_passwords
# ---------------------------------------------------------------------------
class TestGetNumPasswords:
    def test_valid_count(self):
        with patch("builtins.input", return_value="3"):
            assert get_num_passwords() == 3

    def test_boundary_low(self):
        with patch("builtins.input", return_value="1"):
            assert get_num_passwords() == 1

    def test_boundary_high(self):
        with patch("builtins.input", return_value="10"):
            assert get_num_passwords() == 10

    def test_out_of_range_rejected(self, capsys):
        with patch("builtins.input", side_effect=["0", "1"]):
            result = get_num_passwords()
        assert result == 1
        assert "1 and 10" in capsys.readouterr().out

    def test_non_numeric_rejected(self, capsys):
        with patch("builtins.input", side_effect=["!", "2"]):
            result = get_num_passwords()
        assert result == 2
        assert "valid number" in capsys.readouterr().out


# ---------------------------------------------------------------------------
# generate_password
# ---------------------------------------------------------------------------
class TestGeneratePassword:
    def test_correct_length(self):
        chars = string.ascii_letters
        password = generate_password(chars, 16)
        assert len(password) == 16

    def test_characters_from_pool(self):
        chars = string.digits
        password = generate_password(chars, 20)
        assert all(c in chars for c in password)

    def test_empty_would_still_respect_length(self):
        chars = "a"
        password = generate_password(chars, 5)
        assert password == "aaaaa"


# ---------------------------------------------------------------------------
# get_password_strength
# ---------------------------------------------------------------------------
class TestGetPasswordStrength:
    def test_strong(self):
        assert get_password_strength(12, True, True, True) == "Strong"

    def test_strong_long(self):
        assert get_password_strength(20, True, True, True) == "Strong"

    def test_moderate_two_types(self):
        assert get_password_strength(8, True, True, False) == "Moderate"

    def test_moderate_three_types_short(self):
        assert get_password_strength(8, True, True, True) == "Moderate"

    def test_weak_one_type_short(self):
        assert get_password_strength(4, True, False, False) == "Weak"

    def test_weak_single_character(self):
        assert get_password_strength(1, False, True, False) == "Weak"


# ---------------------------------------------------------------------------
# get_character_types integration
# ---------------------------------------------------------------------------
class TestGetCharacterTypes:
    def test_all_yes(self):
        with patch("builtins.input", side_effect=["y", "y", "y"]):
            result = get_character_types()
        assert result == (True, True, True)

    def test_all_no_then_yes(self, capsys):
        with patch("builtins.input", side_effect=["n", "n", "n", "y", "n", "n"]):
            result = get_character_types()
        assert result == (True, False, False)
        assert "at least one" in capsys.readouterr().out
