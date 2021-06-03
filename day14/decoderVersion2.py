


def mem_operation(bitmask, value):
    loopMe = list(bin(int(value))[2:])
    bitArray = list(bitmask)[0:-1]
    for i in range(len(loopMe)):
        if bitArray[len(bitArray)-1 - i] == 'X':
            bitArray[len(bitArray)-1 - i] = loopMe[len(loopMe) - 1 -i]
    for i in range(len(bitArray)):
        if bitArray[i] == 'X':
            bitArray[i] = '0'
    bitArray = "".join(bitArray)
    return int(bitArray, 2)

def add_up_the_array(thingy):
    sum = 0
    for i in thingy.values():
        sum += i
    return sum

with open('data.txt') as raw_intput:
    smart_dict = {}
    current_mask = 'Nothing'
    for i in raw_intput:
        splitted = i.split(' = ')
        value = splitted[1]
        if splitted[0] == 'mask':
            current_mask = splitted[1]
        elif int(splitted[0][4:-1]) in smart_dict.keys():
            address = int(splitted[0][4:-1])
            smart_dict[address] = mem_operation(current_mask, value)
        else:
            address = int(splitted[0][4:-1])
            smart_dict[address] = mem_operation(current_mask, value)
    print(add_up_the_array(smart_dict))