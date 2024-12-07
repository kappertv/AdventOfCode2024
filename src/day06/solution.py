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
        