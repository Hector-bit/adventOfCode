
test = [3,8,9,1,2,5,4,6,7]
data = [7,1,2,6,4,3,5,8,9]
    #Rules
        #1) the crab picks up the three cups that are after the current cup
        #2) selecting a destingation cup: the cup with a label equal to currentCup - 1
            #if one is not found then subtract 1 until it hits 0, then find largest label available
        #3) the crab places the cups it picked up down after the destination cup has been chosen,
            # they keep the same order
        #4) the crab selcts a new current cup, which is whatever comes after 1 spot going clockwise
def crabDancerPartOne(arr, x):
    currentCup = 0
    for i in range(x):
        following = [arr[currentCup+i] for i in range(1,4)]
        target = arr[currentCup] - 1
        result = arr[4:]
        destinationCup = None
        # print(following, target, result)
        while destinationCup is None:
            if target == 0:
                destinationCup = max(result)
            for i in result:
                if i == target:
                    destinationCup = i
            target -=1
        print(destinationCup)
        for index, j in enumerate(result):
            if j == destinationCup:
                newArr = result[:index+1] + following + result[index+1:]
                newArr.append(arr[currentCup])
                # print(newArr)
        arr = newArr
        currentCup 
    print("CHECKPOINT")
    for inde, i in enumerate(arr):
        if i == 1:
            return arr[inde+1], arr[inde+2]

newArray = test + [i for i in range(10, 1000001)]
# print(newArray)

crabDancerPartOne(newArray, 10000000)
