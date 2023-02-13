import utilities as utils
from tile import tile

class grid:
    def __init__(self, raw_data:list, g_cost:int=0):
        self.tiles = self.create_grid(raw_data) #2D array of tile objects
        init_loc = self.locate_s()
        self.tiles[init_loc[1]][init_loc[0]].type = 'SB'
        self.f_cost = 0
        self.g_cost = g_cost
        self.h_cost = 0
        self.compute_distances()
        self.compute_costs()

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

    #Build the grid data be forming the basic 
    def create_grid(self, raw_data):
        raw_data = ['....G', '.####', '...#S', '.#.#.', '.#...'] #Temporary copy
        tiles = []

        if type(raw_data) != list:
            utils.terminate("Incorrect data!",2)
        if len(raw_data) == 0:
            utils.terminate("Empty list!",2)
        
        for y in range(len(raw_data)): #Y
            row_tiles = []
            for x in range(len(raw_data[y])): #X
                row_tiles.append(tile(x,y,raw_data[y][x]))
            tiles.append(row_tiles)
        
        return tiles

    #Returns list of bot's neighbors
    #Excludes neighbors that are invalid (exceeds grid limits) or is a wall
    def neighbor_bot(self):
        x = self.locate_bot()[0]
        y = self.locate_bot()[1]
        traversable = [[x,y-1],[x-1,y],[x,y+1],[x+1,y]]
        for s in range(len(traversable)):
            if traversable[s][0] < 0 or traversable[s][0] >= self.get_size() or traversable[s][1] < 0 or traversable[s][1] >= self.get_size():
                traversable[s] = None
            if traversable[s] != None:
                if self.get_tiles()[traversable[s][1]][traversable[s][0]].isWall():
                    traversable[s] = None
        return traversable
    
    def check_if_goal(self):
        if self.locate_bot() == self.locate_g():
            return True
        return False

    #Update position of 'bot'; Assumes that landing location is allowed/valid
    #Note that this is just the representation of the bot on the grid. The logic behind the bot's state selection is still different from here.
    #Every call of the update bot represents change in the g_cost/move count.
    def update_bot(self, x:int,y:int):
        b_loc = self.locate_bot()
        s_loc = self.locate_s()
        g_loc = self.locate_g()

        #Reset current tile to initial
        if b_loc == s_loc: #Bot at S
            self.tiles[s_loc[1]][s_loc[0]].type = 'S'
        elif b_loc == g_loc: #Bot at G
            self.tiles[g_loc[1]][g_loc[0]].type = 'G'
        else: #Bot at .
            self.tiles[b_loc[1]][b_loc[0]].type = '.'
        
        if (x,y) == s_loc:
            self.tiles[y][x].type = 'SB'
        elif (x,y) == g_loc:
            self.tiles[y][x].type = 'GB'
        else:
            self.tiles[y][x].type = 'B'

        self.g_cost += 1
        self.compute_distances()
        self.compute_costs()

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

    #Get Costs as List [f, g, h]
    def get_costs(self):
        return [self.f_cost, self.g_cost, self.h_cost]

    #Get Start Tile object
    def get_s(self):
        s_loc = self.locate_s()
        return self.tiles[s_loc[1]][s_loc[0]]

    #Get Goal Tile object
    def get_g(self):
        g_loc = self.locate_g()
        return self.tiles[g_loc[1]][g_loc[0]]

    #Get Bot Tile Object
    def get_bot(self):
        b_loc = self.locate_bot()
        return self.tiles[b_loc[1]][b_loc[0]]

    #Get size of grid
    def get_size(self):
        return len(self.tiles)

    #Get tiles as 2D list
    def get_tiles(self):
        return self.tiles
    
    def chk(self): #To check if the script/class imports correctly.
        print("This is grid.py") 
    
    def test_print(self):
        utils.cls()
        size = len(self.tiles)
        utils.bar(size*4)
        print("Costs: ", self.get_costs())
        print("Valid Moves: ", self.neighbor_bot())
        utils.bar(size*4)
        for y in range(size):
            row = ""
            for x in range(size):
                tile = self.tiles[y][x].get_attributes()
                row = row + tile[0] + " "
            print(row)
        utils.bar(size*4)