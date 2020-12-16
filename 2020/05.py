"""Puzzle 05 solutions."""

import math

import helpers


def get_seat_id(seat):
    """Get unique seat ID."""

    def bisection(letters, upper, lower=0):
        """Do a bisection search."""
        for letter in letters:
            if letter == "F" or letter == "L":
                middle = math.floor((lower + upper) / 2)
                upper = middle
            else:
                middle = math.ceil((lower + upper) / 2)
                lower = middle
        return middle

    return bisection(seat[:7], 127) * 8 + bisection(seat[7:], 7)


def get_seat_id_list(data):
    """Get list of all occupied seats by ID."""
    return tuple([get_seat_id(seat) for seat in data])


def find_seat(data):
    """Find seat ID."""
    seats = get_seat_id_list(data)
    for seat in range(max(seats)):
        if seat - 1 in seats and seat + 1 in seats and seat not in seats:
            return seat


data = helpers.linereader("05.txt")
print(max(get_seat_id_list(data)))
print(find_seat(data))
