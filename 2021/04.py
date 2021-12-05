"""Puzzle set 04 solutions."""

import helpers


class BingoBoard(object):
    """Creates a bingo board."""

    def __init__(self, board):
        """
        Initialise bingo board.

        Inputs: board, a list of dictionaries.
        """
        self.board = board

    def mark_number(self, n):
        """
        Mark a number in a bingo board.

        Inputs: n, an int.
        """
        for row in self.board:
            if n in row:
                row[n] = True

    def check_victory(self):
        """
        Check a bingo board for victory condition.

        Returns: a bool.
        """
        for row in self.board:
            if all(value for value in row.values()):
                return True
        for x in range(len(self.board[0])):
            if all(list(row.values())[x] for row in self.board):
                return True


def parser(data):
    """
    Parse bingo data.

    Inputs: data, a tuple of strings.
    Returns: (
        a list of ints,
        a list of bingo boards.
        )
    """
    parsed, wip = [], []
    for line in data:
        if line:
            wip.append(line)
        else:
            parsed.append(wip)
            wip = []
    parsed.append(wip)
    return (
        list(map(int, parsed[0][0].split(","))),
        [BingoBoard(board) for board in board_parser(parsed[1:])]
    )


def board_parser(boards):
    """
    Parse bingo boards data.

    Inputs: boards, a list of lists of strings.
    Returns: a list of lists of dictionaries.
    """
    parsed, wip = [], []
    for board in boards:
        for row in board:
            wip.append({x: False for x in map(int, row.split())})
        parsed.append(wip)
        wip = []
    return parsed


def mark_boards(boards, n):
    """
    Mark a number in bingo boards.

    Inputs: boards, a list of bingo board objects.
            n, an int.
    """
    for board in boards:
        board.mark_number(n)


def check_victory_all(boards, draw):
    """
    Check for victory condition across all boards.

    Inputs:
            boards, a list of bingo boards.
            draw, a list of ints.

    Returns: (
    a list of dictionaries,
    a list of dictionaries
    )
    """
    winners = []
    for n in draw:
        mark_boards(boards, n)
        for board in boards:
            if board.check_victory():
                winners.append((board.board, n))
                boards.remove(board)
    return winners[0], winners[-1]


def score(board, n):
    """
    Calculate score.

    Inputs:
            board, a list of dictionaries.
            n, an int.
    Returns: an int.
    """
    return sum(k for row in board for k, v in row.items() if not v) * n


draw, boards = parser(helpers.linereader("04.txt"))
first, last = check_victory_all(boards, draw)
print(score(first[0], first[1]), score(last[0], last[1]))
