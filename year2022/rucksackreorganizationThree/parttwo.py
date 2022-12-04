from string import ascii_letters

with open('input.txt') as raw_input:
    letters = []
    team_sacks = []
    for index, line in enumerate(raw_input):
        line = line.strip('\n')
        team_sacks.append(line)
        if (index+1) % 3 == 0:
            group = team_sacks[-3:]
            group.sort(key=len)
            for uno in group[0]:
                if uno in group[1]:
                    if uno in group[2]:
                        letters.append(uno)
                        break
    letterSum =[(ascii_letters.index(letter) + 1) for letter in letters]
    total = 0
    for i in letterSum:
        total += i
    print('Sum Total:',total)
