

mylist = []
mydict = {}
final = {}

partTwo = []
twoDict = {}

with open('data.txt') as raw_input:
    for i in raw_input:
        splitted = i.split("(")
        language = splitted[0][:-1].split(" ")
        mylist.append(language)
        allergens = splitted[1][:-2].replace("contains ", "").split(", ")
        for j in allergens:
            if j not in mydict.keys():
                mydict[j] = language
            elif j in mydict.keys():
                #compare and remove non duplicates:
                temp = mydict[j]
                save = []
                for copy in temp:
                    if copy in language:
                        save.append(copy)
                mydict[j] = save

    while len(mydict) > 0:
        #loops through keys of mydict
        for i in mydict.keys():
            #if i has only one word then add it to final
            if len(mydict[i]) == 1:
                final[mydict[i][0]] = i
                #also delete allergen from mydict
                del mydict[i]

                break
            #else go throught the possible matches and look for repeats in final
            #there is more than one word
            for search in mydict[i]:
                if search in final:
                    mydict[i].remove(str(search))

    notallergens = 0
    for counting in mylist:
        for oneMore in counting:
            if oneMore not in final:
                notallergens +=1
    
    for reverse in final.keys():
        twoDict[final[reverse]] = reverse
    
    for en in twoDict.keys():
        partTwo.append(en)
    partTwo.sort()
    for index, k in enumerate(partTwo):
        partTwo[index] = twoDict[k]

    print("Part One", notallergens)
    print("Part Two", ','.join(partTwo))


