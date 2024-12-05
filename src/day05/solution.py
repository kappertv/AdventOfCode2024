def readReports(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip()
    parts = data.split("\n\n")
    pageOrderingRules = parts[0].splitlines()
    updates = parts[1].splitlines()
    intUpdates = []
    for update in updates:
        intUpdates.append([int(x) for x in update.split(',')])

    return pageOrderingRules, intUpdates

def part1(file_path):
    rules, updates = readReports(file_path)
    validUpdates = list(update for update in updates if isValidUpdate(update, rules))
    result = sum(get_middle(update) for update in validUpdates)
    return result

def part2(file_path):
    rules, updates = readReports(file_path)
    inValidUpdates = list(update for update in updates if not isValidUpdate(update, rules))
    validUpdates = list(makeValidUpdate(update, rules) for update in inValidUpdates)
    result = sum(get_middle(update) for update in validUpdates)
    return result

def makeValidUpdate(update, rules):
    for rule in rules:
        x, y = rule.split('|')
        iX = int(x)
        iY = int(y)
        positions = {x: i for i, x in enumerate(update) if x in {iX, iY}}
        if iX in positions and iY in positions:
            if positions[iY] < positions[iX]: 
                # print(f"{iX} is at position {positions[iX]}, {iY} is at position {positions[iY]}")
                update[positions[iX]], update[positions[iY]] = update[positions[iY]], update[positions[iX]]
                return makeValidUpdate(update, rules)
        else:
            continue    
    return update

def isValidUpdate(update, rules):
    for rule in rules:
        x, y = rule.split('|')
        iX = int(x)
        iY = int(y)
        positions = {x: i for i, x in enumerate(update) if x in {iX, iY}}
        if iX in positions and iY in positions:
            # print(f"{iX} is at position {positions[iX]}, {iY} is at position {positions[iY]}")
            if positions[iY] < positions[iX]: 
                return False
        else:
            continue

    return True

def get_middle(numbers):
    if len(numbers) % 2 == 1:
        return numbers[len(numbers) // 2]
    else:
        raise ValueError("The list does not have an odd number of elements.")
