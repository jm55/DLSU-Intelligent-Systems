import utilities
import gui
from tile import tile
from grid import grid

def main():
    #Import test
    t = tile(0,0,'S')
    g = grid()
    utilities.chk()
    t.chk()
    g.chk()
    gui.chk()
    chk()

def chk():
    print("This is driver.py")

if __name__ == "__main__":
    main()
    exit(0)