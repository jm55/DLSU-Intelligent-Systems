class tile:
    def __init__(self, x:int, y:int, tile_type:chr):
        self.x = x
        self.y = y
        self.s_dist = 0
        self.g_dist = 0
        self.priority = 0
        self.type = tile_type
        self.parent = None
    
    def dist_s(self, s_x: int, s_y:int):
        """Compute tile's distance from s[x,y]"""
        self.s_dist = get_manhattan((self.x, self.y), (s_x, s_y))
        return self.s_dist
    
    def dist_g(self, g_x:int, g_y:int):
        """Compute tile's distance from g[x,y]"""
        self.g_dist = get_manhattan((self.x, self.y), (g_x, _y))
        return self.g_dist

    
    def get_pos(self):
        """Returns the coordinate of this tile object"""
        return (self.x, self.y)
    
    def __str__(self):
        return f"Type: {self.type} - x:{self.x} y:{self.y}"
    # def __eq__(self, tile):
    #     return (self.x, self.y) == (tile.x, tile.y)
    
    # def chk(self): #To check if the script/class imports correctly.
    #     print("This is tile.py")
        
class grid:
    def __init__(self, tiles:tile):
        self.tiles = tiles #2D array of tile objects
    
    def get_tiles(self):
        return None
    
    def get_tile(self, value:chr):
        """Returns a tile object based on the given value"""
        x = 0
        y = 0
        for row in self.tiles:
            for col in row:
                if value == col.type:
                    return col
                y += 1       
            y = 0
            x += 1
    def get_type(self, x:int, y:int):
        """Returns the type of the tile in the grid"""
        return self.tiles[x][y].type
    
    
    def check_action(self, x:int, y:int, actions:list, parent_pos):
        """Checks if the tile coordinate for an action is valid and appends it to the action list"""
        if self.get_type(x, y) != '#':
            actions.append(self.tiles[x][y])
            #print(f"Parent: {self.tiles[x][y].parent}")
            if self.tiles[x][y].parent == None and self.tiles[x][y].type != "S":
                self.tiles[x][y].parent = self.tiles[parent_pos[0]][parent_pos[1]]
                #print(f"Parent: {self.tiles[x][y].parent}")
            #print((x, y))
            
    def get_actions(self, tile:tile):
        actions = []
        """Returns a list of valid tile objects to explore"""
        #print(f"Valid actions for tile ({tile.x}, {tile.y}):")
        
        if tile.x-1 >= 0:
            self.check_action(tile.x-1, tile.y, actions, tile.get_pos())   
        if tile.y-1 >= 0:
            self.check_action(tile.x, tile.y-1, actions, tile.get_pos())
        if tile.x+1 < len(self.tiles):
            self.check_action(tile.x+1, tile.y, actions, tile.get_pos())
        if tile.y+1 < len(self.tiles):  
            self.check_action(tile.x, tile.y+1, actions, tile.get_pos()) 

        return actions
    # def chk(self): #To check if the script/class imports correctly.
    #     print("This is grid.py") 
            
class bot:
    def __init__(self, pos=None):
        self.pos = pos
        
    def __str__(self):
        return f"Bot is at position: {self.pos[0]}, {self.pos[1]}"
    
class State():
    def __init__(self, grid, bot_pos):
        # add bot character to grid
        grid[bot_pos[0]][bot_pos[1]][0] = "X" # Temp bot char
        self.grid = grid
        