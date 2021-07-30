from os import terminal_size


def math(bound):
    # print(bound, 'BOUNDS')
    #do the math, get a num, replace the big myStringing
    opAndnum = bound.split(" ")
    addition = "+" in opAndnum
    mult = "*" in opAndnum
    # print(opAndnum, 'ALL STRINGS? OR NUMS?')
    while addition == True:
        for i in range(len(opAndnum) - 1):
            if opAndnum[i] == "+":
                sum = [str(int(opAndnum[i-1]) + int(opAndnum[i+1]))]
                #then replace:
                # temp = opAndnum[3:]
                # temp.insert(0, str(sum))
                # opAndnum = temp
                tempLeft = opAndnum[:i-1]
                tempRight = opAndnum[i+2:]
                temp1 = tempLeft + sum + tempRight
                # print(temp1, 'summmm', sum)
                opAndnum = temp1
                # print(opAndnum, 'add')
                break
        addition = "+" in opAndnum
        # print("new", addition)
    while mult == True:
        for j in range(len(opAndnum) - 1):
            if opAndnum[j] == "*":
                product = [str(int(opAndnum[j-1]) * int(opAndnum[j+1]))]
                #then replace:
                tempLeft = opAndnum[:j-1]
                tempRight = opAndnum[j+2:]
                temp2 = tempLeft + product + tempRight
                opAndnum = temp2
                # print(opAndnum, "mult")
                break
        mult = "*" in opAndnum
    # print('EVERYTHING', opAndnum)
    return opAndnum[0]

def lookFor(myString):
    #we get a stack then take from top
    #then return a myStringing of inputs
    # print(myString)
    while len(myString) != 1:
        rightP = myString.find(")")
        # print('FIRST', rightP)
        if rightP != -1:
            for i in range(rightP, -1, -1):
                if myString[i] == '(':
                    num = math(myString[int(i) +1:int(rightP)])
                    # print(num, 'MY NUM')
                    tempLeft = myString[:i]
                    tempRight = myString[rightP + 1:]
                    temp = tempLeft + str(num) + tempRight
                    myString = temp
                    # print('NEW STINR', myString)
                    break
        else:
            num = math(myString)
            #print(num, 'MY NUM')
            return num
            # print('NEW STINR', myString)



with open('data.txt') as raw_input:
    add_up = []
    for i in raw_input:
        add_up.append(lookFor(i))
    sum = 0
    print(add_up)
    for num in add_up:
        sum += int(num)
    print(sum)
    # sum = 0
    # for j in add_up:
    #     sum += j
    # print("Sum: ", sum)