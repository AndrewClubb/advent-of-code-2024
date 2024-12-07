from aocd import get_data


def fetch_data_into_arrays():
    return [[int(num) for num in row.split()] for row in get_data(day=2, year=2024).strip().split('\n')]


def are_levels_safe(first, second, is_inc):
    if is_inc:
        return 0 < second - first <= 3
    else:
        return 0 < first - second <= 3


def is_report_safe_recursive(i, is_inc, failure_allowed, report):
    if i >= len(report) - 1:
        return True

    if are_levels_safe(report[i], report[i + 1], is_inc):
        return is_report_safe_recursive(i + 1, is_inc, failure_allowed, report)

    if failure_allowed:
        if i == len(report) - 2:
            return True

        if i == 0 and (are_levels_safe(report[0], report[2], is_inc) or are_levels_safe(report[1], report[2], is_inc)):
            return is_report_safe_recursive(i + 2, is_inc, False, report)

        if are_levels_safe(report[i], report[i + 2], is_inc):
            return is_report_safe_recursive(i + 2, is_inc, False, report)

    return False


def is_report_safe(report, failure_allowed):
    return (is_report_safe_recursive(0, True, failure_allowed, report) or
            is_report_safe_recursive(0, False, failure_allowed, report))


def main():
    reports = fetch_data_into_arrays()

    print("part 1: ", sum(is_report_safe(report, False) for report in reports))
    print("part 2: ", sum(is_report_safe(report, True) for report in reports))


main()