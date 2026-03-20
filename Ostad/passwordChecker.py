print("Welcome to Password Strength Checker!")

password = input("Enter your password: ")

score = 0

# Length check
if len(password) >= 8:
    score += 1

# Number check
if any(char.isdigit() for char in password):
    score += 1

# Uppercase check
if any(char.isupper() for char in password):
    score += 1

# Special character check
if any(char in "!@#$%^&*()" for char in password):
    score += 1

# Result
if score == 4:
    print("Strength: Very Strong")
elif score == 3:
    print("Strength: Strong")
elif score == 2:
    print("Strength: Medium")
elif score == 1:
    print("Strength: Weak")
else:
    print("Strength: Very Weak")

print("Thanks for using Password Strength Checker!")