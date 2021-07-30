

playerOne = []
playerTwo = []

mylist = []

with open('data.txt') as raw_input:
    for i in raw_input:
        if i[:-1].isdigit():
            mylist.append(i[:-1])
    playerOne = mylist[:len(mylist)>>1]
    playerTwo = mylist[len(mylist)>>1:]
    # print(playerOne)
    # print(playerTwo)
    #now you may play until a player has lost all their cards
    round = 1
    while len(playerTwo) > 0 or len(playerOne) > 0:
        if len(playerTwo) == 0 or len(playerOne) == 0:
            break
        # print("====", round, "====")
        # print("PLAYER ONE: ",playerOne, len(playerOne))
        # print("PLAYER TWO: ",playerTwo, len(playerTwo))
        po = int(playerOne[0])
        playerOne.pop(0)
        pt = int(playerTwo[0])
        playerTwo.pop(0)
        if po > pt:
            playerOne.append(po)
            playerOne.append(pt)
            # playerTwo.pop(0)
            # playerOne.pop(0)
        elif pt > po:
            playerTwo.append(pt)
            playerTwo.append(po)
            # playerOne.pop(0)
            # playerTwo.pop(0)
        # elif po > pt and len(playerTwo) == 1:
        #     playerOne.append(po)
        #     playerOne.append(pt)
        #     playerTwo.pop(0)
        #     playerOne.pop(0)
        #     # break
        # elif pt > po and len(playerOne) == 1:
        #     playerTwo.append(pt)
        #     playerTwo.append(po)
        #     playerOne.pop(0)
        #     playerTwo.pop(0)
        #     # break
        round += 1
    print("====FINAL====")
    print(playerOne)
    print(playerTwo)
    sum = len(playerTwo)
    total = 0
    sum2 = len(playerOne)
    total2 = 0
    for index, i in enumerate(playerTwo):
        total += (sum - index) * i
    for indext, it in enumerate(playerOne):
        total2 += (sum2 - indext) * it
    print(total)
    print(total2)