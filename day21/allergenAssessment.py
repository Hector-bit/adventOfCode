

mylist = []
mydict = {}
final = {}

with open('data.txt') as raw_input:
    for i in raw_input:
        # print(i)
        splitted = i.split("(")
        # print(splitted)
        # print(str(splitted[0]))
        language = splitted[0][:-1].split(" ")
        # print(language)
        # print(mylist)
        # if language not in mylist:
        mylist.append(language)
        allergens = splitted[1][:-2].replace("contains ", "").split(", ")
        print(allergens)
        # print(allergens)
        for j in allergens:
            if j not in mydict.keys():
                mydict[j] = language
            elif j in mydict.keys():
                #compare and remove non duplicates:
                temp = mydict[j]
                save = []
                for copy in temp:
                    if copy in language:
                        # print(language, 'then', copy)
                        save.append(copy)
                mydict[j] = save
    print(mydict)
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
            # there is more than one word
            for search in mydict[i]:
                # print('Searching: ', search, "In list: ", final)
                if search in final:
                    mydict[i].remove(str(search))
        # print(final,'final') 
        # print(mydict, 'result')
    notallergens = 0
    for counting in mylist:
        for oneMore in counting:
            print(oneMore)
            if oneMore not in final:
                notallergens +=1
    print(mylist)
    print(notallergens)

