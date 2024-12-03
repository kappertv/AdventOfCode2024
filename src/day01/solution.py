def getSortedLeftAndRight(file_path):
    left = []
    right = []
    with open(file_path, "r") as file:
        data = file.read().strip()
    lines = data.splitlines()
    for line in lines:
        s = line.split("   ")
        left.append(int(s[0]))
        right.append(int(s[1]))

    left.sort()
    right.sort()
    return left,right

def part1(file_path):
    left, right = getSortedLeftAndRight(file_path)

    result = sum([abs(a - b) for a,b in zip(left,right)])

    return result

def similarityScore(file_path):
    left, right = getSortedLeftAndRight(file_path)
    result = 0

    for l in left:
        result += l * right.count(l)

    return result

