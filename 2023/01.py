"""Puzzle set 01 solutions."""

import helpers


def first_last_digits(line):
    """
    Return only the first and last digits of a string.

    Input: line, a string.
    Output: a string of 2 digits.
    """
    digits = "".join(i for i in line if i.isdigit())
    return int(digits[0] + digits[-1])


def digit2word(line):
    """
    Return only the first and last digits of a string, considering words.

    Input: line, a string.
    Output: a string of 2 digits.
    """
    numbers = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "4",
        "five": "5e",
        "six": "6",
        "seven": "7n",
        "eight": "e8t",
        "nine": "n9e"
    }

    for k, v in numbers.items():
        if k in line:
            line = line.replace(k, v)
    return line


def calibration_value(calibration_data):
    """
    Sum data from calibration file for both puzzles.

    Input: calibration_data, a tuple of strings.
    Output: a tuple of ints.
    """
    return (
        sum(first_last_digits(line) for line in calibration_data),
        sum(first_last_digits(digit2word(line)) for line in calibration_data)
    )


print(calibration_value(helpers.linereader("01.txt")))
