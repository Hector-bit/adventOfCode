


def mem_operation(bitmask, value):
    loopMe = bin(int(value))[2:]
    print(loopMe, "<== before")
    bitArray = list(bitmask)
    for i in range(len(loopMe), -1, -1):
        if bitmask[i] == 'X':
            # bitArray = list(bitmask)
            # print(bitArray, "BRUH")
            bitArray[35 - i] = loopMe[len(loopMe) - 1]
    for i in range(len(bitArray)):
        if bitArray[i] == 'X':
            bitArray[i] = '0'
    bitmask = "".join(bitArray)
    # print(bitArray, "<== after!!!")
    return int(bitmask[1:-1], 2)

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
        splitted = i.split('=')
        if splitted[0] == "mask ":
            current_mask = splitted[1]
        else:
            #so here we get a change in the memory
            #so this piece of code needs to 
                #change the mem using the mask
                #and then add it back to the sum_of_arrays
                #but if its all ready there then it needs to be replaced
            temp = splitted[0].split('[')
            value = splitted[1]
            address = int(temp[1].replace("] ", ""))
            # print(mem_operation(current_mask, value))
            smart_dict[address] = mem_operation(current_mask, value)
    print(smart_dict)