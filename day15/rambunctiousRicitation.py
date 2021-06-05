test = [0,3,6]

def rr(n, arr):
    turn = 0
    while turn != 2020:
        #create a new num from the previous input
        num = arr[-1]
        for i in range(len(test), -1, -1):
            if test[i] == num:
                arr.append(len(test) -1 -i)
        
        turn += 1
    return turn

print(rr(2020, test))