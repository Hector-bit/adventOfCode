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
    add_up = []
    for i in raw_input:
        add_up.append(recurse(i))
        # print(recurse(i))
    # sum = 0
    # for j in add_up:
    #     sum += j
    # print("Sum: ", sum)