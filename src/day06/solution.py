def load_map_to_dict(file_path):
    """
    Laad een kaart uit een tekstbestand en zet het om naar een dictionary.
    Elke cel krijgt coördinaten (rij, kolom) als sleutel.
    """
    map_dict = {}
    obstructions = []
    start = 0
    
    with open(file_path, 'r') as file:
        for row_index, line in enumerate(file):
            # Strip whitespace en lees elke regel
            line = line.strip()
            for col_index, char in enumerate(line):
                map_dict[(row_index, col_index)] = char
                if char == '#':
                    obstructions.append((row_index, col_index))
                if char == '^':
                    start = (row_index, col_index)
    
    return map_dict, obstructions, start

def part1(file_path):
    map_d, obstructions, start = load_map_to_dict(file_path)
    visitedpositions = {start}
    nextPosition = start # row, col
    direction = '^'
    while nextPosition != None:
        nextPosition, direction = getNextPosition(nextPosition,map_d,obstructions,direction)
        print(nextPosition)
        if nextPosition != None:
            visitedpositions.add(nextPosition)

    return len(visitedpositions)

def getNextPosition(currentpos, map_d:dict, obstructions,direction):
    if direction == '^':
        nextPosition = (currentpos[0] - 1, currentpos[1])
        if nextPosition not in map_d.keys():
            return None, None
        if nextPosition in obstructions:
            nextPosition = (currentpos[0], currentpos[1] + 1)
            return nextPosition, '>'
        else:
            return nextPosition, direction
    if direction == '>':
        nextPosition = (currentpos[0], currentpos[1] + 1)
        if nextPosition not in map_d.keys():
            return None, None
        if nextPosition in obstructions:
            nextPosition = (currentpos[0] + 1, currentpos[1])
            return nextPosition, 'v'
        else:
            return nextPosition, direction
    if direction == 'v':
        nextPosition = (currentpos[0] + 1, currentpos[1])
        if nextPosition not in map_d.keys():
            return None, None
        if nextPosition in obstructions:
            nextPosition = (currentpos[0], currentpos[1] - 1)
            return nextPosition, '<'
        else:
            return nextPosition, direction
        
    if direction == '<':
        nextPosition = (currentpos[0], currentpos[1] - 1)
        if nextPosition not in map_d.keys():
            return None, None
        if nextPosition in obstructions:
            nextPosition = (currentpos[0] - 1, currentpos[1])
            return nextPosition, '^'
        else:
            return nextPosition, direction
        
def part2(file_path):
    map_d, obstructions, start = load_map_to_dict(file_path)
    nextPosition = start # row, col
    direction = '^'
    visitedpositions = [(start, direction)]
    while nextPosition != None:
        nextPosition, direction = getNextPosition(nextPosition,map_d,obstructions,direction)
        if nextPosition != None:
            visitedpositions.append((nextPosition,direction))

    print (visitedpositions)
    causeLoop = list(v for v in visitedpositions if isCauseLoop(v, visitedpositions, obstructions, map_d))
    print(causeLoop)
    return len(causeLoop)

def isCauseLoop(v, visitedpostions, obstructions, map_d):
    position = v[0]
    direction = v[1]
    if direction == '^':
        nextPosition = (position[0] - 1, position[1])
        if nextPosition in obstructions:
            return False
        nextWhenBlocked = (position[0], position[1] + 1)
        nextDirectionWhenBlocked = '>'
        if arriveInMatchingVisitedPostion(visitedpostions, nextWhenBlocked, nextDirectionWhenBlocked, map_d):
            return True
    if direction == '>':
        nextPosition = (position[0], position[1] + 1)
        if nextPosition in obstructions:
            return False
        nextWhenBlocked = (position[0] + 1, position[1])
        nextDirectionWhenBlocked = 'v'
        if arriveInMatchingVisitedPostion(visitedpostions, nextWhenBlocked, nextDirectionWhenBlocked, map_d):
            return True

    if direction == 'v':
        nextPosition = (position[0] + 1, position[1])
        if nextPosition in obstructions:
            return False
        nextWhenBlocked = (position[0], position[1] - 1)
        nextDirectionWhenBlocked = '<'
        if arriveInMatchingVisitedPostion(visitedpostions, nextWhenBlocked, nextDirectionWhenBlocked, map_d):
            return True

    if direction == '<':
        nextPosition = (position[0], position[1] - 1)
        if nextPosition in obstructions:
            return False
        nextWhenBlocked = (position[0] - 1, position[1])
        nextDirectionWhenBlocked = '^'
        if arriveInMatchingVisitedPostion(visitedpostions, nextWhenBlocked, nextDirectionWhenBlocked, map_d):
            return True

    return False

def arriveInMatchingVisitedPostion(visitedpostions, nextWhenBlocked, nextDirectionWhenBlocked, map_d):
    if (nextWhenBlocked, nextDirectionWhenBlocked) in visitedpostions:
        print("y")
        print(nextWhenBlocked)
        print(nextDirectionWhenBlocked)
        print(visitedpostions)
        print("x")
        return True
    else:
        if nextDirectionWhenBlocked == '^':
            nextPosition = (nextWhenBlocked[0] - 1, nextWhenBlocked[1])
            if nextPosition not in map_d.keys():
                return False
            return arriveInMatchingVisitedPostion(visitedpostions, nextPosition, nextDirectionWhenBlocked, map_d)
        if nextDirectionWhenBlocked == '>':
            nextPosition = (nextWhenBlocked[0], nextWhenBlocked[1] + 1)
            if nextPosition not in map_d.keys():
                return False
            return arriveInMatchingVisitedPostion(visitedpostions, nextPosition, nextDirectionWhenBlocked, map_d)
        if nextDirectionWhenBlocked == 'v':
            nextPosition = (nextWhenBlocked[0] + 1, nextWhenBlocked[1])
            if nextPosition not in map_d.keys():
                return False
            return arriveInMatchingVisitedPostion(visitedpostions, nextPosition, nextDirectionWhenBlocked, map_d)
            
        if nextDirectionWhenBlocked == '<':
            nextPosition = (nextWhenBlocked[0], nextWhenBlocked[1] - 1)
            if nextPosition not in map_d.keys():
                return False
            return arriveInMatchingVisitedPostion(visitedpostions, nextPosition, nextDirectionWhenBlocked, map_d)
