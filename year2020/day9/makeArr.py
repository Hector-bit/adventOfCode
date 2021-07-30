r = open('encode.txt', 'r')

g = open('test.txt', 'w')

g.write('[')

for i in range(999):
    thisThing = r.readline()
    g.write(thisThing)
    g.write(',')

g.write(']')