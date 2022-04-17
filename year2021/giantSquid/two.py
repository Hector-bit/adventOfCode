
with open('data.txt') as raw_input:
    lines = raw_input.readlines()
    luckyNumbers = lines[0][:-1].split(",")
    bingoBoards = []
    #create bingo boards
    buildBoard = []
    lines.append('\n')
    for index, i in enumerate(lines[2:]):
        if i != '\n':
            temp = i[:-1].split(" ")
            for j in temp:
                if j.isdigit() == False:
                    temp.remove(j)
            buildBoard.append(temp)
        else:
            bingoBoards.append(buildBoard)
            buildBoard = []
    def checkHori(bingoCard):
        #checks horizontall for bingos
        for i in range(5):
            temptemp = 0
            for j in range(5):
                if bingoCard[i][j] == "X":
                    temptemp += 1
            if temptemp >= 5:
                print("BINGO CARD")
                print(bingoCard)
                return i
        return None
                
    def checkVert(bingoCard):
        #checks vertically for bingos
        for i in range(5):
            bingo = 0
            for j in range(5):
                if bingoCard[j][i] == "X":
                    bingo +=1
            if bingo >= 5:
                return i
        return None

    def checkCross(bingoCard):
        #checks diaganally for a bingo
        bingo = 0
        for i in range(5):
            if bingoCard[i][i] == "X":
                bingo +=1
            else:
                bingo = 0
            if bingo == 5:
                print("BINGO CARD")
                print(bingoCard)
                return bingoCard
        for i in range(5):
            if bingoCard[4-i][i] == "X":
                bingo +=1
            else:
                bingo = 0
            if bingo == 5:
                return bingoCard
        return None
    def getSumOfList(arr):
        sums = 0
        for i in arr:
            for j in i:
                if j != "X":
                    sums += int(j)
        print("SUM: ", str(sums)) 
        return sums
        

    #start playing bingo
    def playBingo(bbb, ln):
        print(ln)
        print(bbb)
        for i in ln:
            print("LATEST LUCKY NUMBER: ", i)
            for indexj, j in enumerate(bbb):
                for indexk, k in enumerate(j):
                    for indexo, o in enumerate(k):
                        if o == i:
                            bbb[indexj][indexk][indexo] = "X"
            #do checks for a winner after every number
            newBoards = []
            if len(bbb) == 1:
                hbingo = checkHori(bbb[0])
                vbingo = checkVert(bbb[0])
                if hbingo != None:
                    return getSumOfList(bbb[0]) * int(i)
                elif vbingo != None:
                    return getSumOfList(bbb[0]) * int(i)
            else:
                for boardIndex, p in enumerate(bbb):
                    hbingo = checkHori(p)
                    vbingo = checkVert(p)
                    #cbingo = checkCross(i)
                    if hbingo == None and vbingo == None:
                        newBoards.append(p)
                bbb = newBoards
        return "nothing..."

    final = playBingo(bingoBoards, luckyNumbers)
    
    print(final)

    

