import math

def extraFuel(number):
    residual = number
    total = 0
    while residual > 0:
        op = math.floor(residual / 3)
        number += op-2
        residual = op -2
        if residual < 0:
            break
        total += residual
    return total

with open("data.txt") as raw_input:
    sum = 0
    for i in raw_input:
        op = math.floor(int(i) / 3)
        done = op - 2
        other = extraFuel(done)
        sum += done
        sum += other
    print("SUM: ", sum)
