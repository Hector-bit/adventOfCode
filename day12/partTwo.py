from os import posix_fallocate
from typing import DefaultDict


def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }

def move_Here(direction, distance, pos):
    if direction == 90:
        pos[0] += distance
    elif direction == 180:
        pos[1] += -distance
    elif direction == 270:
        pos[0] += -distance
    elif direction == 0 or direction == 360:
        pos[1] += distance
    print("new pos: ", pos)
    return pos

with open('data.txt') as raw_input:
    waypoint = [10, 1]
    facing = 90
    position = [0, 0]
    dictionary_for_directions = {
        "E": 90,
        "S": 180,
        "N": 0,
        "W": 270
    }
    for i in raw_input:
        instru = i[:1]
        measure = int(i[1:])
        if instru in dictionary_for_directions:
            print(instru, "this gfam here")
            temp = 0
            temp += facing
            facing = dictionary_for_directions.get(instru)
            # print(facing, 'not the temp', temp, '<-- tmep')
            position = move_Here(facing, measure, position)
            facing = temp % 360
        elif instru == "R":
            facing += measure
            facing = (facing % 360)
            # print(facing, "from the tihihg")
            # pos = move_Here(facing, measure, position)
        elif instru == "L":
            facing -= measure
            facing = (facing % 360)
        elif instru == "F":
            print("found the F", instru)
            position = move_Here(facing, measure, position)
            # print("new pos from F: ", pos)
    print("Facing: ", facing, " Position: ", position)
    print(abs(position[0]) + abs(position[1]))
