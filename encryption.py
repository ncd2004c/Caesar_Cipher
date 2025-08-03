#!/usr/bin/env python3

message = input("Type message you want me to encrypt: ")
step = int(input("How many positions away do you want to be from the base letter: "))
def shifting_message(phrase, steps):
    end_message = ""
    for char in phrase:
        if char.isupper():
            ascii_value = ord(char) + steps
            while ascii_value > 90:
                temp = ascii_value - 90
                ascii_value = temp + 64
            new_char = chr(ascii_value)
            end_message = end_message + new_char
        elif char.islower():
            ascii_value = ord(char) + steps
            while ascii_value > 122:
                temp = ascii_value - 122
                ascii_value = temp + 96
            new_char = chr(ascii_value)
            end_message = end_message + new_char
        else:
            end_message = end_message + char

    return end_message

encrypted_message = shifting_message(message, step)
print("Your encrypted message : " + encrypted_message)
