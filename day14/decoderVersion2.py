def permutations(dictionary, value, perma):
    #loop through perma until your get an x, then branch
    for i in range(len(perma)):
        if perma[i] == 'X':
            mk_zero = perma.copy()
            mk_one = perma.copy()
            mk_zero[i] = '0'
            mk_one[i] = '1'
            permutations(dictionary, value, mk_zero)
            permutations(dictionary, value, mk_one)
    the_addy = "".join(perma)
    if the_addy.isdigit() == False:
        return
    print(the_addy)
    dictionary[the_addy] = value

def mem_operation(bitmask, value, address, dictionary):
    loopMe = list(bin(int(address))[2:])
    bitArray = list(bitmask)[0:-1]
    #have to increase size of loopMe because I will get index later on if I don't
    for _ in range(36 - len(loopMe)):
        loopMe.insert(0, "0")
    #this first loop will get us our result with "x"s
    #here we modify our 36 bit version of our address, by using the bitmask
    # 0's will incur no change
    # 1's will overwrite the value to 1
    # X's will overwrite with X, and then remmeber to use for permutation
    for i in range(len(loopMe)):
        if bitArray[len(bitArray)-1 - i] == '1':
            loopMe[len(bitArray)-1 - i] = bitArray[len(bitArray) - 1 -i]
        elif bitArray[len(bitArray)-1 - i] == 'X':
            loopMe[len(bitArray)-1 - i] = bitArray[len(bitArray) - 1 -i]
    #here we work on the permutations
    #we look for "X"s and we throw it into the permutations function
    #this function will look for "X"s then create permutation addresses
    permutations(dictionary, value, loopMe)
    return

def add_up_the_array(thingy):
    sum = 0
    for i in thingy.values():
        sum += i
    return sum

with open('test.txt') as raw_intput:
    smart_dict = {}
    current_mask = 'Nothing'
    for i in raw_intput:
        splitted = i.split(' = ')
        value = splitted[1]
        #if its a mask then update to the current mask var
        if splitted[0] == 'mask':
            current_mask = splitted[1]
        #here we get the permutations of the memory val and then 
        #write the value to all the permutations
        else:
            address = int(splitted[0][4:-1])
            #allow past address to be overwritten
            #also we want to modify the smart_dict var so we can use it with the add_up function
            mem_operation(current_mask, value, address, smart_dict)
    print(smart_dict)