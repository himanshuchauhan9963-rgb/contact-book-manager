import string

def check_password_strength(password):
    special_chars = "!@#$%^&*()-_+="
    
    length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in special_chars for c in password)

    score = sum([length, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

# Example usage
if __name__ == "__main__":
    password = input("🔐 Enter your password to check strength: ")
    result = check_password_strength(password)
    print(f"Password Strength: {result}")
