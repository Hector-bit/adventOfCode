def checkInside(elfone, elfTwo):
    if int(elfone[0]) >= int(elfTwo[0]):
        if int(elfone[1]) <= int(elfTwo[1]):
            return True
    return False

with open('input.txt') as raw_input:
    fully = 0
    for i in raw_input:
        i = i.strip('\n')
        splited = i.split(',')
        elfone = splited[0].split('-')
        elftwo = splited[1].split('-')
        if checkInside(elfone, elftwo):
            fully += 1
        elif checkInside(elftwo, elfone):
            fully += 1

    print('full overlaps:', fully)

