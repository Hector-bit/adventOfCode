tie

with open('data.txt') as raw_input:
    busses = []
    temp = ""
    for i in raw_input:
        for j in i:
            if j == ',':
                print(temp)
                if temp is not '':
                    busses.append(temp)
                    temp = ""
            elif j.isnumeric():
                temp += j
    print(busses)