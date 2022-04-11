
with open("test.txt") as raw_input:
    prev = None
    increases = 0
    windows = []
    #first loop will create the sum of 3 numbers to create a window
    a = None
    b = None
    for index, _ in enumerate(raw_input):
        c = int(_)
        print(c, " index: ", index)
        if (index % 3 == 0):
            a = 
        if (index % 3 == 1):
            b = int(c)
        if index >= 2:
            print("a: ", a, " b: ", b, " c: ", c)
            windows.append(a+b+c)
    print("windows", windows)
#copied over the part one code and subbed in the windows array
    for i in windows:
        curr = int(i)
        if prev is not None:
            if prev < curr:
                increases += 1
        prev = curr
    print("number of increases: " + str(increases))
        


