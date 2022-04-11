

with open ("data.txt") as raw_input:
    prev = None
    increases = 0
    for i in raw_input:
        curr = int(i)
        if prev is not None:
            if prev < curr:
                increases += 1
        prev = curr
    print("number of increases: " + str(increases))
