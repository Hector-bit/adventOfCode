questions = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

with open("answers.txt") as raw_input:
    counter = 0
    split_1 = raw_input.read().split('\n\n')
    split_2 = [string.replace('\n', '') for string in split_1]
    for text in split_2:
        tracker = []
        for i in text:
            if i not in tracker:
                tracker.append(i)
        counter += len(tracker)
    print(counter)
    