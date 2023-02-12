import utilities as utils

class tile:
    def __init__(self, x:int, y:int, tile_type:chr):
        self.type = tile_type
        self.x = x
        self.y = y
        self.s_dist = 0
        self.g_dist = 0

    def isGoal(self):
        return 'G' in self.type

    def isStart(self):
        return 'S' in self.type

    def isBot(self):
        return 'B' in self.type
    
    def isWall(self):
        return '#' in self.type

    def isSpace(self):
        return '.' in self.type

    def get_coor(self):
        return self.x, self.y

    def get_attributes(self):
        return [self.type, self.x, self.y, self.s_dist, self.g_dist]

    def dist_s(self, s_x: int, s_y:int):
        self.s_dist = utils.find_manhattan(self.x, self.y, s_x, s_y)
    
    def dist_g(self, g_x:int, g_y:int):
        self.g_dist = utils.find_manhattan(self.x, self.y, g_x, g_y)
    
    def chk(self): #To check if the script/class imports correctly.
        print("This is tile.py")