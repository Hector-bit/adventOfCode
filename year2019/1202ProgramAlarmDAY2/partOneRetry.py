
testCase = [1,0,0,0,99]

def IntComputer(arr):
    print(arr)
    for i in arr:
        if i%4 == 0 or i == 0:
            first = arr[i+1]
            second = arr[i+2]
            third = arr[i+3]
            if arr[i] == 1:
                sums = arr[first] + arr[second]
                print(sums, third, arr[third])
                arr[third] += sums - arr[third]
            elif arr[i] == 2:
                product = arr[first] * arr[second]
                arr[third] += product - arr[third]
            elif arr[i] == 99:
                break
    print(arr)
    print("position at one", arr[0])
IntComputer(testCase)
