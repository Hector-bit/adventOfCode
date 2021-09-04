
f = open('data.txt')
wireOne = f.readline()
wireTwo = f.readline()
#find the first intersection
coordinateUno = [0,0]
coordinateDos = [0,0]

def wireCounter(wire):
    myArray = []
    coordinates = [0,0]
    wireList = wire.split(",")
    for i in wireList:
        letter = i[0:1]
        number = int(i[1:])
        temp = []
        if letter == 'R':
            for i in range(number):
                coordinates[0] = coordinates[0] + 1
                temptemp = coordinates.copy()
                temp.append(temptemp)
        elif letter == 'L':
            for i in range(number):
                coordinates[0] = coordinates[0] - 1
                temptemp = coordinates.copy()
                temp.append(temptemp)
        elif letter == 'U':
            for i in range(number):
                coordinates[1] = coordinates[1] + 1
                temptemp = coordinates.copy()
                temp.append(temptemp)
        elif letter == 'D':
            for i in range(number):
                coordinates[1] = coordinates[1] - 1
                temptemp = coordinates.copy()
                temp.append(temptemp)
        myArray = myArray + temp
    return myArray
uno = wireCounter(wireOne)
dos = wireCounter(wireTwo)
print(uno)
print(dos)
countOne = 0
countTwo = 0
firstIntersection = None
for i in uno:
    for j in dos:
        if i == j:
            firstIntersection = i
            break
    else:
        continue
    break
for i in uno:
    countOne += 1
    if i == firstIntersection:
        break
for i in dos:
    countTwo += 1
    if i == firstIntersection:
        break
print("Travel Distance: ", countOne+countTwo)
