print('START')

with open('input.txt') as raw_input:
    listOne = []
    listTwo = []
    for indexI, i in enumerate(raw_input):
        temp = i.split("\n")
        temp = temp[0].split("   ")
        listOne.append(int(temp[0]))
        listTwo.append(int(temp[1]))
    listOne.sort()
    listTwo.sort()
    sum = 0
    for index, num in enumerate(listOne):
        sum += (abs(num - listTwo[index]))
        # for indexJ, j in enumerate(i):
        #     if i == 1:
        #       print(indexI)
        #     if j == "#":
        #         mySet.add((indexJ, indexI, 0))
    # for i in range(6):
    #     state = stepSimulation(state)

    # print(listOne)
    print(sum)