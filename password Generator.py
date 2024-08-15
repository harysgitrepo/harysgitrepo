import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    """
    Generates a random password with specified criteria.

    Args:
        length (int): Length of the password (default is 12).
        use_uppercase (bool): Include uppercase letters (default is True).
        use_lowercase (bool): Include lowercase letters (default is True).
        use_digits (bool): Include digits (default is True).
        use_special_chars (bool): Include special characters (default is True).

    Returns:
        str: Randomly generated password.
    """
    chars = ""
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    if not chars:
        raise ValueError("At least one character set must be selected.")

    password = "".join(random.choice(chars) for _ in range(length))
    return password

# Example usage:
generated_password = generate_password(length=16, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True)
print("Generated Password:", generated_password)