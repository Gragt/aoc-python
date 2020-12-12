import helpers


def get_answers(data):
    data = tuple(map(int, data))
    for item1 in data:
        for item2 in data[data.index(item1) + 1:]:
            if item1 + item2 == 2020:
                answer1 = item1 * item2
            for item3 in data[data.index(item2) + 1:]:
                if item1 + item2 + item3 == 2020:
                    answer2 = item1 * item2 * item3
    return (answer1, answer2)


print(get_answers(helpers.linereader("01.txt")))
