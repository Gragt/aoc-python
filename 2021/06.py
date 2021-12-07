"""Solve puzzle set 06."""

import helpers


def parser(data):
    """
    Parse fish information.

    Inputs: data, a tuple of strings.
    Returns: a list of ints.
    """
    school = list(map(int, data[0].split(",")))
    counter = [0 for x in range(9)]
    for x in range(max(school) + 1):
        counter[x] += school.count(x)
    return counter


def lanternfish(school, days):
    """
    Simulate lanterfish.

    Inputs:
        school, a list of ints.
        days, an int.
    Returns: a list of ints.
    """
    for day in range(days):
        newfish = 0
        newfish += school[0]
        school.insert(8, school.pop(0))
        school[6] += newfish
    return sum(school)


school = parser(helpers.linereader("06.txt"))
print(lanternfish(school[:], 80), lanternfish(school[:], 256))
