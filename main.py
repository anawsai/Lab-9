def encode(password):
    encoded_password = ''.join(str((int(char) + 3) % 10) for char in password)
    return encoded_password