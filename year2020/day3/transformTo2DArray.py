f = open("day3/data.txt", "r")

entries = f.read().split()

g = open("day3/dataToArrayl.txt", "w")

for i in entries:
    g.write("'")
    g.write(i)
    g.write("'")
    g.write(",")

g.close()

print(entries)
f.close()