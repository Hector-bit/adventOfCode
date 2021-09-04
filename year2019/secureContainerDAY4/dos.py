#CRITERIA:
#   1) Can never decrease going from left to right
#   2) 2 adjacent numbers must have the same value
passes = 0
testing = []
def extraLarge(string):
    mylist = list(string)
    mydict = {}
    for i in mylist:
        if i in mydict.keys():
            mydict[i] += 1
        else:
            mydict[i] = 1
    for i in mydict.values():
        if i == 2:
            return True
    return False

def neverDecrease(string):
    mylist = list(string)
    if len(mylist) != 6:
        return False
    for i in range(len(mylist)-1):
        if mylist[i] > mylist[i+1]:
            return False
    return True

for i in range(165432, 707912):
    integer = str(i)
    testOne = extraLarge(integer)
    testTwo = neverDecrease(integer)
    if testOne and testTwo:
        passes += 1
        testing.append(integer)
print(testing)
print(passes)


