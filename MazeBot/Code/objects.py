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
        self.g_dist = get_manhattan((self.x, self.y), (g_x, g_y))
        return self.g_dist

    #Returns tile's x,y coor as tuple
    def get_coor(self):
        return self.x, self.y

    #Checks if the tile is a Goal or not
    def isGoal(self):
        return 'G' in self.type

    #Checks if the tile is a Start or not
    def isStart(self):
        return 'S' in self.type

    #Checks if the tile is a Bot or not
    def isBot(self):
        return 'B' in self.type
    
    def get_pos(self):
        """Returns the coordinate of this tile object"""
        return (self.x, self.y)
    
    def __str__(self):
        return f"Type: {self.type} - x:{self.x} y:{self.y}"
        
class grid:
    def __init__(self, tiles:tile):
        self.tiles = tiles #2D array of tile objects
    
    def get_tiles(self):
        return self.tiles

    def get_size(self):
        return len(self.tiles)
    
    def get_tile(self, value:chr):
        """Returns a tile object based on the given value"""
        x = 0
        y = 0
        for row in self.tiles:
            for col in row:
                if value in col.type:
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

    #Update position of 'bot'; Assumes that landing location is allowed/valid
    #Note that this is just the representation of the bot on the grid. The logic behind the bot's state selection is still different from here.
    #Every call of the update bot represents change in the g_cost/move count.
    def update_bot(self, x:int,y:int):
        b_loc = self.locate_bot()
        s_loc = self.locate_s()
        g_loc = self.locate_g()

        #Reset current tile to initial
        if b_loc == s_loc: #Bot at S
            self.tiles[s_loc[0]][s_loc[1]].type = 'S'
        elif b_loc == g_loc: #Bot at G
            self.tiles[g_loc[0]][g_loc[1]].type = 'G'
        else: #Bot at .
            self.tiles[b_loc[0]][b_loc[1]].type = '.'
        
        if (x,y) == s_loc:
            self.tiles[x][y].type = 'SB'
        elif (x,y) == g_loc:
            self.tiles[x][y].type = 'GB'
        else:
            self.tiles[x][y].type = 'B'

        #self.g_cost += 1
        #self.compute_distances()
        #self.compute_costs()

    def compute_costs(self):
        self.h_cost = self.get_bot().g_dist
        self.f_cost = self.g_cost + self.h_cost

    #Compute distances of tiles from S and G
    def compute_distances(self):
        size = self.get_size()
        s_loc = self.locate_s()
        g_loc = self.locate_g()

        for y in range(size):
            for x in range(size):
                self.tiles[y][x].dist_s(s_loc[0], s_loc[1])
                self.tiles[y][x].dist_g(g_loc[0], g_loc[1])

     #Locate the Goal assuming that tiles are not empty
    def locate_g(self):
        if len(self.tiles) == 0:
            return None
        for row in self.tiles:
            for col in row:
                if col.isGoal():
                    return col.get_coor()

    #Locate the Bot assuming that tiles are not empty
    def locate_bot(self):
        if len(self.tiles) == 0:
            return None
        for row in self.tiles:
            for col in row:
                if col.isBot():
                    return col.get_coor()

    #Locate the Start assuming that tiles are not empty
    def locate_s(self):
        if len(self.tiles) == 0:
            return None
        for row in self.tiles:
            for col in row:
                if col.isStart():
                    return col.get_coor()
                
     #Get Bot Tile Object
    def get_bot(self):
        b_loc = self.locate_bot()
        return self.tiles[b_loc[0]][b_loc[1]]
            
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

def get_manhattan(pos1, pos2):
    """Returns the manhattan distance between two points"""
    return (abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]))