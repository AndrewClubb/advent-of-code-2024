from aocd import get_data
import re


def fetch_data():
    raw_data = get_data(day=4, year=2024)

    data_table = [list(row) for row in raw_data.strip().split('\n')]
    locations_of_x = [(match.start() // len(data_table), match.start() % len(data_table))
                      for match in re.finditer(r'X', raw_data.replace("\n", ""))]
    locations_of_a = [(match.start() // len(data_table), match.start() % len(data_table))
                      for match in re.finditer(r'A', raw_data.replace("\n", ""))]

    return data_table, locations_of_x, locations_of_a


def compare_letters_pt1(first, second, third):
    return first == "M" and second == "A" and third == "S"


def count_xmas_occurrences_pt1(data_table, locations_of_x):
    xmas_count = 0
    min_x = 3
    max_x = len(data_table) - 4
    min_y = 3
    max_y = len(data_table[0]) - 4

    for row, col in locations_of_x:
        # up
        if row >= min_x and compare_letters_pt1(
                data_table[row - 1][col], data_table[row - 2][col], data_table[row - 3][col]):
            xmas_count += 1
        # up-right
        if row >= min_x and col <= max_y and compare_letters_pt1(
                data_table[row - 1][col + 1], data_table[row - 2][col + 2], data_table[row - 3][col + 3]):
            xmas_count += 1
        # right
        if col <= max_y and compare_letters_pt1(
                data_table[row][col + 1], data_table[row][col + 2], data_table[row][col + 3]):
            xmas_count += 1
        # down-right
        if row <= max_x and col <= max_y and compare_letters_pt1(
                data_table[row + 1][col + 1], data_table[row + 2][col + 2], data_table[row + 3][col + 3]):
            xmas_count += 1
        # down
        if row <= max_x and compare_letters_pt1(
                data_table[row + 1][col], data_table[row + 2][col], data_table[row + 3][col]):
            xmas_count += 1
        # down-left
        if row <= max_x and col >= min_y and compare_letters_pt1(
                data_table[row + 1][col - 1], data_table[row + 2][col - 2], data_table[row + 3][col - 3]):
            xmas_count += 1
        # left
        if col >= min_y and compare_letters_pt1(
                data_table[row][col - 1], data_table[row][col - 2], data_table[row][col - 3]):
            xmas_count += 1
        # up-left
        if row >= min_x and col >= min_y and compare_letters_pt1(
                data_table[row - 1][col - 1], data_table[row - 2][col - 2], data_table[row - 3][col - 3]):
            xmas_count += 1

    return xmas_count


def compare_letters_pt2(first, second, third, forth):
    return all(letter in {"M","S"} for letter in [first, second, third, forth]) and first != third and second != forth


def count_xmas_occurrences_pt2(data_table, locations_of_a):
    xmas_count = 0
    min_x = 1
    max_x = len(data_table) - 2
    min_y = 1
    max_y = len(data_table[0]) - 2

    for row, col in locations_of_a:
        # up
        if (min_x <= row <= max_x and min_y <= col <= max_y and
                compare_letters_pt2(
                data_table[row - 1][col - 1],
                data_table[row + 1][col - 1],
                data_table[row + 1][col + 1],
                data_table[row - 1][col + 1])):
            xmas_count += 1

    return xmas_count


def main():
    data_table, locations_of_x, locations_of_a = fetch_data()
    print("pt 1 count:", count_xmas_occurrences_pt1(data_table, locations_of_x))
    print("pt 2 count:", count_xmas_occurrences_pt2(data_table, locations_of_a))


main()