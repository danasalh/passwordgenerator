import string

def check_strength(password):
length = len(password)
has_lower = any(c.islower() for c in password)
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbol = any(c in string.punctuation for c in password)

score = sum([has_lower, has_upper, has_digit, has_symbol])

if length >= 12 and score == 4:
return "💪 Strong"
elif length >= 8 and score >= 3:
return "👌 Medium"
else:
return "⚠️ Weak"
