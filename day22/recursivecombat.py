

playerOne = []
playerTwo = []

mylist = []

def historyFunction(history, playerUno, playerDos):
    if str(playerUno + playerDos) in history:
        return True
    return False

def DEEPER(playerUno, playerDos, history):
    #i only wanna recurse if a new game starts
    #otherwise play normally
    while len(playerUno) > 0 and len(playerDos) > 0:
        # print("---------------")
        # print(playerUno)
        # print(playerDos)
        # print("---------------")
        inThePast = historyFunction(history, playerUno, playerDos)
        if inThePast:
            # print('HISTORy')
            #give win to playerUno
            playerUno.append(playerUno[0])
            playerUno.append(playerDos[0])
            playerUno.pop(0)
            playerDos.pop(0)
            return "UNO"
        else:
            history.append(str(playerUno + playerDos))
        po = playerUno[0]
        playerUno.pop(0)
        pt = playerDos[0]
        playerDos.pop(0)
        if po <= len(playerUno) and pt <= len(playerDos):
            print("NEW GAME")
            truthMe = DEEPER(playerUno[:po], playerDos[:pt], history)
            # print(truthMe, "<=======================")
            if truthMe == "UNO":
                playerUno.append(po)
                playerUno.append(pt)
            elif truthMe == "DOS":
                playerDos.append(pt)
                playerDos.append(po)
        elif po > pt:
            # print('player uno')
            playerUno.append(po)
            playerUno.append(pt)
            # playerDos.pop(0)
            # playerUno.pop(0)
        elif pt > po:
            # print("player dos")
            playerDos.append(pt)
            playerDos.append(po)
    print('                                 ', playerUno, playerDos)
    if len(playerUno) == 0:
        return "DOS"
    if len(playerDos) == 0:
        return "UNO"

def recursion(playerUno, playerDos, history):
    #i only wanna recurse if a new game starts
    #otherwise play normally
    while len(playerUno) > 0 and len(playerDos) > 0:
        print("---------------")
        print(playerUno)
        print(playerDos)
        print("---------------")
        # print(history)
        inThePast = historyFunction(history, playerUno, playerDos)
        if inThePast:
            # print('HISTORy not deeper')
            #give win to playerUno
            playerUno.append(playerUno[0])
            playerUno.append(playerDos[0])
            playerUno.pop(0)
            playerDos.pop(0)
            break
        else:
            history.append(str(playerUno + playerDos))
        po = playerUno[0]
        playerUno.pop(0)
        pt = playerDos[0]
        playerDos.pop(0)
        if po <= len(playerUno) and pt <= len(playerDos):
            print("NEW GAME")
            truthMe = DEEPER(playerUno[:po], playerDos[:pt], history)
            # print(truthMe, "<=======================")
            if truthMe == "DOS":
                playerUno.append(po)
                playerUno.append(pt)
            elif truthMe == "UNO":
                playerDos.append(pt)
                playerDos.append(po)
        elif po > pt:
            # print('player uno')
            playerUno.append(po)
            playerUno.append(pt)
            # playerDos.pop(0)
            # playerUno.pop(0)
        elif pt > po:
            # print("player dos")
            playerDos.append(pt)
            playerDos.append(po)
    return playerUno, playerDos

with open('test.txt') as raw_input:
    for i in raw_input:
        if i[:-1].isdigit():
            mylist.append(int(i[:-1]))
    playerOne = mylist[:len(mylist)>>1]
    playerTwo = mylist[len(mylist)>>1:]
    # print(playerOne)
    # print(playerTwo)
    #now you may play until a player has lost all their cards
    history = []
    while len(playerOne) > 0 and len(playerTwo) > 0:
        playerOne, playerTwo = recursion(playerOne, playerTwo, history)
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