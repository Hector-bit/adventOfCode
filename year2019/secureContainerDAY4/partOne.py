#CRITERIA:
#   1) Can never decrease going from left to right
#   2) 2 adjacent numbers must have the same value
passes = 0

def double(string):
    mylist = list(string)
    for i in range(len(mylist)-1):
        if mylist[i] == mylist[i+1]:
            return True
    return False

def neverDecrease(string):
    mylist = list(string)
    for i in range(len(mylist)-1):
        if mylist[i] > mylist[i+1]:
            return False
    return True
#165432-707912
for i in range(165432, 707912):
    integer = str(i)
    testOne = double(integer)
    testTwo = neverDecrease(integer)
    if testOne and testTwo:
        passes += 1
print(passes)


