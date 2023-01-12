import nltk    # pip install nltk
import ssl
import re

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

from nltk.corpus import words, names
nltk.download("words", quiet=True)
nltk.download("names", quiet=True)


word_db = words.words()
names_db = names.words()


def encrypt(string, shift):
    result = ""
    for char in string:
        lower = 32 if char.islower() else 0
        new_shift = ord(char.upper()) + (shift % 26) + lower
        if char.isalpha():
            result += chr(new_shift - 26) if new_shift > 90 + lower else chr(new_shift)
        else:
            result += char
    return result


def decrypt(string, shift):
    return encrypt(string, shift*(-1))


def crack(string):
    for i in range(1, 26):
        attempt = encrypt(string, i)
        word_list = attempt.split()
        count = 0
        for word in word_list:
            word = re.sub(r"[^A-Za-z]+", "", word)
            if word.lower() in word_db or word in names_db:
                count += 1
        if count / len(word_list) > 0.9:
            return attempt
    return ""


if __name__ == "__main__":

    choice = input("> Would you like to encrypt (e), decrypt (d), or crack (c) a message? Use any other key to exit. ")
    if choice.lower() == "e":
        msg = ""
        while msg == "":
            msg = input("> Type the message you'd like to encrypt: ")
        shift = 0
        while not (shift > 0):
            shift = int(input("> Input a whole number that you'd like to shift the message: "))
        print(encrypt(msg, shift))
    if choice.lower() == "d":
        msg = ""
        while msg == "":
            msg = input("> Type the message you'd like to decrypt: ")
        shift = 0
        while not (shift > 0):
            shift = int(input("> Input a whole number that you'd like to un-shift the message: "))
        print(decrypt(msg, shift))
    if choice.lower() == "c":
        msg = ""
        while msg == "":
            msg = input("> Type the message you'd like to crack: ")
        cracked = crack(msg)
        print("Result: ", cracked)
