import string


def alphabet_position(letter):
    """Receives a character, letter, and returns the 0-based
    numerical position of that letter in the alphabet."""
    lowerletter = letter.lower()
    index = string.ascii_lowercase.find(lowerletter)
    return index


def rotate_character(char, rot):
    """Receives a character, char, and an integer, rot, and returns string
    newchar the character rotated rot alphabetic places to the right."""
    if not char.isalpha():
        return char
    newindex = (alphabet_position(char) + rot) % 26
    if char.isupper():
        newchar = string.ascii_uppercase[newindex]
    else:
        newchar = string.ascii_lowercase[newindex]
    return newchar


def encrypt(text, rot):
    """Receives a string, text, and an integer, rot, and returns an encrypted
    string, encrypt_str, that is comprised of the characters of text rotated
    rot places to the right alphabetically."""
    encrypt_str = ""
    for char in text:
        encrypt_str = encrypt_str + rotate_character(char, rot)
    return encrypt_str