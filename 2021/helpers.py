"""Helper functions."""


def linereader(file):
    """Read content of input file and return a tuple with content."""
    file = open(file, "r")
    return tuple([line.rstrip("\n") for line in file.readlines()])


def linereader_int(file):
    """Read input file and return a tuple with content converted to ints."""
    file = open(file, "r")
    return tuple(map(int, [line.rstrip("\n") for line in file.readlines()]))
