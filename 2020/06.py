"""Puzzle 06 solutions."""

import helpers


def parser(data):
    """Parse data into a list of sets."""
    parsed_data, current, wip = [], [], set()
    for line in data:
        if not line:
            parsed_data.append(current)
            current = []
        else:
            for letter in line:
                wip.add(letter)
            current.append(wip)
            wip = set()
    parsed_data.append(current)
    return parsed_data


def answer_counter(parsed_data):
    """Count answered questions from parsed data."""
    merged_answers, intersected_answers = [], []
    for group in parsed_data:
        merged_answers.append(set())
        intersected_answers.append(group[0].copy())
        for member in group:
            merged_answers[-1].update(member)
            intersected_answers[-1].intersection_update(member)
    return (
        sum(len(group) for group in merged_answers),
        sum(len(group) for group in intersected_answers)
    )


data = parser(helpers.linereader("06.txt"))
print(answer_counter(data))
