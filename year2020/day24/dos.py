dirs = {
    "e": [1, -1, 0],
    "s": [0, -1, 1],  # s == se
    "S": [-1, 0, 1],  # S == sw
    "w": [-1, 1, 0],
    "N": [0, 1, -1],  # N == nw
    "n": [1, 0, -1],  # n == ne
}


with open("data.txt") as f:
    paths = [
        l.strip()
        .replace("sw", "S")
        .replace("se", "s")
        .replace("nw", "N")
        .replace("ne", "n")
        for l in f.readlines()
    ]


black_tiles = set()
white_tiles = set()
for path in paths:
    coord = (0, 0, 0)
    for p in path:
        coord = tuple([a + b for a, b in zip(coord, dirs[p])])
    white_tiles.add(coord)
    if coord in black_tiles:
        black_tiles.remove(coord)
    else:
        black_tiles.add(coord)

for i in black_tiles:
    if i in white_tiles:
        white_tiles.remove(i)

def getNeighbors(pos):
    blackNeighbors = 0
    for i in dirs:
        coord = tuple(zip(pos,i))
        if coord in black_tiles:
            blackNeighbors += 1
    return blackNeighbors

def getWhiteNeighbors(pos):
    blackNeighbors = 0
    for i in dirs:
        coord = tuple(zip(pos,i))
        if coord in black_tiles:
            blackNeighbors += 1
    return blackNeighbors
#switchToWhite = set()
#switchToBlack = set()
for _ in range(100):
    new_tiles = set()
    to_check = set()
    for i in black_tiles:
        to_check.add(i)
        for diff in dirs.values():
            to_check.add(tuple([a + b for a, b in zip(i, diff)]))
    for i in to_check:
        num_neigh = sum([tuple(a+b for a, b in zip(i, d)) in black_tiles for d in dirs.values()])
        if (i in black_tiles and 0 < num_neigh <= 2) or (i not in black_tiles and num_neigh == 2):
            new_tiles.add(i)
    black_tiles = new_tiles

print(len(white_tiles))

print(f"Part 1: {len(black_tiles)}")
