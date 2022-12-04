from string import ascii_letters

with open('input.txt') as raw_input:
    letters = []
    for line in raw_input:
        line = line.strip('\n')
        strLen = int(len(line)/2)
        compA = line[0:strLen]
        compB = line[strLen:]
        for letter in compA:
            if letter in compB:
                letters.append(letter)
                break


    letterSum =[(ascii_letters.index(letter) + 1) for letter in letters]
    total = 0
    for i in letterSum:
        total += i
    print('Sum Total:',total)


