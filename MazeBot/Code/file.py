import re
import os

import utils

def readfile(filename):
    data = [] #Returns content of file as string
    if os.stat(filename).st_size==0:
            utils.terminate("Empty file!",0)
    with open(filename, encoding='utf-8') as file:
        for line in file:
            data.append(line.strip())
    if not re.search("[0-9]", data[0]): #Check if first line is an integer, exit if otherwise
        utils.terminate("No n value at first line!\nExiting...", 0)
    data[0] = int(data[0]) #Convert n from str to int
    if data[0] < 3 or data[0] > 64: #Check if n value is 3<=n<=64, exit if otherwise.
        utils.print("Value of n out of bounds (3 <= n <= 64).", 0)
    for i in range(1,len(data),1):
        data[i] = data[i].upper()
    s = False
    g = False
    for d in range(1,len(data),1): #Search for S & G
        if 'S' in data[d]:
            s = True
        if 'G' in data[d]:
            g = True
    if not s and g: #Check if both S & G exists
        utils.terminate("Missing S/G values.\nS Found: " + str(s) + "\nG Found: " + str(g), 0)
    return data