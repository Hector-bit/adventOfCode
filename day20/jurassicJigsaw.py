with open('test.txt') as raw_input:
    maps = {}
    id = None
    curr_map = []
    #This first part gets the tile id's to match the tile in a dictionary
    for i in raw_input:
        print(i)
        if "Tile" in i:
            id = i.replace("\n", "")
        elif "#" in i or "." in i:
            curr_map.append(i.replace("\n",""))
        else:
            maps[id] = curr_map
            id = None
            curr_map = []
    print(maps)
    #here we need a way to match add 
