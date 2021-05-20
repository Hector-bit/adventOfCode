import math
r = open('day5/seatData.txt', 'r').read().split()

input = r

def getID(myStr):
    upper = 0
    lower = 127
    middle = 0
    myStr = myStr[:7]
    for letter in myStr:
        middle = findMiddle(upper, lower)
        # print('Middle: ', middle, 'Letter: ', letter)
        if letter == 'F':
            lower = math.floor(middle)
            middle = math.floor(middle)
        elif letter == 'B':
            upper = math.ceil(middle)
            middle = math.ceil(middle)
    # print("row mid: ", middle)
    return middle
        
    

def findMiddle(num1, num2):
    middle = num2 - num1
    findMid = (middle / 2)
    # print("middle: ", num1 + findMid)
    return num1 + findMid

def getCol(anotherStr):
    #needs work
    anotherStr = anotherStr[-3:]
    # print(anotherStr)
    upper = 0
    lower = 7
    middle = 0
    for letter in anotherStr:
        middle = findMiddle(upper, lower)
        if letter == "L":
            lower = math.floor(middle)
            middle = math.floor(middle)
        elif letter == "R":
            upper = math.ceil(middle)
            middle = math.ceil(middle)
    # print("col mid: ", middle)
    return middle


def arrayOfIDS(data):
    idArray = []
    for i in data:
        idArray.append((getID(i) * 8) + getCol(i))
    print(idArray.sort(), "HEREERE")
    return idArray

def largestNum(arr):
    largest = 0
    for num in arr:
        if num > largest:
            largest = num
    return largest

def partTwo(array):
    #finds the missing id by counting and look for a skip
    count = array[0]
    for i in array:
        if i == count:
            count += 1
        else:
            return count
    
print(partTwo(arrayOfIDS(input)))
