g = open('result.txt', 'w')
with open('data.txt') as raw_input:
    for i in raw_input:
        g.write("'")
        g.write(i)
        g.write("'")
        g.write(',')