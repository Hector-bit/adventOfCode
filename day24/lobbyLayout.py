directions = ['e', 'se', 'sw', 'w', 'nw', 'ne']

with open('test.txt') as raw_input:
    for i in raw_input:
        meme = list(i)
        readstart = 0
        readend = 0
        # print(meme)
        for j in range(len(meme)):
            readend = j
            joined = ''.join(meme[readstart:readend])
            # print(joined)
            if joined in directions:
                readstart = readend
                print(joined)



