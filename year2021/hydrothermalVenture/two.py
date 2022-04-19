
def drawLine(mat, start, end):
    xOne = int(start[0])
    xTwo = int(end[0])
    yOne = int(start[1])
    yTwo = int(end[1])
    xDelta = xTwo - xOne
    yDelta = yTwo - yOne
    print("X delta: " + str(xDelta)+ "  :::::::  Y Delta: " + str(yDelta))
    # Checks for horizantal line
    if xDelta != 0 and yDelta == 0:
        print("HORIZANTAL")
        myStart = 0
        myEnd = xDelta+1
        if xDelta < 0:
            temp = myStart
            myStart = myEnd-1
            myEnd = temp+1
        for i in range(myStart, myEnd):
            spot = mat[xOne + i][yOne]
            if spot == '.':
                mat[xOne+i][yOne] = periodOrNum(spot)
            elif spot != '.':
                mat[xOne+i][yOne] = periodOrNum(spot)
    # Checks for vertical line
    elif xDelta == 0 and yDelta !=0:
        print("VERTICAL")
        myStart = 0
        myEnd = yDelta+1
        if yDelta < 0:
            temp = myStart
            myStart = myEnd-1
            myEnd = temp+1
        for i in range(myStart, myEnd):
            spot = mat[xOne][yOne + i]
            if spot == '.':
                mat[xOne][yOne + i] = periodOrNum(spot)
            elif spot != '.':
                mat[xOne][yOne + i] = periodOrNum(spot)
    #if both delta's change then do a diagnol line
    elif xDelta != 0 and yDelta != 0:
        print("DIAGNOL START from :: " + str(xOne) + ", " +str(yOne))
        getRange = abs(xDelta)+1
        for i in range(getRange):
            if xDelta > 0 and yDelta > 0:
                mat[xOne+i][yOne+i] = periodOrNum(mat[xOne+i][yOne+i])
            elif xDelta > 0 and yDelta < 0:
                mat[xOne+i][yOne-i] = periodOrNum(mat[xOne+i][yOne-i])
            elif xDelta < 0 and yDelta > 0:
                mat[xOne-i][yOne+i] = periodOrNum(mat[xOne-i][yOne+i])
            elif xDelta < 0 and yDelta < 0:
                mat[xOne-i][yOne-i] = periodOrNum(mat[xOne-i][yOne-i])
            else:
                print('something went wrong... xdelta- '+str(xDelta) + ' ydelta- '+str(yDelta)) 
    return mat

def periodOrNum(spot):
    if spot == ".":
        return "1"
    else:
        return str(int(spot)+1)

def countOverLaps(mat, pointOverlaps):
    count = 0
    for i in mat:
        for j in i:
            if j.isdigit():
                if int(j) >= pointOverlaps:
                    count += 1
    return count

def printMat(mat):
    for i in range(len(mat)-1, -1, -1):
        print(mat[i])


with open('data.txt') as raw_input:
    #9 by 9 matrix for the test file
    seaFloor = []
    for y in range(1000):
        row = []
        for x in range(1000):
            row.append(".")
        seaFloor.append(row)
    #for i in seaFloor:
     #   print(i)
    
    for i in raw_input:
        i = i[:-1]
        splitted = i.split(" -> ")
        ventStart = splitted[0].split(',')
        ventEnd = splitted[1].split(',')
        seaFloor = drawLine(seaFloor, ventStart, ventEnd)
    print(countOverLaps(seaFloor, 2))
        
    

