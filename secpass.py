import random
import string

def generate_password(length=12, use_numbers=True, use_symbols=True, style="strong"):
"""
Generate a random password.
style: "strong" -> mix all chars
"easy" -> pronounceable (letters only)
"""
if style == "easy":
chars = string.ascii_lowercase
else:
chars = string.ascii_letters
if use_numbers:
chars += string.digits
if use_symbols:
chars += string.punctuation

password = ''.join(random.choice(chars) for _ in range(length))
return password

def main():
print("🔐 Welcome to the Password Generator 🔐")
length = int(input("Enter password length (default 12): ") or 12)
use_numbers = input("Include numbers? (y/n, default y): ").lower() != "n"
use_symbols = input("Include symbols? (y/n, default y): ").lower() != "n"
style = input("Password style? (strong/easy, default strong): ").lower() or "strong"
count = int(input("How many passwords to generate? (default 1): ") or 1)

print("\nGenerated passwords:")
for _ in range(count):
print("➡", generate_password(length, use_numbers, use_symbols, style))

if __name__ == "__main__":
main()

