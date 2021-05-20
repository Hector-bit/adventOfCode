
import re


my_set = set()
my_counter = 0
main_bag_dictionary = {}
bag_dictionary = {}

def add_to_dict(id, soa, first_dict, second_dict):
    iskey = soa[0]
    iskey = iskey.replace(' bags ', '')
    isvalue = soa[1:]
    first_dict[iskey] = id
    second_dict[id] = isvalue

def possibleCombos(first_dict, second_dict, color):
    for i in range(len(main_bag_dictionary)):
        bags_in_bag = second_dict[i]
        for j in bags_in_bag:
            if color in j:
                possibleCombos(first_dict, second_dict, get_new_color(i))

def get_new_color(key_id):
    key_list = list(main_bag_dictionary.values())
    new_color = key_list[key_id]

    global my_set
    if new_color not in my_set:
        my_set.add(new_color)
        global my_counter
        my_counter += 1
    return new_color

###################################
            #Part Two
###################################

def how_many_bags(color):
    # print(color)
    # print(main_bag_dictionary[color], '-------------------')
    thisThing = bag_dictionary[main_bag_dictionary[color]]
    # print(thisThing)
    for i in thisThing:
        if i != ' no other bags.':
            number = int(i.split()[0])
            new_color = i.split()[1] + " " + i.split()[2]
            for i in range(number):
                global my_counter
                my_counter += 1
                how_many_bags(new_color)



with open('rules.txt') as raw_input:
    split_1 = raw_input.read().split('\n')
    id = 0
    for ss in split_1:
        split_2 = re.split('contain|,', ss)
        add_to_dict(id, split_2, main_bag_dictionary, bag_dictionary)
        id += 1

how_many_bags("shiny gold")

print(my_set)
print('SET: ', len(my_set))
print('COUNTER: ',  my_counter)