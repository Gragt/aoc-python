"""Helper functions."""


def linereader(file):
    """Read content of input file and return a tuple with content."""
    file = open(file, "r")
    return tuple([line.rstrip("\n") for line in file.readlines()])
