password = input("Enter your password: ")

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(not c.isalnum() for c in password)

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong Password 💪")
else:
    print("Weak Password ❌")
if len(password) < 8:
    print("Password must be at least 8 characters")