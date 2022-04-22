value = 1
subject = 1004920
card = 5764801
door = 17807724

one = 10441485
two = 1004920
for i in range(2, 8):
    print(i)
    value = 1
    counter = 0
    while value <= door*9:
        print(value)
        value = value * i
        value = value % 20201227
        counter += 1
        if value == door:
            print("door loops", counter)
            break
        else:
            continue
        break


print("final:", value)


