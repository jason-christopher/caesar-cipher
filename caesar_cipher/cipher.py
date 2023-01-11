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
    # result = string in stopwords.words('english')
    # print(result)
    # return result
    pass


# doc strings to add later, they make it too messy right now...
    # """
    # Used for a encrypting AND decrypting a Caesar Cipher.
    # :param string: String that will be encrypted or decrypted.
    # :param shift: Can be a positive (for encrypting) or negative (for decrypting) integer.
    # :return: Returns the input string, but every letter will be shifted. Non-letter characters will remain the same.
    # """
    #
    # """
    # Passes the input parameters to the encrypt function to decrypt.
    # :param string: String that will be decrypted.
    # :param shift: Usually a positive integer (but could be negative). The input is converted to a negative value.
    # :return: Returns the decrypted string.
    # """

# stuff that didn't work for the crack function...
# import nltk
# # from nltk.corpus import words
# from nltk.corpus import stopwords
#
# # pip install nltk
