###############################################################################
# Map Module
###############################################################################
#for map table
from tabulate import tabulate


#Tile classes
class Tile():
    '''base class for tiles'''
    def __init__(self):
        """
        this is always overwritten in the child classes
        this is only here in case of errors
        """
        self.description = "description"
        self.actions = {"actions": False}


    def PrintDescription(self):
        """Prints description of the tile"""
        print(self.description)


class Camp(Tile):
    def __init__(self):
        '''sets up the description and the actions available for the tile'''
        self.description = "\nYou have entered a pirate camp"
        self.actions = {"Fight the pirates": False}


    def __str__(self):
        '''__str__ method to show on map'''
        return("Camp")


class Key(Tile):
    def __init__(self):
        '''sets up the description and the actions available for the tile'''
        self.description = ("\nSomething shiny catches your eye\n" + 
        "After closer inspection, you find that it's a key")
        self.actions = {"Pick up the key": False}


    def __str__(self):
        '''__str__ method to show on map'''
        return("Key")


class Patrol(Tile):
    def __init__(self):
        '''sets up the description and the actions available for the tile'''
        self.description = "\nYou encounter patrolling pirates"
        self.actions = {"Fight the pirates": False}


    def __str__(self):
        '''__str__ method to show on map'''
        return("Patrol")


class Shovel(Tile):
    def __init__(self):
        '''sets up the description and the actions available for the tile'''
        self.description = "\nYou find a shovel on the ground"
        self.actions = {"Pick up the shovel": False}


    def __str__(self):
        '''__str__ method to show on map'''
        return("Shovel")


class Start(Tile):
    def __init__(self):
        '''sets up the description and the actions available for the tile'''
        self.description = "\nThis is where you washed up"
        self.actions = {"Start actions": True}


    def __str__(self):
        '''__str__ method to show on map'''
        return("Start")


class Trap(Tile):
    def __init__(self):
        '''sets up the description and the actions available for the tile'''
        self.description = "\nYou fall into a pit full of spikes"
        self.actions = {"Disable trap": False}


    def __str__(self):
        '''__str__ method to show on map'''
        return("Trap")


class Treasure(Tile):
    def __init__(self):
        '''sets up the description and the actions available for the tile'''
        self.description = "\nOn the ground is a big red X"
        self.actions = {"Dig": False, "Unlock": True, 
                        "Take the treasure": True}


    def __str__(self):
        '''__str__ method to show on map'''
        return("Treasure")


class Tree(Tile):
    def __init__(self):
        '''sets up the description and the actions available for the tile'''
        self.description = "\nOn the sandy shore, you spot a coconut tree"
        self.actions = {"Pick a coconut": False}


    def __str__(self):
        '''__str__ method to show on map'''
        return("Tree")


def mapExport(map, fileName):
    '''
    Exports the map to an external file
    map: the actual map that is saved
    fileName: the file for the map
    '''
    try:
        with open(fileName, "w") as file:
            file.write(tabulate(map, tablefmt = "fancy_grid"))
        print("Your map has been updated")
    except:
        print("Unable to export map")
    else:
        print("You have a map")
    finally:
        print("Maybe that will help")


def viewMap(fileName):
    '''
    Prints the map from an external file
    fileName: the file for the map
    '''
    try:
        with open(fileName, "r") as file:
            print(file.read())
    except:
        print("Unable to read map")
    else:
        print("Nice map")
    finally:
        print("Maybe that will help")

