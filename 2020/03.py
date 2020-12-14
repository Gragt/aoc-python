"""Puzzle 03 solutions."""

import helpers


def count_trees(data, x_inc, y_inc):
    """Count trees in input data."""
    max_length, max_height, x, y, trees = len(data[0]), len(data), 0, 0, 0
    limit_reached = False
    while not limit_reached:
        x += x_inc
        y += y_inc
        if x >= max_length:
            x -= max_length
        if data[y][x] == "#":
            trees += 1
        if y + y_inc >= max_height:
            limit_reached = True
    return trees


data = helpers.linereader("03.txt")
print(count_trees(data, 3, 1))
print(
    count_trees(data, 1, 1)
    * count_trees(data, 3, 1)
    * count_trees(data, 5, 1)
    * count_trees(data, 7, 1)
    * count_trees(data, 1, 2)
)
