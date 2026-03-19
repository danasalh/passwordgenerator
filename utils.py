# utils.py
import string
import random

def easy_password(length=8):
chars = string.ascii_lowercase
return ''.join(random.choice(chars) for _ in range(length))
