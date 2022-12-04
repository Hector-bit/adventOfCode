def checkOverlap(elfone, elftwo):
    for i in range(int(elfone[0]), int(elfone[1])+1):
        for j in range(int(elftwo[0]), int(elftwo[1])+1):
            if i == j:
                return True
    return False

with open('input.txt') as raw_input:
    fully = 0
    for i in raw_input:
        i = i.strip('\n')
        splited = i.split(',')
        elfone = splited[0].split('-')
        elftwo = splited[1].split('-')
        if checkOverlap(elfone, elftwo):
            fully += 1

    print('Overlaps:', fully)

