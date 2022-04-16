
with open("data.txt") as raw_input:
    oxygenArray = []
    oxygenRating = None
    co2Array = []
    co2Rating = None

    #counts number of one's in each coloumn
    def getCountOnRow(twodarray, index):
        ones = 0
        zeros = 0
        for i in twodarray:
            if i[index] == "1":
                ones += 1
            elif i[index] == "0":
                zeros += 1
        if ones > zeros:
            return 1
        elif zeros > ones:
            return 0
        elif ones == zeros:
            return "same"

    def removewith(twodarray, index, num):
        returner = []
        for i in twodarray:
            if i[index] == str(num):
                returner.append(i)
        return returner
    
    def reduceArray(twodarray, bigorsmallvalue):
        if bigorsmallvalue == "big":
            for index, i in enumerate(twodarray):
                most = getCountOnRow(twodarray, index)
                if most == "same":
                    #do somthiing else
                    twodarray = removewith(twodarray, index, 1)
                else:
                    twodarray = removewith(twodarray, index, most)
                if len(twodarray) == 1:
                    return twodarray[0]
        elif bigorsmallvalue == "small":
            for index, i in enumerate(twodarray):
                most = getCountOnRow(twodarray, index)
                least = None
                if most == 1:
                    least = 0
                elif most == 0:
                    least = 1
                elif most == "same":
                    least = "same"
                if least == "same":
                    #do something else
                    twodarray = removewith(twodarray, index, 0)
                else:
                    twodarray = removewith(twodarray, index, least)
                if len(twodarray) == 1:
                    return twodarray[0]
    #fills oxygenarry and co2array with all values 
    for i in raw_input:
        oxygenArray.append(i[:-1])
        co2Array.append(i[:-1])
    #loop through and romove until there is only one value left
    oxygenRating = reduceArray(oxygenArray, "big")
    co2Rating = reduceArray(co2Array, "small")
    print('ORATING', oxygenRating)
    print('co2Rating', co2Rating)
    #converting gamma to int and epsilon to int
    a = [str(x) for x in oxygenRating]
    b = [str(x) for x in co2Rating]
    a = "".join(a)
    b = "".join(b)
    print(a)
    print(b)
    gg = int(a, 2)
    ee = int(b, 2)
    print("TOTAL", ee*gg)


