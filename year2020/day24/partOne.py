#you can simulate a hexgon style grid useing 3 axis cartesian grid
#so just use that 

stepper = {'e': 'east', 'se': 'southEast', 'sw': 'southWest', 'w':'west', 'nw':'northWest', 'ne':'northEast'}
directions = {'east':'goEast', 'southEast':'goSouthEast', 'southWest':'goSouthWest', 'west':'goWest', 'northWest':'goNorthWest', 'northEast':'goNorthEast'}

tiles = {}

def colorChange(color):
    if color == 0:
        return 1
    elif color == 1:
        return 0

def sumOf(coor):
    #sum = 0
    #changer = 345
    #for i in coor:
    #    sum += i
    #    sum = sum * changer
    #return sum
    summer = str(coor[0]) + ',' + str(coor[1]) + ',' + str(coor[2])
    return summer

black_tiles = set()
with open('test.txt') as raw_input:
    for i in raw_input:
        print(i)
        meme = list(i)
        coordinates = [0,0,0]
        readstart = 0
        readend = 0
        # print(meme)
        for j in range(len(meme)):
            readend = j
            joined = ''.join(meme[readstart:readend])
            # print(joined)
            if joined in stepper.keys():
                if joined == 'e':
                    #west 0
                    coordinates[0] += 1
                    coordinates[1] -= 1
                if joined == 'se':
                    #northWest 1
                    coordinates[2] += 1
                    coordinates[1] -= 1
                elif joined == 'sw':
                    #northEast 2
                    coordinates[2] += 1
                    coordinates[0] -= 1
                elif joined == 'w':
                    #east 0
                    coordinates[0] -= 1
                    coordinates[1] += 1
                elif joined == 'nw':
                    #southeast 1
                    coordinates[2] -= 1
                    coordinates[1] += 1 
                elif joined == 'ne':
                    #southwest 2
                    coordinates[2] -= 1
                    coordinates[0] += 1
                else:
                    print("something went wrong:", joined)
                readstart = j
        print(len(black_tiles), "looky")
        key = sumOf(coordinates)
        if key in black_tiles:
            print('remove')
            black_tiles.remove(key)
        else:
            black_tiles.add(key)
    total = 0
    totalTwo = 0
    for i in tiles.values():
        if i == 0:
            total += 1
        else:
            totalTwo += 1
    print(black_tiles)
    print("new test:", len(black_tiles))
    print("all white???:",totalTwo)
    print("all blacks:", total)


