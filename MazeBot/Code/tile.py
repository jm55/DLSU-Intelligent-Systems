
class tile:
    def __init__(self, x:int, y:int, tile_type:chr):
        self.x = x
        self.y = y
        self.s_dist = 0
        self.g_dist = 0
        self.type = tile_type
    
    def dist_s(self, s_x: int, s_y:int):
        #Compute tile's distance from s[x,y]
        return 0
    
    def dist_g(self, g_x:int, g_y:int):
        #Compute tile's distance from g[x,y]
        return 0
    
    def chk(self): #To check if the script/class imports correctly.
        print("This is tile.py")