###############################################################################
# Map Module
###############################################################################
#for map table
from tabulate import tabulate


#Tile classes
class Tile():
    '''base class for tiles'''
    def __init__(self):
        """this is always overwritten in the child classes"""
        self.description = "description"
        self.actions = {"actions": False}


    def PrintDescription(self):
        """Prints description of the tile"""
        print(self.description)


class Camp(Tile):
    def __init__(self):
        self.description = "\nYou have entered a pirate camp"
        self.actions = {"Fight the pirates": False}


    def __str__(self):
        return("Camp")


class Key(Tile):
    def __init__(self):
        self.description = ("\nSomething shiny catches your eye\n" + 
        "After closer inspection, you find that it's a key")
        self.actions = {"Pick up the key": False}


    def __str__(self):
        return("Key")


class Patrol(Tile):
    def __init__(self):
        self.description = "\nYou encounter patrolling pirates"
        self.actions = {"Fight the pirates": False}


    def __str__(self):
        return("Patrol")


class Shovel(Tile):
    def __init__(self):
        self.description = "\nYou find a shovel on the ground"
        self.actions = {"Pick up the shovel": False}


    def __str__(self):
        return("Shovel")


class Start(Tile):
    def __init__(self):
        self.description = "\nThis is where you washed up"
        self.actions = {"Start actions": True}


    def __str__(self):
        return("Start")


class Trap(Tile):
    def __init__(self):
        self.description = "\nYou fall into a pit full of spikes"
        self.actions = {"Disable trap": False}


    def __str__(self):
        return("Trap")


class Treasure(Tile):
    def __init__(self):
        self.description = "\nOn the ground is a big red X"
        self.actions = {"Dig": False, "Unlock": True, 
                        "Take the treasure": True}


    def __str__(self):
        return("Treasure")


class Tree(Tile):
    def __init__(self):
        self.description = "\nOn the sandy shore, you spot a coconut tree"
        self.actions = {"Pick a coconut": False}


    def __str__(self):
        return("Tree")


#initializing tiles
Tree1 = Tree()
Trap1 = Trap()
Camp1 = Camp()
Treasure1 = Treasure()
Start1 = Start()
Patrol1 = Patrol()
Shovel1 = Shovel()
Camp2 = Camp()
Patrol2 = Patrol()
Trap2 = Trap()
Camp3 = Camp()
Key1 = Key()
#Map
islandMap = [[Tree1, Trap1, Camp1, Treasure1], 
             [Start1, Patrol1, Shovel1, Camp2], 
             [Patrol2, Trap2, Camp3, Key1]]


#map export file
mapFile = 'map.txt'

def mapExport():
    '''Exports the map to an external file'''
    try:
        with open(mapFile, "w") as file:
            file.write(tabulate(islandMap, tablefmt = "fancy_grid"))
        print("Your map has been updated")
    except:
        print("Unable to export map")
    else:
        print("You have a map")
    finally:
        print("Maybe that will help")


def viewMap():
    '''Prints the map from an external file'''
    try:
        with open(mapFile, "r") as file:
            print(file.read())
    except:
        print("Unable to read map")
    else:
        print("Nice map")
    finally:
        print("Maybe that will help")

