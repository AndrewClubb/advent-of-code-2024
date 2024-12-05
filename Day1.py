from aocd import get_data


def fetch_data_into_arrays():
    integer_array = list(map(int, get_data(day=1, year=2024).split()))

    return sorted(integer_array[::2]), sorted(integer_array[1::2])


def distance_between_arrays(left_array, right_array):
    return sum(abs(a - b) for a, b in zip(left_array, right_array))


def similarity_between_arrays(left_array, right_array):
    return sum(value * right_array.count(value) for value in left_array)


def main():
    left_array, right_array = fetch_data_into_arrays()
    distance = distance_between_arrays(left_array, right_array)
    similarity = similarity_between_arrays(left_array, right_array)

    print("distance: ", distance)
    print("similarity: ", similarity)


main()
