import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    character_pool = ""

    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        print("No character types selected. Please select at least one type.")
        return None

    # Generate the password by randomly selecting characters from the pool
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Password Generator")

    # Get user input for password length
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive integer for the password length.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer for the password length.")
        return

    # Get user preferences for password complexity
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    # Generate the password
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
    
    if password:
        print(f"Generated Password: {password}")

# Run the main function
if __name__ == "__main__":
    main()
