import utilities as utils
import gui
from tile import tile
from grid import grid
from bot import bot

def main():
    raw_data = utils.read_file(gui.ask_filepath())

    g = grid(raw_data)
    b = bot(g)
    b.a_star()
    input()
    #gui.print_simple_grid(g)

def chk():
    print("This is driver.py")

if __name__ == "__main__":
    main()
    exit(0)