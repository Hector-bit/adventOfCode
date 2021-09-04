import fileinput 
import re 
import itertools


def solve(p1, cycles):
    ON = set()
    L = list([l.strip() for l in fileinput.input('test.txt')])
    for index, l in enumerate(L):
        for indexCH, ch in enumerate(l):
            if ch == '#':
                ON.add((index,indexCH,0,0))
    for _ in range(cycles):
        NEW_ON = set()
        CHECK = set()
        for (x,y,z,w) in ON:
            for dx, dy, dz, dw in itertools.product([-1,0,1], repeat=4):
                if w+dw==0 or (not p1):
                    CHECK.add((x+dx, y+dy, z+dz, w,dw))
    print("here", len(CHECK), 'other', len(NEW_ON))
    print(ON)
print(solve(True, 5))

