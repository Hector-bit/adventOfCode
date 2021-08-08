import math
with open("data.txt") as raw_input:
    sum = 0
    for i in raw_input:
        op = math.floor(int(i) / 3)
        sum += op-2
    print("Here you go:", sum)
