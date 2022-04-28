#just reading the output from the line and only 1, 4, 7, and 8

with open("data.txt") as raw_input:
    ones = 0
    fours = 0
    sevens = 0
    eights = 0
    for i in raw_input:
        splitted = i.split(" | ")
        output = splitted[1][:-1].split(" ")
        print(output)
        for i in output:
            ll = len(i)
            if ll == 2:
                ones +=1
            elif ll == 4:
                fours +=1
            elif ll == 3:
                sevens +=1
            elif ll == 7:
                eights += 1
    print(ones + fours + sevens + eights)


