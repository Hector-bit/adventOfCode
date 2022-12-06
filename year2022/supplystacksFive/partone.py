
testBlocks = [
    ['Z','N'],
    ['M','C','D'],
    ['P']
]

realBlocks = [
    ['F','C','P','G','Q','R'],
    ['W','T','C','P'],
    ['B','H','P','M','C'],
    ['L','T','Q','S','M','P','R'],
    ['P','H','J','Z','V','G','N'],
    ['D','P','J'],
    ['L','G','P','Z','F','J','T','R'],
    ['N','L','H','C','F','P','T','J'],
    ['G','V','Z','Q','H','T','C','W']
]

def moveOne(start, destination, arrBlocks):
    moving = arrBlocks[start].pop(-1)
    arrBlocks[destination].append(moving)

with open('input.txt') as raw_input:
    blocks = realBlocks
    for line in raw_input:
        line = line.strip('\n')
        bigsplit = line.split(' ')
        amountToMove = int(bigsplit[1])
        movingFrom = int(bigsplit[3])-1
        movingTo = int(bigsplit[5])-1
        print('amount:',amountToMove, '| moving from:',movingFrom,'| moving to: ',movingTo)
        for i in range(amountToMove):
            moveOne(movingFrom, movingTo, blocks)
    print('FINAL:')
    tempstr = ''
    for i in blocks:
        tempstr += (i[-1])
    print(tempstr)

