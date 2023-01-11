def encrypt(string, shift_input):
    shift = shift_input % 26
    result = ""
    for char in string:
        if char.isupper():
            new_num = ord(char) + shift
            result += chr(new_num - 26) if new_num > 90 else chr(new_num)
        elif char.islower():
            new_num = ord(char) + shift
            result += chr(new_num - 26) if new_num > 122 else chr(new_num)
        else:
            result += char
    return result


def decrypt(string, shift_input):
    shift = shift_input % 26


def crack(string):
    pass


