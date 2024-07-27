def encode(password):
    return ''.join([chr(ord(char) + 3) for char in password])

def decode_password(password):
    decoded_password = ''.join(str((int(char) - 3) % 10) for char in password)
    return decoded_password

def main():
    encoded_password = None
    while True:
        print("Menu")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")
        if option == '1':
            password = input("Please enter the password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored.")
        elif option == '2':
            if encoded_password:
                original_password = decode_password(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
            else:
                print("No password has been encoded yet.")
        elif option == '3':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()