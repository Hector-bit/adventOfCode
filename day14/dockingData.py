


def mem_operation(bitmask, memory):
    print(bitmask, memory)
    loopMe = bin(int(memory))[2:]
    print(loopMe, "<== here")
    for i in range(len(loopMe), -1, -1):
        if bitmask[i] == 'X':
            bitArray = list(bitmask)
            print(bitArray, "<== should be an array")
            bitArray[35 - i] = loopMe[len(loopMe) - 1]
            bitmask = "".join(bitArray)
    return bitmask

def add_up_the_array(arr):
    adder = 0
    for i in arr:
        adder += i
    return adder

with open('test.txt') as raw_intput:
    smart_dict = {}
    sum_of_arrays = []
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
            myElse = splitted[0].split('[')
            memory = int(myElse[1].replace("] ", ""))
            print(memory, type(memory))
            print(mem_operation(current_mask[1: -1], splitted[1]))
    print(sum_of_arrays)