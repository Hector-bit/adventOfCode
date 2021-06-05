test = [0,3,6]

def rr(n, arr):
    turn = 0
    while turn != n:
        #create a new num from the previous input
        num = arr[-1]
        # print(turn, num)
        #do a quick check to see if the nuber exists
        #within the array, if it does then add a zero to arr
        if num not in arr[:-1]:
            # print(num, 'not found so zero')
            arr.append(0)
        #here we loop backwards
        else:
            # print('In arr is', num, arr)
            for i in range(len(arr) - 2, -1, -1):
                if arr[i] == num:
                    arr.append( - 1 -i)
        turn += 1
    print(arr)
    return arr[-1]

print(rr(10, test))