from io import open_code


my_adapters = [84,60,10,23,126,2,128,63,59,69,127,73,140,55,154,133,36,139,4,70,110,97,153,105,41,106,79,145,35,134,146,148,13,77,49,107,46,138,88,152,83,120,52,114,159,158,53,76,16,28,89,25,42,66,119,3,17,67,94,99,7,56,85,122,18,20,43,160,54,113,29,130,19,135,30,80,116,91,161,115,141,102,37,157,129,34,147,142,151,68,78,24,90,121,123,33,98,1,40]
test_adapter = [28,
33,
18,
42,
31,
14,
46,
20,
48,
47,
24,
23,
49,
45,
19,
38,
39,
11,
1,
32,
25,
35,
8,
17,
7,
9,
4,
2,
34,
10,
3]
#we, start at zero jolts
#are adapters acccept jolts no lower than 3 jolts

#do not count the differences of two, just 1 ands threes

def oneVSthree(arr):
    my_max = max(arr) + 3
    print("my max: ", my_max)
    sortedArr = sorted(arr)
    print(sortedArr)
    jolts = 0
    ones = 0
    threes = 0
    for i in sortedArr:
        difference = abs(i - jolts)
        print("here are my jolts", jolts)
        if difference == 1:
            print("ones::: ", i)
            ones += 1
            jolts = i
        if difference == 3:
            print("threes== ", i)
            threes += 1
            jolts = i
    
    print("ones: ", ones, "threes: ", threes, " and then my jolts ", jolts)
    return ones * threes

def all_permutations(arr):
    my_max = max(arr) + 3
    sortArr = sorted(arr)
    jolts = 0
    group_of_ones = 0
    combos = {1:1,2:2,3:4,4:7}
    possible = 1
    for i in sortArr:
        difference = abs(i - jolts)
        if difference == 1 :
            group_of_ones += 1
            jolts = i
        if difference == 3:
            if group_of_ones in combos:
                possible = possible *  combos.get(group_of_ones)
                group_of_ones = 0
            jolts = i
    
    return possible * 7



print(all_permutations(my_adapters))




