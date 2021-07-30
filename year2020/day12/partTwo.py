quadrant = 0

def which_quadrantXL(quad, x, deg):
    new_quad = (360 + (quad - deg)) % 360
    print(new_quad)
    if new_quad == 0:
        return abs(x)
    elif new_quad == 90:
        return abs(x)
    elif new_quad == 180:
        return abs(x) * -1
    elif new_quad == 270:
        return abs(x) * -1

def which_quadrantXR(quad, x, deg):
    new_quad = (360 + (quad + deg)) % 360
    print(new_quad)
    if new_quad == 0:
        return abs(x)
    elif new_quad == 90:
        return abs(x)
    elif new_quad == 180:
        return abs(x) * -1
    elif new_quad == 270:
        return abs(x) * -1

def which_quadrantYL(quad, y, deg):
    new_quad = (360 + (quad - deg)) % 360
    if new_quad == 0:
        return abs(y)
    elif new_quad == 90:
        return abs(y) * -1
    elif new_quad == 180:
        return abs(y) * -1
    elif new_quad == 270:
        return abs(y)

def which_quadrantYR(quad, y, deg):
    new_quad = (360 + (quad + deg)) % 360
    if new_quad == 0:
        return abs(y)
    elif new_quad == 90:
        return abs(y) * -1
    elif new_quad == 180:
        return abs(y) * -1
    elif new_quad == 270:
        return abs(y)

def rotate_around_the_boat(ist, amt, old_waypoint):
    if ist == 'L':
        for _ in range(int(amt/90)):
            old_waypoint[0], old_waypoint[1] = -old_waypoint[1], old_waypoint[0]
            # old_waypoint[1] = old_waypoint[0]
    elif ist == 'R':
        for _ in range(int(amt/90)):
            old_waypoint[0], old_waypoint[1] = old_waypoint[1], -old_waypoint[0]
            # old_waypoint[1] = -old_waypoint[0]
    return old_waypoint


def move_the_waypoint(ist, amt, old_waypoint):
    if ist == "N":
        #move waypoint n
        old_waypoint[1] = old_waypoint[1] + amt
    elif ist == "S":
        #move the waypoint south
        old_waypoint[1] = old_waypoint[1] - amt
    elif ist == "W":
        #move the waypoint west 
        old_waypoint[0] = old_waypoint[0] - amt
    elif ist == "E":
        #move the waypoint east
        old_waypoint[0] = old_waypoint[0] + amt
    return old_waypoint

with open('data.txt') as raw_input:
    big_boat = [0,0]
    waypoint = [10,1]
    rotation = ["L", "R"]
    move_waypoint = ["N", "S", "W", "E"]
    for i in raw_input:
        instruction = i[:1]
        measure = int(i[1:])
        # print(instruction, measure)
        # if instruction in move_waypoint:
        #     #will move the waypoint relative to the boat
        #     waypoint = move_the_waypoint(instruction, (measure), waypoint)
        if instruction == "N":
            waypoint[1] += measure
        elif instruction == "S":
            waypoint[1] -= measure
        elif instruction == "W":
            waypoint[0] -= measure
        elif instruction == "E":
            waypoint[0] += measure
        # elif instruction == 'L':
        #     for _ in range(int(measure/90)):
        #         waypoint[0], waypoint[1] = -waypoint[1],waypoint[0]
        # elif instruction == 'R':
        #     for _ in range(int(measure/90)):
        #         waypoint[0], waypoint[1] = waypoint[1],-waypoint[0]
        elif instruction in rotation:
            #will flip the waypoint
            waypoint = rotate_around_the_boat(instruction, (measure), waypoint)
        elif instruction == "F":
            #moves the boat forward towards the waypoint
            big_boat[0] += waypoint[0] * measure
            big_boat[1] += waypoint[1] * measure
        else:
            assert False
    print(big_boat, waypoint)
    print(abs(big_boat[0]) + abs(big_boat[1]))

        