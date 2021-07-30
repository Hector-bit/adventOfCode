def mathStuff(str):
    # print('HERE: ', str)
    splitted = str.split(' ')
    print(splitted)
    for i in splitted:
        if i == '*'
num = 0

def recurse(str):
    #this takes a line of math the returns a number
    global num
    num = 0
    for index, i in enumerate(str):
        if i == '(':
            remaining = (str[index+1:])
            for ind, j in enumerate(remaining):
                if j == '(':
                    print('RECURSE')
                    recurse(remaining)
                elif j == ')':
                    #do some math for the line
                    #a number is returned
                    num += mathStuff(remaining[:ind])
                # else:
                #     splitted = remaining.split(' ')
                #     print(splitted)
    return num



with open('test.txt') as raw_input:
=======
def math(bound):
    print(bound, 'BOUNDS')
    #do the math, get a num, replace the big myStringing
    opAndnum = bound.split(" ")
    # print(opAndnum)
    while len(opAndnum) != 1:
        if opAndnum[1] == "+":
            sum = int(opAndnum[0]) + int(opAndnum[2])
            #then replace:
            temp = opAndnum[3:]
            temp.insert(0, str(sum))
            opAndnum = temp
        elif opAndnum[1] == "*":
            product = int(opAndnum[0]) * int(opAndnum[2])
            #then replace:
            temp = opAndnum[3:]
            temp.insert(0,str(product))
            opAndnum = temp
        # print('NEW', opAndnum)
    return opAndnum[0]



# def capture(arr, myString):
#     #we get a stack then take from top
#     #then return a myStringing of inputs
#     bound = None
#     # print(myString)
#     while len(myString) != 3:
#         rightP = myString.find(")")
#         for i in range(rightP, 0, -1):
#             leftP = myString[i] == "("
#             if leftP:
#                 num = math(myString[leftP:rightP])
#                 tempLeft = myString[:leftP]
#                 tempRight = myString[rightP:]
#                 temp = tempLeft + num + tempRight
#         while leftP != -1:
#             #search tighter
#             looky = myString[leftP + 1:]
#             temp = looky.find("(")
#             print('TMEP', temp)
#             if temp == -1:
#                 print('MATH TIME')
#                 break
#             else:
#                 leftP = temp
#                 print(leftP, 'NEW')
    # for i in reversed(arr):
    #     for y in range(int(i), len(myString)-1, 1):
    #         # print(y)
    #         if myString[y] == ")":
    #             bound = myString[int(i) + 1:y]
    #             # print(bound, "VOUBSDFASD")
    #             mathedUp = math(bound, myString)
    #             leftTemp = myString[:i]
    #             rightTemp = myString[y + 1:]
    #             temp = leftTemp + mathedUp + rightTemp
    #             print(temp)
    #             myString = temp


def lookFor(myString):
    #we get a stack then take from top
    #then return a myStringing of inputs
    # print(myString)
    while len(myString) != 1:
        rightP = myString.find(")")
        print('FIRST', rightP)
        if rightP != -1:
            for i in range(rightP, -1, -1):
                if myString[i] == '(':
                    num = math(myString[int(i) +1:int(rightP)])
                    print(num, 'MY NUM')
                    tempLeft = myString[:i]
                    tempRight = myString[rightP + 1:]
                    # print(tempLeft,'LOOKAOSKDFJALKSDJF', tempRight)
                    temp = tempLeft + num + tempRight
                    myString = temp
                    print('NEW STINR', myString)
                    break
        else:
            return math(myString)
        # while i != -1:
        #     #search tighter
        #     looky = myString[i + 1:]
        #     temp = looky.find("(")
        #     print('TMEP', temp)
        #     if temp == -1:
        #         print('MATH TIME')
        #         break
        #     else:
        #         i = temp
        #         print(i, 'NEW')



with open('data.txt') as raw_input:
>>>>>>> a8f31292118d78b07c8999f8bf804c0dcf73eb96
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