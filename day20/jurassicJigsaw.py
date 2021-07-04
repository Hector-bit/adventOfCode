import math
import numpy

def compTB(one, two):
    left = []
    right = []
    bottom = one[-1]
    top = one[0]
    for i in one:
        left

with open('test.txt') as raw_input:
    maps = {}
    id = None
    curr_map = []
    #This first part gets the tile id's to match the tile in a dictionary
    for i in raw_input:
        print(i)
        if "Tile" in i:
            id = i[5:-2].replace("\n", "")
        elif "#" in i or "." in i:
            curr_map.append(i.replace("\n",""))
        else:
            maps[str(id)] = curr_map
            id = None
            curr_map = []
    print(maps)
    #here we need a way to match add 
    #first we find all that match with no 2d array manipulation
    idArray = [[[] for x in range(int(math.sqrt(len(maps))))]]
    
    while len(idArray) is not len(maps):
        for i in maps:
            #compare all sides
            for j in maps:
                #compare tops and bottoms
                connect = compTB(maps[i], maps[j])
                if connect and i is not j:
                    print(maps[i])
                    rotated = numpy.flip(maps[j])
                    print(rotated)
                    maps[i + " " + j] = maps[i] + list(rotated)
                    del maps[i]
                    del maps[j]
                    break
                # elif connect == "BOTTOM" and i is not j:
                #     print(maps[i])
                #     rotated = numpy.flip(maps[i])
                #     rot = numpy.flip(maps[j])
                #     print(rotated)
                #     maps[i + " " + j] = list(rotated) + list(rot)
                #     del maps[i]
                #     del maps[j]
                #     break
            break
        print(maps)
    print(maps)



