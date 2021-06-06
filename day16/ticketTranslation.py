# departure location: 48-885 or 906-949
# departure station: 28-420 or 431-970
# departure platform: 45-112 or 129-967
# departure track: 41-447 or 459-956
# departure date: 36-913 or 934-962
# departure time: 34-792 or 815-952
# arrival location: 35-644 or 657-973
# arrival station: 45-550 or 563-970
# arrival platform: 41-533 or 539-973
# arrival track: 33-729 or 745-967
# class: 36-516 or 523-956
# duration: 37-94 or 108-960
# price: 35-669 or 678-974
# route: 37-834 or 847-968
# row: 35-295 or 312-956
# seat: 35-563 or 588-951
# train: 29-210 or 221-968
# type: 50-853 or 877-958
# wagon: 28-341 or 353-971
# zone: 43-413 or 421-962

# your ticket:
# 163,151,149,67,71,79,109,61,83,137,89,59,53,179,73,157,139,173,131,167
def arr_maker(str):
    smart_arr = []
    with open(str) as raw_input:
        for i in raw_input:
            two = i.split('-')
            start = int(two[0])
            end = int(two[1])
            for num in range(start, end):
                smart_arr.append(num)
    return smart_arr

def invalidRate():
    #create a dictionary full of valid numbers
    print('nothing')

with open("data.txt") as raw_input:
    valid_times = arr_maker("vaildTimes.txt")
    sum_of_invalids = 0
    for i in raw_input:
        new_arr = i.split(",")
        for j in new_arr:
            if int(j) not in valid_times:
                sum_of_invalids += int(j)
    print(sum_of_invalids)