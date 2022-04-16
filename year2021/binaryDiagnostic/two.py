
with open("data.txt") as raw_input:
    rows = 0
    counterArr = []
    #create counter array to count # of one's in each coloumn
    for i in raw_input:
        for x in i:
            if x == '0' or x =='1':
                counterArr.append(0)
        break
    oxygenArray = []
    oxygenRating = None
    co2Array = []
    co2Rating = None

    #counts number of one's in each coloumn
    def getCountOnRow(twodarray, index):
        ones = 0
        zeros = 0
        for i in twodarray:
            if twodarray[index] == "1":
                ones += 1
            elif twodarray[index] == "0":
                zeros += 1
        if ones > zeros:
            return ones
        elif zeros > ones:
            return zeros
        elif ones == zeros:
            return "same"

    def removewith(twodarray, index, num):
        returner = []
        for i in twodarray:
            for j in i:
                if i[index] != num:
                    returner.append(i)
        return returner
    #put the raw_inputs into the oxygen and co3 arrays
    
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
        if bigorsmallvalue == "small":
            for index, i in enumerate(twodarray):
                least = getCountOnRow(twodarray, index)
                if least == "same":
                    #do something else
                    twodarray = removewith(twodarray, index, 0)
                else:
                    twodarray = removewith(twodarray, index, least)
                if len(twodarray) == 1:
                    return twodarray[0]

    for i in raw_input:
        oxygenArray.append(i)
        co2Array.append(i)
    #loop through and romove until there is only one value left
            
    oxygenRating = reduceArray(oxygenArray, "big")
    co2Rating = reduceArray(co2Rating, "small")
    print('ORATING', oxygenRating)
    print('co2Rating', co2Rating)
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


