import secrets


def encrypt(text, shift=None):
    """
    Encrypts the given text using the Caesar cipher algorithm.

    Parameters:
    - text (str): The text to be encrypted.
    - shift (int, optional): The number of positions to shift each character. If not provided, a random shift value between 0 and 25 will be used.

    Returns:
    - str: The encrypted text.
    """
    if shift is None:
        shift = secrets.randbelow(26)

    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord("a") if char.islower() else ord("A")
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text, shift


def decrypt(text, shift):
    """
    Decrypts the given text using the Caesar cipher algorithm.

    Args:
        text (str): The text to be decrypted.
        shift (int): The number of positions to shift each character.

    Returns:
        str: The decrypted text.
    """
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord("a") if char.islower() else ord("A")
            new_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text
