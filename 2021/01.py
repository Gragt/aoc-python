"""Puzzle set 01 solutions."""

import helpers


def detect_depth(depths):
    """
    Count number of increases between measurements.

    Inputs: depths, a list of ints.
    Returns: an int.
    """
    return sum(x < y for x, y in zip(depths, depths[1:]))


def sliding_window(depths):
    """
    Count increases between three-measurement sliding window.

    Inputs: depths, a list of ints.
    Returns: an int.
    """
    return detect_depth(
        [sum(window) for window in zip(depths, depths[1:], depths[2:])]
    )


print(
    detect_depth(helpers.linereader_int("01.txt")),
    sliding_window(helpers.linereader_int("01.txt"))
)
