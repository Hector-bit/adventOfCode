

def getNeighbors(someSet):
    # print(someSet, '<========')
    x, y, z = someSet
    # print(x, y, z, 'and then', someSet)
    newSet = set()
    for xdel in range(-1,2):
        for ydel in range(-1,2):
            for zdel in range(-1,2):
                neigh = (x + xdel, y + ydel, z + zdel)
                newSet.add(neigh)
    newSet.remove(someSet)
    return newSet

def stepSimulation(activeNodes):
    newNodes = set()
    activationCounts = {}
    for i in activeNodes:
        activeNeighbors = 0
        neighbors = getNeighbors(i)
        # print(neighbors)
        for n in neighbors:
            if n in activeNodes:
                activeNeighbors += 1
            else:
                if n not in activationCounts.keys():
                    activationCounts[n] = 1
                else:
                    activationCounts[n] += 1
        if activeNeighbors == 2 or activeNeighbors == 3:
            newNodes.add(i)
    for potential in activationCounts:
        if activationCounts[potential] == 3:
            newNodes.add(potential)
    # print(activationCounts)
    return newNodes

with open('data.txt') as raw_input:
    mySet = set()
    for indexI, i in enumerate(raw_input):
        for indexJ, j in enumerate(i):
            if j == "#":
                mySet.add((indexJ, indexI, 0))
    state = mySet
    for i in range(6):
        state = stepSimulation(state)
    print(len(state))
