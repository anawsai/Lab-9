def decode_password(password):
    decoded_password = ''.join(str((int(char) - 3) % 10) for char in password)
    return decoded_password