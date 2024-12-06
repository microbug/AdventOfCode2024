from copy import copy


def main():
    f = open("input.txt", "r")
    reports = []
    for line in f.readlines():
        report = [int(level) for level in line.split(" ")]
        reports.append(report)
    part_1(reports)
    part_2(reports)


def part_1(reports):
    safe_count = 0
    for report in reports:
        if is_safe(report):
            safe_count += 1
    print(f"Part 1: {safe_count}")


def part_2(reports):
    safe_count = 0
    for report in reports:
        if is_safe(report):
            safe_count += 1
            continue
        for i in range(len(report)):
            report_copy = copy(report)
            report_copy.pop(i)
            if is_safe(report_copy):
                safe_count += 1
                break
    print(f"Part 2: {safe_count}")


def is_safe(report):
    if sorted(report) != report and sorted(report, reverse=True) != report:
        return False  # Report is not monotonic

    for (a, b) in zip(report[:-1], report[1:]):
        difference = abs(a - b)
        if difference > 3 or difference < 1:
            return False

    return True


if __name__ == "__main__":
    main()