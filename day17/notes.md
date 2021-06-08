Day 17:
    Part One - 
        This is gonna be one of those "life game" type questions
        I have an infinite 3-D space, at each point i have a cube that is either on or off
        And I have the following rules
            - If a cube is active, and 2 or 3 of its neighbors are active then the cube remains active. Otherwise it becomes inactive.
            - If a cube is inactive but 3 of its neighbors are active, then the cube becomes active. Otherwise it stays inactive.
        I am suppose to return the number of active cubes at the end of 6 cycles

        My plan:
            1. I want to fill a dictionary useing the given data
            2. Then from there cycle 6 times using the given rules
