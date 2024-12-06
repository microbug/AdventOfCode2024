
def main():
    f = open("input.txt", "r")
    list_1 = []
    list_2 = []
    for line in f.readlines():
        sections = line.split()
        list_1.append(int(sections[0]))
        list_2.append(int(sections[-1]))  # allows a variable number of spaces
    list_1.sort()
    list_2.sort()
    assert(len(list_1) == len(list_2))
    distance = 0
    for (item_one, item_two) in zip(list_1, list_2):
        distance += abs(item_one - item_two)
    print(f"Part 1: {distance}")

    similarity = 0
    for item in list_1:
        similarity += item * list_2.count(item)
    print(f"Part 2: {similarity}")
        



if __name__ == "__main__":
    main()