
def indirectOrbits(orbitee, dictionary):
    IOcount = 0
    DOcount = 0
    searching = orbitee
    IOgroup = []
    #look for whatever we are searching
    #this is round 1 so no need to count IO
    for searchee in dictionary.keys():
        if searchee == searching:
            #count as an indirect orbit and add it to IOgroup
            for i in dictionary[searchee]:
                IOgroup.append(i)
                DOcount += 1
    #round 2 are all IO orbits
    while len(IOgroup) > 0:
        print(IOgroup, 'should be new')
        newGroup = []
        for search in IOgroup:
            if search in dictionary.keys():
                for i in dictionary[search]:
                    IOcount += 1
                    newGroup.append(i)
        print(newGroup)
        IOgroup = newGroup
    return IOcount + DOcount

with open('data.txt') as rawinput:
    orbitList = {}
    for i in rawinput:
        splitted = i.split(')')
        if splitted[0] not in orbitList:   
            orbitList[splitted[0]] = [splitted[1][:-1]]
        else:
            orbitList[splitted[0]].append(splitted[1][:-1])
    orbitCount = 0
    for i in orbitList.keys():
        orbitCount += indirectOrbits(i, orbitList)
    print(orbitCount)