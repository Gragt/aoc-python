def linereader(file):
    file = open(file, "r")
    return tuple([line.rstrip("\n") for line in file.readlines()])
