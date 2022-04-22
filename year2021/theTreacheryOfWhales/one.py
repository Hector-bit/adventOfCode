def minAndMax(arr):
    smallest = arr[0]
    biggest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
        if i > biggest:
            biggest = i
    return [smallest, biggest]


with open("data.txt") as raw_input:
    crabs = raw_input.readline().strip("\n").split(",")
    crabs = [int(x) for x in crabs if x.isdigit()]
    myRange = minAndMax(crabs)
    print(myRange)
    cheapest = []
    for i in range(myRange[0], myRange[1]):
        accCost = []
        for j in crabs:
            accCost.append(abs(i-j))
        totalCost = sum(accCost)
        cheapest.append(totalCost)
    print(min(cheapest))




