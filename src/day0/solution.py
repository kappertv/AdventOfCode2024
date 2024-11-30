
def count(group):
    return map(int, group.split("\n"))


def part1(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip()
    groups = data.split("\n\n")
    group_sums = [sum(count(group)) for group in groups]
    return max(group_sums)

def part2(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip()
    groups = data.split("\n\n")
    group_sums = [sum(count(group)) for group in groups]
    return sum(sorted(group_sums)[-3:])
