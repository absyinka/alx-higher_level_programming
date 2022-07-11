#!/usr/bin/python3


def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return 0
    roman_string = str(roman_string).upper()
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    number = 0
    lastItem = "I"
    for letter in roman_string[::-1]:
        if my_dict[letter] < my_dict[last]:
            number -= my_dict[letter]
        else:
            number += my_dict[letter]
        lastItem = letter
    return number
