
accumalator = 0

identifyier = {}
memory = []

def add_to_dictionary(id, arr):
    global identifyier
    identifyier[id] = arr

def accum_before_repeat(my_dict, index):
    for i in range(index, len(my_dict) - 1):
        global memory
        global accumalator
        if index in memory:
            print("ACC", accumalator)
            print("repeat found")
            break
        memory.append(index)
        instruct = my_dict.get(index)[0]
        number_w_instruct = my_dict.get(index)[1]
        if instruct == 'acc':
            # print('IS THIS A NUMERB: ', int(number_w_instruct))
            accumalator += int(number_w_instruct)
        elif instruct == 'jmp':
            index += int(number_w_instruct)

            print("got hops boi: ", index, 'from ', int(number_w_instruct))
            accum_before_repeat(my_dict, index)
        index += 1

with open ("instructions.txt") as raw_input:
    countering = 0
    for i in raw_input:
        new_array = i.split()
        add_to_dictionary(countering, new_array)
        countering += 1

accum_before_repeat(identifyier, 0)
print(memory)
print(identifyier)