import random


def generate_password(length, special_chars=False):
    password = ""

    if special_chars:
        for _ in range(length):
            password += chr(random.randint(33, 126))
    else:
        available_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ"
        for _ in range(length):
            password += random.choice(available_characters)
    
    if any(c.isdigit() for c in password) and any(c.isupper() for c in password):
        return password

    return generate_password(length, special_chars)
        
