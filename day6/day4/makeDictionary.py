r = open('day4/day4Data.txt', "r").read()

g = open('day4/DataMOD.txt', "w")

reqs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

input = r

g.write("[[")

for i in input:
    # for j in i:
    # if j:
    g.write("'")
    g.write(i)
    g.write("'")
    g.write(",")
    # if i == "":
    g.write("]")
    g.write(",")
    g.write("[")
    break

g.write("]]")

g.close()