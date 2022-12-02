with open('data.txt') as raw_input:
    elfCalorieList = []
    elfChecker = 0
    for i in raw_input:
        if i != '\n':
            elfChecker += int(i)
        else:
            elfCalorieList.append(elfChecker)
            elfChecker = 0
    print(max(elfCalorieList))

        
    

