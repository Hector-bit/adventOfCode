#opcode 1 tells us to add the sum of 2 numbers then add it to position 3
#opcode 2 tells us to do the same things as opcode 1, except to multiply instead of add

data = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,6,23,27,1,27,5,31,2,9,31,35,1,5,35,39,2,6,39,43,2,6,43,47,1,5,47,51,2,9,51,55,1,5,55,59,1,10,59,63,1,63,6,67,1,9,67,71,1,71,6,75,1,75,13,79,2,79,13,83,2,9,83,87,1,87,5,91,1,9,91,95,2,10,95,99,1,5,99,103,1,103,9,107,1,13,107,111,2,111,10,115,1,115,5,119,2,13,119,123,1,9,123,127,1,5,127,131,2,131,6,135,1,135,5,139,1,139,6,143,1,143,6,147,1,2,147,151,1,151,5,0,99,2,14,0,0]

testCaseOne = [1,0,0,0,99]
testCaseTwo = [2,0,0,0,99]
#2,3,0,3,99 
testCaseThree = [2,3,0,3,99]
#2,4,4,5,99,0 
#becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
#1,1,1,4,99,5,6,0,99
#becomes 30,1,1,4,2,5,6,0,99.
testCase = [1,0,0,0,99]

def IntComputer(arr):
    print(arr)
    for i in arr:
        if i%4 == 0 or i == 0:
            zero = arr[i]
            first = arr[i+1]
            second = arr[i+2]
            third = arr[i+3]
            if zero == 1:
                sums = arr[first] + arr[second]
                print(sums, third, arr[third])
                arr[third] += sums - arr[third]
            elif zero == 2:
                product = arr[first] * arr[second]
                arr[third] += product - arr[third]
            elif zero == 99:
                break
    print(arr)
    print("position at one", arr[0])
IntComputer(testCaseTwo)
IntComputer(testCaseOne)
IntComputer(testCaseThree)
IntComputer(data)
