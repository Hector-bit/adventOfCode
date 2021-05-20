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
    new_waypoint = old_waypoint
    tempx = new_waypoint[0]
    tempy = new_waypoint[1]
    global quadrant
    if amt == 180:
        new_waypoint[0] = -tempx
        new_waypoint[1] = -tempy
    if ist == "L":
        new_waypoint[0] = which_quadrantXL(quadrant, tempy, amt)
        new_waypoint[1] = which_quadrantYL(quadrant, tempx, amt)
    if ist == "R":
        new_waypoint[0] = which_quadrantXR(quadrant, tempy, amt)
        new_waypoint[1] = which_quadrantYR(quadrant, tempx, amt)
    return new_waypoint

def move_the_waypoint(ist, amt, old_waypoint):
    new_waypoint = old_waypoint
    if ist == "N":
        #move waypoint n
        new_waypoint[1] = new_waypoint[1] + amt
    elif ist == "S":
        #move the waypoint south
        new_waypoint[1] = new_waypoint[1] - amt
    elif ist == "W":
        #move the waypoint west 
        new_waypoint[0] = new_waypoint[0] - amt
    elif ist == "E":
        #move the waypoint east
        new_waypoint[0] = new_waypoint[0] + amt
    return new_waypoint

def boat_move(bb, dd, ww):
    bb[0] += ww[0] * dd
    bb[1] += ww[1] * dd
    # print(bb)
    return bb

with open('data.txt') as raw_input:
    big_boat = [0,0]
    waypoint = [10,1]
    rotation = ["L", "R"]
    move_waypoint = ["N", "S", "W", "E"]
    for i in raw_input:
        instruction = i[:1]
        measure = i[1:]
        # print(instruction, measure)
        if instruction in rotation:
            #will flip the waypoint
            waypoint = rotate_around_the_boat(instruction, int(measure), waypoint)
        elif instruction in move_waypoint:
            #will move the waypoint relative to the boat
            waypoint = move_the_waypoint(instruction, int(measure), waypoint)
        elif instruction == "F":
            #moves the boat forward towards the waypoint
            big_boat = boat_move(big_boat, int(measure), waypoint)
    print(big_boat, waypoint)
    print(abs(big_boat[0]) + abs(big_boat[1]))

        