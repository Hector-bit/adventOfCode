from os import terminal_size

#BELOW IS PROBLEM DATA
time = 1002632
arrival = 1002632
#BELOW IS TEST DATA
# time = 939
# arrival = 939
travel_by = 829

def doubleCheck(arr, time):
    for i in arr:
        if i is not '':
            if time % int(i) != 0:
                print("This time did not work: ", time)
                return False
    return True

def checkIfWorks(arr, time):
    if (time - 23) % 23 == 0:
        print(time, "<== TIME")
        if doubleCheck(arr, time):
            return True
        return False


def partTwo(arr):
    global time
    global travel_by
    while True:
        if time % travel_by == 0:
            for _ in range(len(arr)):
                if checkIfWorks(arr, time):
                    print("I found the time: ", time)
                    return
                time += travel_by
        time += 1

        


with open('data.txt') as raw_input:
    busses = []
    temp = ""
    for i in raw_input:
        for j in i:
            if j == ',':
                # print(temp)
                busses.append(temp)
                temp = ""
            elif j.isnumeric():
                temp += j 
    print("DONE COLLECTING:", busses) 
    print(partTwo(busses))