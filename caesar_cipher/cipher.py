import nltk    # pip install nltk
import ssl
import re
from nltk.corpus import words, names
nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


def encrypt(string, shift):
    result = ""
    for char in string:
        lower = 32 if char.islower() else 0
        new_shift = ord(char.upper()) + (shift % 26) + lower
        if char.isalpha():
            if new_shift < 65 + lower:
                result += chr(new_shift + 26)
            elif new_shift > 90 + lower:
                result += chr(new_shift - 26)
            else:
                result += chr(new_shift)
        else:
            result += char
    return result


def decrypt(string, shift):
    return encrypt(string, shift*(-1))


def crack(string):
    for i in range(25):
        attempt = encrypt(string, i)
        word_list = attempt.split()
        count = 0
        for word in word_list:
            word = re.sub(r"[^A-Za-z]+", "", word)
            if word.lower() in words.words() or word.lower() in names.words():
                count += 1
        if count / len(word_list) > 0.9:
            return attempt
    return ""
