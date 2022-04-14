
with open("data.txt") as raw_input:
    coor = [0,0,0]
    for i in raw_input:
        splited = i.split(" ")
        instr = splited[0]
        amt = int(splited[1])
        if instr == "forward":
            coor[0] += amt
            coor[1] += (amt * coor[2])
        elif instr == "up":
            coor[2] -= amt
        elif instr == "down":
            coor[2] += amt
    print(coor)
    print("Total: " + str(coor[0] * coor[1]))


