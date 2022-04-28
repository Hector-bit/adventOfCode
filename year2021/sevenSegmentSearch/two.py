
with open("data.txt") as raw_input:
    numbercombos = {}
    total = []
    def decodeInput(inin):
        display = [0,0,0,0,0,0,0]
        #first pass to get easy numbers figured out
        #pd = {"tt":"", "tl":"", "tr":"","mm":"","bl":"","br":"","bb":""}
        solvedDict = {}
        fives = []
        sixes = []
        one = None
        four = None
        seven = None
        eight = None
        six = None
        for i in inin:
            if len(i) == 2:
                solvedDict[i] = '1'
                one = i
            if len(i) == 4:
                solvedDict[i] = '4'
                four = i
            if len(i) == 3:
                solvedDict[i] = '7'
                seven = i
            if len(i) == 7:
                solvedDict[i] = '8'
                eight = i
            if len(i) == 5:
                fives.append(i)
            if len(i) == 6:
                sixes.append(i)
        for i in sixes:
            for j in one:
                if j not in i:
                    solvedDict[i] = '6'
                    six = i
                    sixes.remove(i)
        for i in sixes:
            for j in four:
                if j not in i:
                    solvedDict[i] = '0'
                    sixes.remove(i)
                    solvedDict[sixes[0]] = '9'
        for i in fives:
            offBy = 0
            for j in one:
                if j not in i:
                    offBy +=1
            if offBy == 0:
                solvedDict[i] = '3'
                fives.remove(i)
                break

        for i in fives:
            offBy = 0
            for j in six:
                if j not in i:
                    offBy += 1
            if offBy == 1:
                solvedDict[i] = '5'
                fives.remove(i)
                solvedDict[fives[0]] = '2'
        return solvedDict

    def matchLetters(strOne, strTwo):
        ssOne = sorted(strOne)
        ssTwo = sorted(strTwo)
        if ssOne == ssTwo:
            return True
        return False
    for i in raw_input:
        splitted = i.split(" | ")
        inin = splitted[0].split(" ")
        output = splitted[1][:-1].split(" ")
        builder = ''
        numberDict = decodeInput(inin)
        for i in output:
            for j in numberDict.keys():
                if matchLetters(i, j):
                    builder += numberDict[j]
        print(builder)
        total.append(int(builder))
    print(sum(total))


