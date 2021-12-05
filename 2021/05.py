"""Solve puzzle set 05."""

import helpers


class Line(object):
    """A representation of a line, with start and end points."""

    def __init__(self, coords):
        """
        Initialise Line object.

        Inputs: coords, a tuple of tuples of ints.
        """
        super(Line, self).__init__()
        self.coords = coords

    def check_hv(self):
        """
        Check if line is vertical or horizontal.

        Returns: a bool.
        """
        return (
            self.coords[0][0] == self.coords[1][0]
            or self.coords[0][1] == self.coords[1][1]
        )

    def get_points(self):
        """
        Bresenham’s line algorithm.

        Returns: a tuple of tuples of ints.
        """
        x0, y0 = self.coords[0][0], self.coords[0][1]
        x1, y1 = self.coords[1][0], self.coords[1][1]
        points_in_line = []
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        x, y = x0, y0
        sx = -1 if x0 > x1 else 1
        sy = -1 if y0 > y1 else 1
        if dx > dy:
            err = dx / 2.0
            while x != x1:
                points_in_line.append((x, y))
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y1:
                points_in_line.append((x, y))
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        points_in_line.append((x, y))
        return points_in_line


def parser(data):
    """
    Parse data into list of coordinates.

    Inputs: data, a tuple of strings.
    Returns: a tuple of tuples of tuples.
    """
    wip = [line.split(" -> ") for line in data]
    coords = []
    for line in wip:
        coords.append(
            tuple([tuple(map(int, coord.split(","))) for coord in line])
        )
    return tuple(coords)


def check_overlaps(lines):
    """
    Check lines for any overlapping values.

    Inputs: lines, a list of lines.
    Returns: a dictionary of tuples.
    """
    check_hv_overlaps, check_overlaps = {}, {}
    for line in lines:
        for coord in line.get_points():
            check_overlaps.setdefault(coord, 0)
            check_overlaps[coord] += 1
            if line.check_hv():
                check_hv_overlaps.setdefault(coord, 0)
                check_hv_overlaps[coord] += 1
    return (
        sum(ov >= 2 for ov in check_hv_overlaps.values()),
        sum(ov >= 2 for ov in check_overlaps.values())
    )


data = parser(helpers.linereader("05.txt"))
lines = [Line(line) for line in data]
print(check_overlaps(lines))
