"""Puzzle set 02 solutions."""

import helpers


def position(instructions):
    """Find out current position."""
    hpos, depth, aim = 0, 0, 0
    for line in instructions:
        command, value = line.split()
        value = int(value)
        if command == "forward":
            hpos += value
            depth += aim * value
        elif command == "down":
            aim += value
        elif command == "up":
            aim -= value
    return hpos * aim, hpos * depth


print(position(helpers.linereader("02.txt")))
