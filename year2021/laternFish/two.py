initialState = [3,4,3,1,2]
data = [1,1,3,1,3,2,1,3,1,1,3,1,1,2,1,3,1,1,3,5,1,1,1,3,1,2,1,1,1,1,4,4,1,2,1,2,1,1,1,5,3,2,1,5,2,5,3,3,2,2,5,4,1,1,4,4,1,1,1,1,1,1,5,1,2,4,3,2,2,2,2,1,4,1,1,5,1,3,4,4,1,1,3,3,5,5,3,1,3,3,3,1,4,2,2,1,3,4,1,4,3,3,2,3,1,1,1,5,3,1,4,2,2,3,1,3,1,2,3,3,1,4,2,2,4,1,3,1,1,1,1,1,2,1,3,3,1,2,1,1,3,4,1,1,1,1,5,1,1,5,1,1,1,4,1,5,3,1,1,3,2,1,1,3,1,1,1,5,4,3,3,5,1,3,4,3,3,1,4,4,1,2,1,1,2,1,1,1,2,1,1,1,1,1,5,1,1,2,1,5,2,1,1,2,3,2,3,1,3,1,1,1,5,1,1,2,1,1,1,1,3,4,5,3,1,4,1,1,4,1,4,1,1,1,4,5,1,1,1,4,1,3,2,2,1,1,2,3,1,4,3,5,1,5,1,1,4,5,5,1,1,3,3,1,1,1,1,5,5,3,3,2,4,1,1,1,1,1,5,1,1,2,5,5,4,2,4,4,1,1,3,3,1,5,1,1,1,1,1,1]

def cycle(myarr, days):
    print("days: " + str(days))
    for i in range(days):
        newState = [0,0,0,0,0,0,0,0,0]
        addFish = myarr[0]
        newState[0] = 0
        for i in range(1,9):
            newState[i-1] += myarr[i]
        newState[8] += addFish
        newState[6] += addFish
        myarr = newState
    total = 0
    for j in myarr:
        total += j
    print(myarr)
    return total

def cleanUp(arr):
    cleaned = [0,0,0,0,0,0,0,0,0]
    for i in arr:
        cleaned[i] +=1
    return cleaned

cleanData = cleanUp(data)
print(cleanData)

totalFishies = cycle(cleanData, 256)
print("part 2 donezo: ", totalFishies)


