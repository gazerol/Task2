from itertools import permutations


def get_distance_points(first_point, second_point):
    x1, y1 = first_point
    x2, y2 = second_point
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def get_list_lengths(combo, i=0):
    distance_points = 0
    list_calc_lengths = []
    while len(list_calc_lengths) != len(list_points):
        distance_points += get_distance_points(combo[0 + i], combo[1 + i])
        list_calc_lengths.append(distance_points)
        i += 1
    return list_calc_lengths


def calc_path(length, list_combination, list_len):
    result = f'{list_combination[0]}'
    iter_list_len = iter(list_len)
    for selected_point in list_combination[1:]:
        result += f' -> {selected_point}[{next(iter_list_len)}]'
    result += f' = {length}'
    return result


def get_best_path(points):
    best_list_combination = []
    best_list_length = []
    point_1 = points[0]
    min_length = -1
    for combination in permutations(points[1:]):
        combination_formatted = list(combination)
        combination_formatted.insert(0, point_1)
        combination_formatted.append(point_1)
        list_lengths = get_list_lengths(combination_formatted)
        if list_lengths[-1] < min_length or min_length == -1:
            min_length = list_lengths[-1]
            best_list_combination = combination_formatted
            best_list_length = list_lengths

    print(calc_path(min_length, best_list_combination, best_list_length))


if __name__ == "__main__":
    list_points = [
        (0, 2),
        (2, 5),
        (5, 2),
        (6, 6),
        (8, 3),
    ]
    get_best_path(list_points)
