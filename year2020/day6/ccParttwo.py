questions = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

with open("answers.txt") as raw_input:
    counter = 0
    split_1 = raw_input.read().split('\n\n')
    split_2 = [string.replace('\n', ":") for string in split_1]
    split_3 = [string.split(":") for string in split_2]
    for group in split_3:
        my_dict = {}
        people_in_group = 0
        for string_g in group:
            # print(string_g)
            people_in_group += 1
            for letter in string_g:
                # print(letter)
                if letter not in my_dict:
                    # print(letter, 'first')
                    my_dict[letter] = 1
                elif letter in my_dict:
                    # print(letter, 'second')
                    my_dict[letter] = my_dict.get(letter) + 1
        print(my_dict.values(), people_in_group)
        for number in my_dict.values():
            print(number)
            if number == people_in_group:
                counter += 1

    print(counter)
    