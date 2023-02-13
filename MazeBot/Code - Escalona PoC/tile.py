import utilities as utils

class tile:
    def __init__(self, x:int, y:int, tile_type:chr):
        self.type = tile_type
        self.x = x
        self.y = y
        self.s_dist = 0
        self.g_dist = 0

    #Checks if the tile is a Goal or not
    def isGoal(self):
        return 'G' in self.type

    #Checks if the tile is a Start or not
    def isStart(self):
        return 'S' in self.type

    #Checks if the tile is a Bot or not
    def isBot(self):
        return 'B' in self.type
    
    #Checks if the tile is a Wall or not
    def isWall(self):
        return '#' in self.type

    #Checks if a tile is a Space or not
    def isSpace(self):
        return '.' in self.type

    #Returns tile's x,y coor as tuple
    def get_coor(self):
        return self.x, self.y

    #Returns tile's attributes: type, x, y, s_dist, g_dist
    def get_attributes(self):
        return [self.type, self.x, self.y, self.s_dist, self.g_dist]

    #Sets distance of tile from s given x,y coor of s
    def dist_s(self, s_x: int, s_y:int):
        self.s_dist = utils.find_manhattan(self.x, self.y, s_x, s_y)
    
    #Sets distance of tile from g given x,y, coor of g
    def dist_g(self, g_x:int, g_y:int):
        self.g_dist = utils.find_manhattan(self.x, self.y, g_x, g_y)