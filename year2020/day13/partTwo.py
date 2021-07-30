from os import terminal_size
from typing import TYPE_CHECKING

#BELOW IS PROBLEM DATA
time = 0
arrival = 1002632
#BELOW IS TEST DATA
# time = 939
# arrival = 939

def check(arr, time):
    time -= 24
    for i in arr:
        if i != '':
            if time % int(i) != 0:
                return False
        time += 1
    return True

def check_mod(timestamp, arr):
    # print(arr)
    for i in arr:
        # print("timestamp: ", timestamp, " moding by: ", i)
        if i != '':
            mathy = timestamp % int(i)
            print("Timestamp: ", timestamp, " Moded: ", i, " Mathy: ", mathy)
            if mathy != 0:
                return False
        timestamp += 1
    return True

def partTwo(arr):
    #this will my own solution
    # thingy = int(arr[0])
    thingy = 0
    while True:
        myMath = thingy % int(arr[0])
        if myMath == 0:
            if check_mod(thingy, arr):
                print("pick it up bitch")
                return thingy
        thingy += int(arr[0])

with open('data.txt') as raw_input:
    busses = []
    temp = ""
    for i in raw_input:
        for j in i:
            if j == ',':
                busses.append(temp)
                temp = ""
            elif j.isnumeric():
                temp += j 
        busses.append(temp)
    # print("looky here: ", busses)
    print(partTwo(busses))