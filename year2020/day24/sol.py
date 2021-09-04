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

for path in paths:
    coord = (0, 0, 0)
    for p in path:
        coord = tuple([a + b for a, b in zip(coord, dirs[p])])
    if coord in black_tiles:
        black_tiles.remove(coord)
    else:
        black_tiles.add(coord)

for 

print(f"Part 1: {len(black_tiles)}")

