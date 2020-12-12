def file_to_tuple(file):
    file = open(file, "r")
    lines = [line.rstrip("\n") for line in file.readlines()]
    return tuple(lines)
