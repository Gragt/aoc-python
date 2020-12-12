import re

import helpers


def parser(data):
    regex = re.compile(r"(\d{1,2})-(\d{1,2}) ([a-z]{1}): ([a-z]+)")
    parsed_data = [regex.search(item).groups() for item in data]
    return tuple(parsed_data)


def get_answer1(parsed_data):
    counter = 0
    for item in parsed_data:
        low, up, letter, password = item
        if password.count(letter) >= int(low) and password.count(letter) <= int(up):
            counter += 1
    return counter


def get_answer2(parsed_data):
    counter = 0
    for item in parsed_data:
        pos1, pos2, letter, password = item
        check = {password[int(pos1) - 1], password[int(pos2) - 1]}
        if letter in check and len(check) == 2:
            counter += 1
    return counter


print(get_answer2(parser(helpers.linereader("02.txt"))))
