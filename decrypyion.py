#!/usr/bin/env python3

message = input("Type message you want me to decrypt: ")
step = int(input("How many positions away is it from the orginal base letter: "))
def shifting_message(phrase, steps):
    end_message = ""
    for char in phrase:
        if char.isupper():
            temp = steps % 26
            diff = ord(char) - temp
            while diff < 65:
                dist = ord(char) - 65
                diff = 91-(temp - dist)
            new_char = chr(diff)
            end_message = end_message + new_char
        elif char.islower():
            temp = steps % 26
            diff = ord(char) - temp
            while diff < 97:
                dist = ord(char) - 97
                diff = 123-(temp - dist)
            new_char = chr(diff)
            end_message = end_message + new_char
        else:
            end_message = end_message + char

    return end_message

encrypted_message = shifting_message(message, step)
print("Your Orginal message : " + encrypted_message)
