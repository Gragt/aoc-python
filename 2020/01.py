def file_to_tuple():
    file = open("01.txt", "r")
    lines = map(int, [line.rstrip("\n") for line in file.readlines()])
    return tuple(lines)


def get_answers(my_tuple):
    for item1 in my_tuple:
        for item2 in my_tuple[my_tuple.index(item1) + 1:]:
            if item1 + item2 == 2020:
                answer1 = item1 * item2
            for item3 in my_tuple[my_tuple.index(item2) + 1:]:
                if item1 + item2 + item3 == 2020:
                    answer2 = item1 * item2 * item3
    return (answer1, answer2)


print(get_answers(file_to_tuple()))
