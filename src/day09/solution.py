def readDiskmap(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip()
    return data

def part1_checksum(file_path):
    diskMap = readDiskmap(file_path)
    fs = convert2FileSystem(diskMap)
    print(fs)
    output = compress(fs)

    print(output)
    hash = []
    for i, val in enumerate(output):
        if val == '.':
            break
        hash.append(i * int(val))
    return sum(hash)

def compress(fs):
    r = iCompress(fs)
    r2 = iCompress(r)
    if (r == r2):
        return r
    else:
        return compress(r)

def iCompress(fs):
    freeSpace = [i for i in range(len(fs)) if fs[i] == '.'][::-1]
    lfs = list(fs)
    for i in range(len(lfs))[::-1]:
        if lfs[i] != '.':
            ff = freeSpace.pop()
            if i < ff:
                break
            lfs[ff] = lfs[i]
            lfs[i] = '.'
            if len(freeSpace) == 0:
                break
    r = ''.join(lfs)
    return r

def convert2FileSystem(diskMap):
    fs = ""
    id = int(0)
    for i in range(len(diskMap)):
        if i % 2 == 0:
            for j in range(int(diskMap[i])):
                fs = fs + str(id)
            id += 1
        else:
            for j in range(int(diskMap[i])):
                fs = fs + '.'
    return fs