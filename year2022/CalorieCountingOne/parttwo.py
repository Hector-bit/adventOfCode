with open('data.txt') as raw_input:
    elfCalorieList = []
    elfChecker = 0
    for i in raw_input:
        if i != '\n':
            elfChecker += int(i)
        else:
            elfCalorieList.append(elfChecker)
            elfChecker = 0
    elfOne = 0
    elfTwo = 0
    elfThree = 0
    for i in elfCalorieList:
        if i > elfOne:
            elfThree = elfTwo
            elfTwo = elfOne
            elfOne = i
        elif i > elfTwo:
            elfThree = elfTwo
            elfTwo = i
        elif i > elfThree:
            elfThree = i
    print(elfOne, ' ', elfTwo, ' ', elfThree)
    print(elfOne + elfTwo + elfThree)


