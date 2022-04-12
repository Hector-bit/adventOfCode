
with open("data.txt") as raw_input:
    prev = None
    increases = 0
    windows = []
    #first loop will create the sum of 3 numbers to create a window
    a = 0
    b = 0
    for index, _ in enumerate(raw_input):
        c = int(_)
        if index >= 2:
            windows.append(a+b+c)
        a = b
        b = c
#copied over the part one code and subbed in the windows array
    for i in windows:
        curr = int(i)
        if prev is not None:
            if prev < curr:
                increases += 1
        prev = curr
    print("number of increases: " + str(increases))
        


