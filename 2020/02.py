import re


def file_to_tuple():
    file = open("02.txt", "r")
    lines = [line.rstrip("\n") for line in file.readlines()]
    return tuple(lines)


def parser(my_tuple):
    regex = re.compile(r"(\d{1,2})-(\d{1,2}) ([a-z]{1}): ([a-z]+)")
    info = [regex.search(item).groups() for item in my_tuple]
    return tuple(info)


def counter1(parsed_info):
    counter = 0
    for item in parsed_info:
        lower, upper, letter, password = item
        if password.count(letter) >= int(lower) and password.count(letter) <= int(upper):
            counter += 1
    return counter


def counter2(parsed_info):
    counter = 0
    for item in parsed_info:
        pos1, pos2, letter, password = item
        check = {password[int(pos1) - 1], password[int(pos2) - 1]}
        if letter in check and len(check) == 2:
            counter += 1
    return counter


print(counter2(parser(file_to_tuple())))
