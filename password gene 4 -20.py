import string
import random
if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    # Handle Gibberish and set the password length within the range of 4 to 20
    while True:
        try:
            plen = int(input("Enter password length (4 to 20):\n"))
            if plen < 4 or plen > 20:
                print("Password length must be between 4 and 20 characters.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    s = list(s1 + s2 + s3 + s4)
    random.shuffle(s)
    print("Your password is: ")
    print("".join(s[:plen]))