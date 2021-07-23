import fileinput
import re
import sys

start = '389125467'
# start = '712643589'

def solve(is_p2):
    # for part 1 n = 9, part 2 n = 1million
    n = len(start) if (not is_p2) else int(1e6)
    # makes a list of 1 through n
    N = [None for i in range(n+1)]
    # x is a list of your given circle labels 7 1 2 6 4 3 5 8 9 
    X = [int(x) for x in start]
    # print(N, " BEFORE")
    # here we loop through len(X)
    for i in range(len(X)):
        #N[at index value of X]
        N[X[i]] = X[(i+1)%len(X)]   
    #PART TWO ONLY
    # print(N, " AFTER")
    if is_p2:
        #
        N[X[-1]] = len(X)+1
        for i in range(len(X)+1, n+1):
            N[i] = i+1
        N[-1] = X[0]

    #Part one sets up N in a weird way idk why
    #X is set up as the data

    t = 0 
    #on first round is three
    current = X[0]
    nmoves = int(1e7) if is_p2 else 100
    for _ in range(nmoves):
        t += 1
        #pickup will be eight
        pickup = N[current]
        #wtf is this shit
        #N[3] is now = One
        N[current] = N[N[N[pickup]]]
        #destination = 9 
        dest = n if current==1 else current-1
        while dest in [pickup, N[pickup], N[N[pickup]]]:
            dest = n if dest==1 else dest-1

        N[N[N[pickup]]] = N[dest]
        N[dest] = pickup
        current = N[current]

    if is_p2:
        return N[1]*N[N[1]]
    else:
        ans = []
        x = N[1]
        while x != 1:
            ans.append(x)
            x = N[x]
        return ''.join([str(x) for x in ans])
print(solve(False))
# print(solve(True))