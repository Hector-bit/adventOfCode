
with open('test.txt') as raw_input:
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
        lp = [] #what is this??
        countme = 0
        for indexI, i in enumerate(arr):
            for indexJ, j in enumerate(i):
                #check adjacents, if all are higher then add to lp list
                checks = [[indexI+1,indexJ],[indexI-1,indexJ],[indexI,indexJ+1],[indexI,indexJ-1]] 
                adjacentSpots = []
                isLowest = True
                arrmaxver = len(arr)
                arrmaxhori = len(arr[0])
                basin = []
                for check in checks:
                    if arrmaxver > check[0] and check[0] > -1 and arrmaxhori > check[1] and check[1] > -1:
                        adjacentSpots.append(arr[check[0]][check[1]])
                        basin.append([check[0],check[1]])
                if len(adjacentSpots) == 3:
                    countme += 1
                for spot in adjacentSpots:
                    if int(spot) <= int(j):
                        isLowest = False
                if isLowest:
                    lp.append(j)
                    basin.append([indexI,indexJ])
                    basinSize = 0
                    while len(basin) > 0:
                        ss = basin[0]
                        basinval = int(arr[ss[0]][ss[1]])
                        checks = [[ss[0]+1,ss[1]],[ss[0]-1,ss[1]],[ss[0],ss[1]+1],[ss[0],ss[1]-1]] 
                        basin.pop(0)
                        for check in checks:
                            if arrmaxver > check[0] and check[0] > -1 and arrmaxhori > check[1] and check[1] > -1:
                                ssval = int(arr[check[0]][check[1]]) - 1
                                if ssval >= 8:
                                    continue
                                elif ssval == basinval:
                                    basin.append([check[0],check[1]])
                                    basinSize += 1
                    print(basinSize)
        print('counted this many: ' + str(countme))
        return lp


    def CountBasins(floorArr):

        def NeighborCheck(coor):
            basinNeighbors = []
            y = coor[0]
            x = coor[1]
            floorPiece = floorArr[y][x]
            if floorPiece != '9' or floorPiece != '#':
                #start counting adjacent nums
                floorArr[coor[0]][coor[1]] = '#'
                #add neightbors to watchlist
                localNeightbors = [[y-1, x],[y, x+1],[y-1, x],[y, x-1]]
                for _ in localNeightbors:
                    neigh = floorArr[_[0]][_[1]]
                    if neigh != '#' and neigh != '9' and neigh != 9:
                        basinNeighbors.append(_)
            return basinNeighbors

        basinsArr = []
        for indexI, i in enumerate(floorArr):
            for indexJ, j in enumerate(i):
                #Now we can count individaul spots
                basinSize = 0
                basinNeighbors = []
                if j != '9' and j != '#' and j !=9:
                    #start counting adjacent nums
                    basinSize += 1
                    floorArr[indexI][indexJ] = '#'
                    #add neightbors to watchlist
                    basinNeighbors = [[indexI-1, indexJ],[indexI+1, indexJ],[indexI, indexJ+1],[indexI, indexJ-1]]
                while len(basinNeighbors) != 0:
                    print(basinNeighbors)
                    aNeighbor = basinNeighbors.pop()
                    if aNeighbor != '9' and aNeighbor != '#':
                        floorArr[aNeighbor[0]][aNeighbor[1]] = '#'
                    moreNeighbors = NeighborCheck(aNeighbor)
                    for __ in moreNeighbors:
                        basinNeighbors.append(__)
                
                basinsArr.append(basinSize)
        return basinsArr
                    

    floorMap = []
    for i in raw_input:
        row = []
        snip = i[:-1]
        row.append('#')
        for j in snip:
            row.append(j)
        row.append('#')
        floorMap.append(row)
    snip += ('##')
    coollistthing = ['#' for x in snip]
    floorMap.append(coollistthing)
    floorMap.insert(0,coollistthing)
    PrintFloor(floorMap)
    basins = CountBasins(floorMap)
    PrintFloor(floorMap)
    print('TOTAL: ')
    print(basins)
