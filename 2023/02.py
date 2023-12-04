"""Puzzle set 01 solutions."""

import helpers


def parser(game_data):
    """
    Return the game data parsed into a list.

    Input: a string.
    Output: a tuple.
    """
    game_id, cubes = game_data.split(":")
    game_id = int(game_id.strip("Game "))
    handfuls = cubes.split(";")
    cubes = []
    for handful in handfuls:
        handful = handful.split(",")
        result = {}
        for single_colour in handful:
            single_colour = single_colour.split()
            result.update({single_colour[1]: int(single_colour[0])})
        cubes.append(result)
    return game_id, cubes


def validate_game(parsed_game):
    """
    Check whether a game is valid and returns a boolean.

    Input: a tuple from parser().
    Output: a boolean.
    """
    for handful in parsed_game[1]:
        if (
            handful.get("red", 0) > 12
            or handful.get("green", 0) > 13
            or handful.get("blue", 0) > 14
        ):
            return False
    return True


def sum_valid_games(games):
    """
    Sum id of all valid games.

    Inputs: strings from input file.
    Outputs: an int.
    """
    total = 0
    for game in games:
        game = parser(game)
        if validate_game(game):
            total += game[0]
    return total


def fewest_cubes(parsed_game):
    """
    Return the fewest number of cubes of each colour for a game.

    Inputs: a tuple from parser().
    Outputs: a list of ints
    """
    fewest = {"blue": 0, "green": 0, "red": 0}
    for handful in parsed_game[1]:
        for k, v in handful.items():
            if v > fewest.get(k):
                fewest.update({k: v})
    return fewest


def power_cubes(games):
    """
    Multiply fewest amount of cubes for a game together.

    Inputs: strings from input file.
    Outputs: an int.
    """
    total = 0
    for game in games:
        game = fewest_cubes(parser(game))
        power = 1
        for v in game.values():
            power *= v
        total += power
    return total


print(sum_valid_games(helpers.linereader("02.txt")))
print(power_cubes(helpers.linereader("02.txt")))
