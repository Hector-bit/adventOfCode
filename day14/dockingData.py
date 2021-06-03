


def mem_operation(bitmask, value):
    loopMe = list(bin(int(value))[2:])
    print(loopMe, "<== before")
    bitArray = list(bitmask)[0:-1]
    # print(len(bitArray), "dick size")
    for i in range(len(loopMe) - 1, -1, -1):
        print(i)
        if bitArray[35 - i] == 'X':
            # bitArray = list(bitmask)
            print(bitArray, "BRUH")
            bitArray[35 - i] = loopMe[len(loopMe) - 1]
    # for i in range(len(bitArray)):
    #     # if bitArray[i] == 'X':
    #     temparr = list(bitmask)
    #     bitArray[i] = temparr[i]
    for i in range(len(bitArray)):
        if bitArray[i] == 'X':
            bitArray[i] = '0'
    bitArray = "".join(bitArray)
    print(bitArray, "<== after!!!", int(bitArray, 2))
    return int(bitArray, 2)

def add_up_the_array(arr):
    adder = 0
    for i in arr:
        adder += i
    return adder

with open('test.txt') as raw_intput:
    #this dictionary will hold the memory address as the key and 
    #the value will be integer value of the mem_operation we did on whatever bitmask we had
    smart_dict = {}
    # sum_of_arrays = []
    current_mask = 'Nothing'
    for i in raw_intput:
        # print(i.split('='))
        splitted = i.split(' = ')
        value = splitted[1]
        # print("triple check clean data", value)
        if splitted[0] == 'mask':
            current_mask = splitted[1]
        elif int(splitted[0][4:-1]) in smart_dict.keys():
            print('Mask', current_mask)
            address = int(splitted[0][4:-1])
            # print('it is in the motherfucking smart dictionary', address)
            smart_dict[address] = mem_operation(current_mask, smart_dict[address])
        else:
            print('amsk', current_mask)
            #so here we get a change in the memory
            #so this piece of code needs to 
                #change the mem using the mask
                #and then add it back to the sum_of_arrays
                #but if its all ready there then it needs to be replaced
            # print(mem_operation(current_mask, value))
            address = int(splitted[0][4:-1])
            smart_dict[address] = mem_operation(current_mask, value)
    print(smart_dict)