

playerOne = []
playerTwo = []

mylist = []

with open('test.txt') as raw_input:
    for i in raw_input:
        if i[:-1].isdigit():
            mylist.append(i[:-1])
    playerOne = mylist[:len(mylist)>>1]
    playerTwo = mylist[len(mylist)>>1:]
    print(playerOne)
    print(playerTwo)
    #now you may play until a player has lost all their cards
    while len(playerTwo) <= 0 or len(playerOne) <= 0:
        po = playerOne[0]
        pt = playerTwo[0]
        if po > pt:
            playerOne.append(po)
            playerOne.append(pt)
            playerOne.pop(0)
        elif pt > po:
            playerTwo.append(pt)
            playerTwo.append(po)
            playerTwo.pop(0)