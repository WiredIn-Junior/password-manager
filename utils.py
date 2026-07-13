# Import Required Modules
import os
import time
import secrets
import string
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
def password_strength_checker():
    pass # For Future Implementation