from aocd import get_data
import re
import math


def fetch_data_into_array():
    pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
    return re.findall(pattern, get_data(day=3, year=2024))


def evaluate_expression_array(mul_array):
    current_sum = 0
    is_valid = True
    for expression in mul_array:
        if expression == "do()":
            is_valid = True
        elif expression == "don't()":
            is_valid = False
        elif is_valid:
            current_sum += math.prod(map(int, expression[4:-1].split(",")))
    return current_sum


def main():
    expression_array = fetch_data_into_array()
    print(evaluate_expression_array(expression_array))


main()