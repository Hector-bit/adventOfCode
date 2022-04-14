

with open("data.txt") as raw_input:
    rows = 0
    counterArr = []
    #create counter array to count # of one's in each coloumn
    for i in raw_input:
        for x in i:
            if x == '0' or x =='1':
                counterArr.append(0)
        break
    gamma = counterArr
    epsilon = []
    #counts number of one's in each coloumn
    for i in raw_input:
        rows +=1
        for index, j in enumerate(i):
            if j == '1':
                counterArr[index] += 1
    #compare counterarr to get gamme and epsilon values
    for index, i in enumerate(counterArr):
        ones = i
        zeros = rows - counterArr[index]
        if ones > zeros:
            gamma[index] = 1
            epsilon.append(0)
        else:
            gamma[index] = 0
            epsilon.append(1)
    #converting gamma to int and epsilon to int
    a = [str(x) for x in gamma]
    b = [str(x) for x in epsilon]
    a = "".join(a)
    b = "".join(b)
    print(a)
    print(b)
    gg = int(a, 2)
    ee = int(b, 2)
    print("TOTAL", ee*gg)


