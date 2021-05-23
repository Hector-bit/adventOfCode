from os import terminal_size

#BELOW IS PROBLEM DATA
time = 1000002632
arrival = 1002632
#BELOW IS TEST DATA
# time = 939
# arrival = 939

def check(arr, time):
    for i in arr:
        if i != '':
            if time % int(i) != 0:
                return False
        time += 1
    return True

def partTwo(arr, time):
    #without the chinese remainder theorum
    mod_me = 0
    

        


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
    print(partTwo(busses, time))