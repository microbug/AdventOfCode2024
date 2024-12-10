from copy import copy


def main():
    f = open("input.txt", "r")
    rules = []
    updates = []
    adding_rules = True
    for line in f.readlines():
        if line.strip() == "":
            adding_rules = False
            continue
        if adding_rules:
            rules_str = line.strip().split("|")
            rules.append((int(rules_str[0]), int(rules_str[1])))
        else:
            update = [int(u) for u in line.strip().split(",")]
            updates.append(update)
    
    part_1(rules, updates)
    part_2(rules, updates)


def part_1(rules: list[(int, int)], updates: list[list[int]]):
    sum = 0
    for update in updates:
        if right_order(rules, update):
            sum += update[len(update) // 2]
    print(f"Part 1: {sum}")


def part_2(rules: list[(int, int)], updates: list[list[int]]):
    sum = 0
    for update in updates:
        if not right_order(rules, update):
            fixed = fix_order(rules, update)
            sum += fixed[len(fixed) // 2]
    print(f"Part 2: {sum}")
            

def right_order(rules: list[(int, int)], update: list[int]):
    """ Returns True if all rules are followed in update, False otherwise. """
    for rule in rules:
        try:
            index_lt = update.index(rule[0])
            index_gt = update.index(rule[1])
            if index_gt < index_lt:
                return False
        except ValueError:  # Rule number(s) not found in this update
            continue
    return True


def fix_order(rules: list[(int, int)], update: list[int]) -> list[int]:
    """ Modifies the order of update to follow rules. """
    fixed = copy(update)
    while not right_order(rules, fixed):
        for rule in rules:
            try:
                index_lt = fixed.index(rule[0])
                index_gt = fixed.index(rule[1])
                if index_gt < index_lt:
                    fixed[index_lt] = rule[1]
                    fixed[index_gt] = rule[0]
            except ValueError:
                continue
    return fixed
    

if __name__ == "__main__":
    main()