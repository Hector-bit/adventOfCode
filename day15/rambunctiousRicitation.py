 
test = [0,3]
data = [9,19,1,6,0,5]

def rr(n, arr):
    turn = len(arr)
    smart_dict = {}
    for index, i in enumerate(arr):
        smart_dict[i] = index
    #create a new num from the previous input
    num = 4
    while turn != n:
        #do a quick check to see if the nuber exists
        #within the array, if it does then add a zero to arr
        if num not in smart_dict.keys():
            smart_dict[num] = turn
            num = 0
        #if the number is in the dictionary then we need
        #to subtract the indexs of the most recent
        else:
            temp = num - 0
            num = turn - smart_dict[temp]
            smart_dict[temp] = turn
        turn += 1
    print(turn, num)

rr(30000000 - 1, data)







2hnqs   tyt