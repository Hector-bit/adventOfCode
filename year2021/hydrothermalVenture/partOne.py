def drawLine(mat, start, end):
    xOne = int(start[0])
    xTwo = int(end[0])
    yOne = int(start[1])
    yTwo = int(end[1])
    xDelta = xTwo - xOne
    yDelta = yTwo - yOne
    print("X delta: " + str(xDelta) + " Y Delta: " + str(yDelta))
    # Checks for horizantal line
    if xDelta != 0 and yDelta == 0:
        myStart = 0
        myEnd = xDelta+1
        if xDelta < 0:
            temp = myStart
            myStart = myEnd-1
            myEnd = temp+1
        for i in range(myStart, myEnd):
            spot = mat[xOne + i][yOne]
            if spot == '.':
                spot = 1
                mat[xOne+i][yOne] = 1
            elif spot != '.':
                mat[xOne+i][yOne] +=1
    # Checks for vertical line
    elif xDelta == 0 and yDelta !=0:
        myStart = 0
        myEnd = yDelta+1
        if yDelta < 0:
            temp = myStart
            myStart = myEnd-1
            myEnd = temp+1
        for i in range(myStart, myEnd):
            spot = mat[xOne][yOne + i]
            if spot == '.':
                mat[xOne][yOne + i] = 1
            elif spot != '.':
                mat[xOne][yOne + i] += 1
    #if both delta's are not zero then ignore
    return mat

def countOverLaps(mat, pointOverlaps):
    count = 0
    for i in mat:
        for j in i:
            if type(j) == int:
                if j >= pointOverlaps:
                    count += 1
    return count

def printMat(mat):
    for i in mat:
        print(i)


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
        
    

