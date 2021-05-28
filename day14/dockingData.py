

def mask_operation(mask):
    print('nothing')

def mem_operation(memory):
    print('nothing')

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
            print("new mask ==>", current_mask)
        else:
            #so here we get a change in the memory
            #so this piece of code needs to 
                #change the mem using the mask
                #and then add it back to the sum_of_arrays
                #but if its all ready there then it needs to be replaced
            print(splitted[0].split('['))
    print(sum_of_arrays)