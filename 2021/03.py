"""Puzzle set 03 solutions."""

import helpers


def bit_counter(report):
    """
    Count occurences of 1’s in report.

    Inputs: report, a list of strings.
    Returns: a list of ints.
    """
    counter = []
    for x in range(len(report[0])):
        counter.append(sum(int(bit) for line in report for bit in line[x]))
    return counter


def bit_criterion_oxygen(data, position, count):
    """
    Check list against bit criterion.

    Inputs:
        data, a list of strs.
        position, an int.
        count, an int.
    """
    if count >= len(data) / 2:
        return [line for line in data if line[position] == "1"]
    else:
        return [line for line in data if line[position] == "0"]


def bit_criterion_co2(data, position, count):
    """
    Check list against bit criterion.

    Inputs:
        data, a list of strs.
        position, an int.
        count, an int.
    """
    if count < len(data) / 2:
        return [line for line in data if line[position] == "1"]
    else:
        return [line for line in data if line[position] == "0"]


def power_comsumption(report):
    """
    Generate power consumption from binary report.

    Inputs: report, a list of strings.
    """
    gamma, epsilon = "", ""
    for bit_count in bit_counter(report):
        if bit_count > len(report) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


def life_support(report):
    """
    Generate life support from binary report.

    Inputs: report, a list of strings.
    """
    oxygen, co2 = report[:], report[:]
    counter = 0
    while len(oxygen) > 1:
        oxygen = bit_criterion_oxygen(
            oxygen, counter, bit_counter(oxygen)[counter]
        )
        counter += 1
    counter = 0
    while len(co2) > 1:
        co2 = bit_criterion_co2(co2, counter, bit_counter(co2)[counter])
        counter += 1
    return int(oxygen[0], 2) * int(co2[0], 2)


print(power_comsumption(helpers.linereader("03.txt")))
print(life_support(helpers.linereader("03.txt")))
