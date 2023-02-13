import os
import re

from tile import tile

#Return a bar at a given character length
def bar(length:int, fillchar:chr="="):
    return str("".center(length, fillchar))

#Get a header for printout (either for display or .txt file)
def header():
    h = "".center(40,"=") + "\n"
    h += "CSINTSY".center(40," ") + "\n"
    h += "MazeBot".center(40," ") + "\n"
    h += "Cruzada, Escalona, Francisco, Loyola".center(40," ") + "\n"
    h += "".center(40,"=") + "\n"
    return h

#Terminate program with proper reason and status code
def terminate(reason:str, status:int=0):
    cls()
    print(header())
    print("SAFETY TERMINATION:\n" + reason)
    print("\nExiting...")
    exit(status)

#Read a given file using it's filepath
def read_file(filepath:str):
    if not os.path.isfile(filepath):
        terminate("File (" + filepath + ") non existent!",0)
    elif os.path.getsize(filepath) <= 0:
        terminate("File (" + filepath + ") is empty!", 0)

    data = []
    size = 0
    ctr = 0
    with open(filepath, encoding='utf-8') as file: #Open file
        for line in file: #For every line in file
            if ctr == 0: #For 1st line, size of grid
                size = line.strip()
                if not re.search("[0-9]", size): #Check if first line is an integer, exit if otherwise
                    terminate("No n value at first line!\nExiting...", 0)
                size = int(size)
                if size < 3 or size > 64: #Check if n value is 3<=n<=64, exit if otherwise.
                    terminate("Value of n out of bounds (3 <= n <= 64).", 0)
                ctr += 1 #Increment
            else: #For every other line
                if len(line.strip()) != size:
                    terminate("Row size mismatch: \'" + line.strip() + "\'")
                else:
                    data.append(line.strip())
    s = 0
    g = 0
    for d in range(len(data)): #Search for S & G
        if 'S' in data[d]:
            s = s + 1
        if 'G' in data[d]:
            g = g + 1
    if not (s==1 and g==1): #Check if both S & G exists; Only 1 of each
        terminate("Missing or Too much S/G values.\nS Found: " + str(s) + "\nG Found: " + str(g), 0)
    
    return data

#Compute for manhattan dist of two coordinates
def find_manhattan(xi:int, yi:int, xf:int, yf:int):
    return abs(xf-xi) + abs(yf-yi)

#Compute for manhattan dist of two tiles
def find_manhattan_tile(tile_init:tile, tile_final:tile):
    return find_manhattan(tile_init.x, tile_init.y, tile_final.x, tile_final.y)

#Execute 'cls' command on Command Prompt
def cls(): 
    os.system("cls")