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
    pointsEarned = 0
    pointsFromPick = 0
    for i in games:
        elf = i[0]
        me = i[1]
        pointsFromPick += meSide[me]
        if me == 'X': #rock
            if elf == 'A': #rock
                pointsEarned += 3
            if elf == 'C': #scissors
                pointsEarned += 6
        if me == 'Y': #paper
            if elf == 'B': #paper
                pointsEarned += 3
            if elf == 'A': #rock
                pointsEarned += 6
        if me == 'Z': #scissors
            if elf == 'C': #scissors
                pointsEarned += 3
            if elf == 'B': #paper
                pointsEarned += 6
    print('points earned:', pointsEarned)
    print('points from pick:', pointsFromPick)
    print("Points Won:", pointsEarned+pointsFromPick)

