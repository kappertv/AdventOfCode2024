def allLines(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip()
    horlines = data.splitlines()

    vertical_lines = [''.join([row[col] for row in horlines]) for col in range(len(horlines[0]))]       

    result = []
    result.extend(horlines)
    result.extend(vertical_lines)
    result.extend(getDiagonals(horlines))

    reverselines = []
    for line in result:
        reverselines.append(line[::-1])
    result.extend(reverselines)


    return result

def getDiagonals(lines):
    # test = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

    max_col = len(lines[0])
    max_row = len(lines)
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(lines[y][x])
            rows[y].append(lines[y][x])
            fdiag[x+y].append(lines[y][x])
            bdiag[x-y-min_bdiag].append(lines[y][x])

    r = []
    for fd in fdiag:
        r.append(''.join(fd))

    for bd in bdiag:
        r.append(''.join(bd))

    return r

def part1(file_path):
    lines = allLines(file_path)
    # print(lines)
    # print(len(lines))
    s = sum(line.count('XMAS') for line in lines)
    return s
