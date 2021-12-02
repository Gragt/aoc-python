"""Puzzle set 01 solutions."""

import helpers


def detect_depth(depths):
    """
    Count number of increases between measurements.

    Inputs: depths, a list of ints.
    Returns: an int.
    """
    old_depth = depths[0]
    counter = 0
    for depth in depths:
        if depth > old_depth:
            counter += 1
        old_depth = depth
    return counter


def sliding_window(depths):
    """
    Count increases between three-measurement sliding window.

    Inputs: depths, a list of ints.
    Returns: an int.
    """
    old_window = depths[0] + depths[1] + depths[2]
    counter = 0
    for x in range(len(depths) - 2):
        window = depths[x] + depths[x + 1] + depths[x + 2]
        if window > old_window:
            counter += 1
        old_window = window
    return counter


print(
    detect_depth(helpers.linereader_int("01.txt")),
    sliding_window(helpers.linereader_int("01.txt"))
)
