import utilities as utils
import gui
from tile import tile
from grid import grid
from bot import bot

def main():
    #Gather raw data
    raw_data = utils.read_file(gui.ask_filepath())

    g = grid(raw_data) #Build grid/initial state with raw data
    b = bot(g) #Build the bot

    b.a_star() #Let bot perform A* search

    replay = True
    while replay: #Conduct replay from initial to goal's optimal path
        gui.replay(b.open, b.closed, False)
        selection = input("\nEnter any key to replay or X/x to Exit: ")
        if selection.lower() == 'x':
            replay = False

def chk():
    print("This is driver.py")

if __name__ == "__main__":
    main()
    exit(0)