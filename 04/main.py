def main():
    f = open("input.txt", "r")
    puzzle = list()
    for line in f.readlines():
        puzzle.append(list(line.strip()))

    max_x = len(puzzle[0])
    max_y = len(puzzle)
    part_1(puzzle, max_x, max_y)
    part_2(puzzle, max_x, max_y)


def part_1(puzzle, max_x, max_y):
    count = 0
    # Left / right
    for y in range(0, max_y):
        count += count_xmas_in_list(puzzle[y])
    # Up / down
    for x in range(0, max_x):
        count += count_xmas_in_list([row[x] for row in puzzle])

    # Diagonal m = +1
    x = 0
    xy = [(0, y) for y in range(0, max_y)]
    xy += [(x, 0) for x in range(1, max_x)] 
    for x, y in xy:
        # Build diagonal string
        chars = list()
        y_c = y
        x_c = x
        while y_c < max_y and x_c < max_x:
            chars.append(puzzle[y_c][x_c])
            y_c += 1
            x_c += 1
        count += count_xmas_in_list(chars)
 
    # Diagonal m = -1
    x = 0
    xy = [(0, y) for y in range(0, max_y)]
    xy += [(x, max_y-1) for x in range(1, max_x)]
    for x, y in xy:
        chars = list()
        y_c = y
        x_c = x
        while y_c >= 0 and x_c < max_x:
            chars.append(puzzle[y_c][x_c])
            y_c -= 1
            x_c += 1
        count += count_xmas_in_list(chars)

    print(f"Part 1: {count}")


def part_2(puzzle, max_x, max_y):
    count = 0
    for y in range(1, max_y-1):
        for x in range(1, max_x-1):
            if cross_mas(puzzle, x, y):
                count += 1
    print(f"Part 2: {count}")


def cross_mas(puzzle, x, y):
    """ Returns True if an X-MAS pattern exists centred at x, y.
    """
    if puzzle[y][x] == "A":
        diag1 = puzzle[y-1][x-1] + puzzle[y+1][x+1]
        if diag1 != "MS" and diag1 != "SM":
            return False
        diag2 = puzzle[y+1][x-1] + puzzle[y-1][x+1]
        if diag2 != "MS" and diag2 != "SM":
            return False
        return True


def count_xmas_in_list(input):
    """ Counts the occurrences of "XMAS" and "SAMX" in a list of single-character strings.
    """
    count = 0
    xmas = ["X", "M", "A", "S"]
    buffer = list()
    for c in input:
        buffer.append(c)
        if len(buffer) > 4:
            buffer.pop(0)
        if buffer == xmas:
            count += 1
        if buffer == list(reversed(xmas)):
            count += 1
    return count


if __name__ == "__main__":
    main()