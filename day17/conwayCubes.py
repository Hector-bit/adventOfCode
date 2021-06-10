def countAlivePoints(dictionary):
    thingy = 0
    # print(dictionary)
    for i in dictionary.values():
        if i == 'ACTIVE':
            thingy += 1
    return thingy

def addboxes(book, boxMethod):
    add = []
    prev_point = (0,0,0)
    for i in book.keys():
        for check in boxMethod:
            if check not in book.keys():
                add.append(check)
        curr_point = i
        #adjust the box as needed
        x = curr_point[0] - prev_point[0]
        y = curr_point[1] - prev_point[1]
        z = curr_point[2] - prev_point[2]
        for index, num in enumerate(boxMethod):
            rx = num[0] + x
            ry = num[1] + y
            rz = num[2] + z
            boxMethod[index] = (rx, ry, rz)
        prev_point = i
    for thing in add:
        book[thing] = "INACTIVE"

def setBox(cb):
    return [(cb[0]+1, cb[1], cb[2]),(cb[0] + 1, cb[1] + 1, cb[2]),(cb[0], cb[1] + 1, cb[2]),(cb[0] + -1, cb[1] + 1, cb[2]),(cb[0] + -1, cb[1], cb[2]), (cb[0]-1, cb[1]-1, cb[2]),(cb[0], cb[1]-1, cb[2]) ,(cb[0] + 1, cb[1]-1, cb[2]) ,(cb[0]+1, cb[1], cb[2]-1),(cb[0] + 1, cb[1]+1,cb[2]-1),(cb[0], cb[1]+1,cb[2]-1),(cb[0]+-1, cb[1]+1,cb[2]-1),(cb[0]+-1, cb[1], cb[2]-1),(cb[0]+-1,cb[1]-1,cb[2]-1),(cb[0], cb[1]-1,cb[2]-1),(cb[0]+1,cb[1]-1,cb[2]-1),(cb[0]+1, cb[1], cb[2]+1),(cb[0] + 1,cb[1]+1,cb[2]+1),(cb[0], cb[1]+1,cb[2]+1),(cb[0]+-1,cb[1]+1,cb[2]+1),(cb[0]-1, cb[1], cb[2]+1),(cb[0]-1,cb[1]-1,cb[2]+1),(cb[0], cb[1]-1,cb[2]+1),(cb[0]+1,cb[1]-1,cb[2]+1),(cb[0],  cb[1], cb[2]+1),(cb[0], cb[1], cb[2]-1)]

def cycle(cycles, dict):
    #go through the dictionary and apply the rules
    for _ in range(cycles):
        boxMethod = [(1,0,0),(1,1,0),(0,1,0),(-1,1,0),(-1,0,0),(-1,-1,0),(0,-1,0),(1,-1,0),(1,0,-1),(1,1,-1),(0,1,-1),(-1,1,-1),(-1,0,-1),(-1,-1,-1),(0,-1,-1),(1,-1,-1),(1,0,1),(1,1,1),(0,1,1),(-1,1,1),(-1,0,1),(-1,-1,1),(0,-1,1),(1,-1,1),(0,0,1),(0,0,-1)]
        prev_point = (0,0,0)
        destroyPoint = []
        activatePoint = []
        #make sure all the boxMethods points are in the dictionary
        addboxes(dict, boxMethod.copy())
        for cb in dict.keys():
            boxMethod = setBox(cb)
            curr_point = cb
            #adjust the box as needed
            x = curr_point[0] - prev_point[0]
            y = curr_point[1] - prev_point[1]
            z = curr_point[2] - prev_point[2]
            for index, num in enumerate(boxMethod):
                rx = num[0] + x
                ry = num[1] + y
                rz = num[2] + z
                boxMethod[index] = (rx, ry, rz)
            # print(boxMethod, '/n/n')
            #check neighbors
            aliveNeighbors = 0
            for neighbor in boxMethod:
                if neighbor in dict.keys():
                    if dict[neighbor] == "ACTIVE":
                        aliveNeighbors += 1
            #check if point should become alive or dead
            if dict[cb] == "ACTIVE":
                if aliveNeighbors == 2 or aliveNeighbors == 3:
                    continue
                else:
                    destroyPoint.append(cb)
            elif dict[cb] == "INACTIVE":
                if aliveNeighbors == 3:
                    activatePoint.append(cb)
            prev_point = cb
        print(destroyPoint, activatePoint)
        for a in activatePoint:
            dict[a] = "ACTIVE"
        for d in destroyPoint:
            dict[d] = "INACTIVE"
        # dict[(0,0,0)] = "BITCHES"
    return countAlivePoints(dict)

with open('test.txt') as raw_input:
    #going to keep track of seen points in a dictionary(loving dictionarys rn, so quick)
    smart_dict = {}
    #you read that data as (x, y, 0)
    #z in the data is always zero
    for indexI, i in enumerate(raw_input):
        for indexJ, j in enumerate(i):
            #we want add all these points to the smart_dict
            #key is an array[x,y,z]
            if j == '#':
                smart_dict[(indexJ, -indexI, 0)] = "ACTIVE"
            elif j == '.':
                smart_dict[(indexJ, -indexI, 0)] = "INACTIVE"
    #at this point we can now cycle 6 times using our dictionary
    print(cycle(1, smart_dict))