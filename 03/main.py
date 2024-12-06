import re

def main():
    input = open("input.txt", "r").read()
    part_1(input)
    part_2(input)


def part_1(input):
    sum = process(input)
    print(f"Part 1: {sum}")


def process(input):
    results = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)
    sum = 0
    for result in results:
        sum += int(result[0]) * int(result[1])
    return sum


def part_2(input):
    dos = list(re.finditer(r"do\(\)", input))
    donts = list(re.finditer(r"don't\(\)", input))
    # commands is a dict of form {<index>: "command", ...}
    commands = {m.span()[1]: "do" for m in dos}
    commands.update({m.span()[0]: "don't" for m in donts})
    for i, _ in enumerate(input):
        command = "do"
        # Find most recent command
        for j in range(i, -1, -1):
            if j in commands:
                command = commands[j]
                break
        if command == "don't":
            # Erase character at position i
            input = input[:i] + "x" + input[i+1:]

    sum = process(input)
    print(f"Part 2: {sum}")
    

if __name__ == "__main__":
    main()