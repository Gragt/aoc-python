"""Puzzle 02 solutions."""

import re

import helpers


def parser(data):
    """Parse input data and return a tuple."""
    regex = re.compile(r"(\d{1,2})-(\d{1,2}) ([a-z]{1}): ([a-z]+)")
    parsed_data = [
        (
            int(regex.search(item).group(1)),
            int(regex.search(item).group(2)),
            regex.search(item).group(3),
            regex.search(item).group(4)
        )
        for item in data
    ]
    return tuple(parsed_data)


def get_answer1(parsed_data):
    """Get part 1 answer."""
    counter = 0
    for item in parsed_data:
        low, up, letter, password = item
        if password.count(letter) >= low and password.count(letter) <= up:
            counter += 1
    return counter


def get_answer2(parsed_data):
    """Get part 1 answer."""
    counter = 0
    for item in parsed_data:
        pos1, pos2, letter, password = item
        check = {password[pos1 - 1], password[pos2 - 1]}
        if letter in check and len(check) == 2:
            counter += 1
    return counter


print(get_answer2(parser(helpers.linereader("02.txt"))))
