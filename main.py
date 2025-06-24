# password_strength_checker/main.py

import re
import math
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def check_length(password: str) -> bool:
    """Check if password length is at least 8 characters."""
    return len(password) >= 8

def check_uppercase(password: str) -> bool:
    """Check if password contains at least one uppercase letter."""
    return any(c.isupper() for c in password)

def check_lowercase(password: str) -> bool:
    """Check if password contains at least one lowercase letter."""
    return any(c.islower() for c in password)

def check_digit(password: str) -> bool:
    """Check if password contains at least one digit."""
    return any(c.isdigit() for c in password)

def check_symbol(password: str) -> bool:
    """Check if password contains at least one special symbol."""
    symbols = '!@#$%^&*()-_=+[]{}|;:,.<>?/'
    return any(c in symbols for c in password)

def get_strength_score(password: str) -> int:
    """Calculate the password strength score (0-5)."""
    score = 0
    score += check_length(password)
    score += check_lowercase(password)
    score += check_uppercase(password)
    score += check_digit(password)
    score += check_symbol(password)
    return score

def calculate_entropy(password: str) -> float:
    """Estimate password entropy in bits."""
    charsets = 0
    if check_lowercase(password): charsets += 26
    if check_uppercase(password): charsets += 26
    if check_digit(password): charsets += 10
    if check_symbol(password): charsets += 32

    if charsets == 0:
        return 0.0

    return len(password) * math.log2(charsets)

def categorize(score: int) -> tuple[str, str]:
    """Categorize password strength based on score."""
    if score <= 2:
        return ("Weak", Fore.RED)
    elif score in [3, 4]:
        return ("Moderate", Fore.YELLOW)
    else:
        return ("Strong", Fore.GREEN)

def display_result(score: int, strength: str, color: str, entropy: float) -> None:
    """Display the password strength result with colored output."""
    print("\n" + "-" * 40)
    print(f"Password Score   : {score}/5")
    print(f"Password Entropy : {entropy:.2f} bits")
    print(f"Password Strength: {color}{strength}{Style.RESET_ALL}")
    print("-" * 40 + "\n")

def main():
    print("\n==============================")
    print("  🔐 Password Strength Checker")
    print("==============================\n")

    password = input("Enter a password to check: ")

    score = get_strength_score(password)
    entropy = calculate_entropy(password)
    strength, color = categorize(score)

    display_result(score, strength, color, entropy)

if __name__ == "__main__":
    main()
