r = open('day4/day4Data.txt', "r").read()

g = open('day4/DataMODPart2.txt', "w")

reqs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

input = r.splitlines()

# g.write("[")
info = ""
for i in input:
    if i == '':
        for j in info:
            print(j)
            j = str(j.split())
            # g.write("[")
            g.write(j)
            # g.write("]")
        g.write(" SPACE ")
        info = ""
    else:
        info.join(i)

g.close()
