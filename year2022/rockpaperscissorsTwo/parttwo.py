with open('data.txt') as raw_input:
    #first we organise the games in arr like [[game1], [game2], ...]
    games = []
    for i in raw_input:
        cleaned = i.strip('\n')
        game = cleaned.split(' ')
        games.append(game)
    #from here on we focus on calculating points won according the the guide given to us by the elf
    elfSide = { "A": 1, "B": 2, "C": 3 }
    meSide = { "X" : 1, "Y": 2, "Z": 3 }
    win = {"A": "Y", "B": "Z", "C": "X"}
    lose = {"A": "Z", "B": "X", "C": "Y"}
    pointsEarned = 0
    for i in games:
        elf = i[0]
        me = i[1]
        if me == 'X': #lose
            pointsEarned += 0
            pointsEarned += meSide[lose[elf]]
        if me == 'Y': #draw
            pointsEarned += elfSide[elf]
            pointsEarned += 3
        if me == 'Z': #win
            pointsEarned += meSide[win[elf]]
            pointsEarned += 6
    print("Points Won:", pointsEarned)

