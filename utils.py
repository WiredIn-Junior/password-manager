# Import Required Modules
import os
import time
import secrets
import string
import re
# utils module for reusable functions
# Clear Screen Function
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear') # Cross Platform Command
# Pause Function
def pause():
    time.sleep(3) # wait Three Seconds Before Executing
def password_generator(length=8):
    # Import Alphabets
    alphabets = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabets) for _ in range(length))
    return password
# Password Strength Function
def password_strength_checker(password):
    score = 0
    strength = ""
    feedback = []
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password Should Be 8 Characters Or More")
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password Should Include Uppercase Letters")
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password Should Include Lowercase Letters")
    if re.search(r"\d", password):
        score += 1
    else:
        print("Password Should Include Digits")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        print("Password Should Include Special Characters")
    
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    return strength, feedback