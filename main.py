# password_strength_checker/main.py
import re
from colorama import Fore, Style, init

init(autoreset=True)

def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return any(c.isupper() for c in password)

def check_lowercase(password):
    return any(c.islower() for c in password)

def check_digit(password):
    return any(c.isdigit() for c in password)

def check_symbol(password):
    return any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for c in password)

def get_strength_score(password):
    score = 0
    if check_length(password): score += 1
    if check_lowercase(password): score += 1
    if check_uppercase(password): score += 1
    if check_digit(password): score += 1
    if check_symbol(password): score += 1
    return score

def categorize(score):
    if score <= 2:
        return ("Weak", Fore.RED)
    elif score == 3 or score == 4:
        return ("Moderate", Fore.YELLOW)
    else:
        return ("Strong", Fore.GREEN)

def main():
    print("\nPassword Strength Checker")
    password = input("Enter a password to check: ")

    score = get_strength_score(password)
    strength, color = categorize(score)

    print(f"\nPassword Score: {score}/5")
    print(f"Password Strength: {color}{strength}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
