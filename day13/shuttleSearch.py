from os import terminal_size

#BELOW IS PROBLEM DATA
time = 1002632
arrival = 1002632
#BELOW IS TEST DATA
# time = 939
# arrival = 939

def partOne(arr):
    global time
    while True:
        for i in arr:
            if time % int(i) == 0:
                print("Bus id: ", i)
                print("TIME: ", time)
                return int(i) * (time - arrival)
        time += 1
        


with open('data.txt') as raw_input:
    busses = []
    temp = ""
    for i in raw_input:
        for j in i:
            if j == ',':
                # print(temp)
                if temp is not '':
                    busses.append(temp)
                    temp = ""
            elif j.isnumeric():
                temp += j 
    print("DONE COLLECTING:", busses) 
    print(partOne(busses))