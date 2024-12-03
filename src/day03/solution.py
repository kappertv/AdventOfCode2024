import re

def readMemory(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip()
    lines = data.splitlines()
    return lines

def getSumOfMultiplications(file_path):
    memory = readMemory(file_path)
    matches = []
    # pattern = r"mul\(\d{1,3},\d{1,3}\)"
    pattern =  r"mul\((\d{1,3}),(\d{1,3})\)"
    for line in memory:
        matches.extend(re.findall(pattern, line))
    
    print(matches)

    result = sum([int(x) * int(y) for x,y in matches])
    return result

def getSumOfMultiplicationsPart2(file_path):
    memory = readMemory(file_path)
    matches = []
    # pattern = r"mul\(\d{1,3},\d{1,3}\)"
    pattern =  r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))" # |don't\(\)|do\(\)"
    for line in memory:
        matches.extend(re.findall(pattern, line))
    
    print(matches)

    result = 0
    skip = False
    for o,x,y in matches:
        if skip:
            if o == 'do()':
                skip = False
            continue
        if o == "don't()":
            skip = True
            continue
        if o.startswith('mul'):
            result = result + int(x) * int(y)


    return result