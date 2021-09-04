#not sure how to go about this one????
#I can create a loop craeteing a list of coordinates i have been to for both wires
#then find intersections based on those coordinates
#also the main port will be zero zero
import math
intersections = []
#keep in mind the main port is (0,0)
f = open('data.txt')
wireOne = f.readline()
wireTwo = f.readline()
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
    print(myArray, '============')
    return myArray
firstWire = wireCounter(wireOne)
secondWire = wireCounter(wireTwo)

for i in firstWire:
    if i in secondWire:
        intersections.append(i)
shortestPath = abs(intersections[0][0]) + abs(intersections[0][1])

for i in intersections:
    mathy = abs(i[0]) + abs(i[1])
    if mathy < shortestPath:
        shortestPath = mathy

print("done: ", shortestPath)
