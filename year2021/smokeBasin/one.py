
with open('data.txt') as raw_input:
    def CountSum(arr):
        total = 0
        for i in arr:
            total += int(i)
            total += 1
        return total
    #prints floormap neatly
    def PrintFloor(arr):
        for i in arr:
            print(i)
    #returns arr of lowpoints
    def LowPoints(arr):
        lp = []
        countme = 0
        for indexI, i in enumerate(arr):
            for indexJ, j in enumerate(i):
                #check adjacents, if all are higher then add to lp list
                checks = [[indexI+1,indexJ],[indexI-1,indexJ],[indexI,indexJ+1],[indexI,indexJ-1]] 
                adjacentSpots = []
                isLowest = True
                arrmaxver = len(arr)
                arrmaxhori = len(arr[0])
                for check in checks:
                    if arrmaxver > check[0] and check[0] > -1 and arrmaxhori > check[1] and check[1] > -1:
                        adjacentSpots.append(arr[check[0]][check[1]])
                if len(adjacentSpots) == 3:
                    countme += 1
                for spot in adjacentSpots:
                    if int(spot) <= int(j):
                        isLowest = False
                if isLowest:
                    lp.append(j)
        print('counted this many: ' + str(countme))
        return lp

    floorMap = []
    for i in raw_input:
        row = []
        snip = i[:-1]
        for j in snip:
            row.append(j)
        floorMap.append(row)
    print('ROW: ' + str(len(floorMap[0])))
    print('COL: ' + str(len(floorMap)))
    lowPoints = LowPoints(floorMap)
    tot = CountSum(lowPoints)
    print('TOTAL: ' + str(tot))
