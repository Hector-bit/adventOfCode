def minAndMax(arr):
    smallest = arr[0]
    biggest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
        if i > biggest:
            biggest = i
    return [smallest, biggest]

memor = {}

def sumOfSum(nump):
    fuelCost = None
    if nump in memor.keys():
        fuelCost = memor[nump]
    else:
        total = 0
        for i in range(1, nump+1):
            total += i
        fuelCost = total
        memor[nump] = total

    return fuelCost


with open("data.txt") as raw_input:
    crabs = raw_input.readline().strip("\n").split(",")
    crabs = [int(x) for x in crabs if x.isdigit()]
    myRange = minAndMax(crabs)
    print(myRange)
    cheapest = []
    for i in range(myRange[0], myRange[1]):
        accCost = []
        for j in crabs:
            steps = (abs(i-j))
            accCost.append(sumOfSum(steps))
        totalCost = sum(accCost)
        cheapest.append(totalCost)
    print(min(cheapest))




