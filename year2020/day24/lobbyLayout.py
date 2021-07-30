

class BigNode():
    def __init__(self):
        self.east = None
        self.southEast = None
        self.southWest = None
        self.west = None
        self.northWest = None
        self.northEast = None
        self.color = "White"
    def goEast(self, dir):
        self.east = dir
    def goSouthEast(self, dir):
        self.southEast = dir
    def goSouthWest(self, dir):
        self.southWest = dir
    def goWest(self, dir):
        self.west = dir
    def goNorthWest(self, dir):
        self.northWest = dir
    def goNorthEast(self, dir):
        self.northEast = dir
    def changeColor(self):
        if self.color == "White":
            self.color = "Black"
        else:
            self.color = "White"
    

#the code below was a quick sanity check to make sure that my nodes worked
# startingNode = BigNode()
# searchNode = BigNode()
# # startingNode.east = searchNode
# startingNode.goEast(searchNode) 
# print(startingNode, startingNode.west, startingNode.east)
stepper = {'e': 'east', 'se': 'southEast', 'sw': 'southWest', 'w':'west', 'nw':'northWest', 'ne':'northEast'}
directions = {'east':'goEast', 'southEast':'goSouthEast', 'southWest':'goSouthWest', 'west':'goWest', 'northWest':'goNorthWest', 'northEast':'goNorthEast'}

startingNode = BigNode()
head = startingNode

with open('test.txt') as raw_input:
    for i in raw_input:
        meme = list(i)
        readstart = 0
        readend = 0
        # print(meme)
        for j in range(len(meme)):
            readend = j
            joined = ''.join(meme[readstart:readend])
            # print(joined)
            if joined in stepper.keys():
                if joined == 'e':
                    startingNode.goEast(BigNode())
                    startingNode = startingNode.east
                elif joined == 'se':
                    startingNode.goSouthEast(BigNode())
                    startingNode = startingNode.southEast
                elif joined == 'sw':
                    startingNode.goSouthWest(BigNode())
                    startingNode = startingNode.southWest
                elif joined == 'w':
                    startingNode.goWest(BigNode())
                    startingNode = startingNode.west
                elif joined == 'nw':
                    startingNode.goNorthEast(BigNode())
                    startingNode = startingNode.northWest
                elif joined == ''
                else:
                    startingNode = startingNode.stepper[joined]
                    startingNode.changeColor()
                readstart = readend
                print(joined)




