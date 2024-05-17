###############################################################################
# Player Module
###############################################################################
import map


class Player():
    def __init__(self, posX, posY, coconuts, hasShovel, 
                 hasKey, hasTreasure, hp, attack):
        #position
        self.posX = posX
        self.posY = posY
        #inventory
        self.coconuts = coconuts
        self.hasShovel = hasShovel
        self.hasKey = hasKey
        self.hasTreasure = hasTreasure
        #combat
        self.hp = hp
        self.attack = -attack


    def Move(self):
        """Allows players to move through the map"""
        while True:
            print("Which direction do you move?")
            #prints movement variable
            print("-Move north \n-Move south \n-Move east \n-Move west")
            print("-Back")
            #default input is a string so I can use .lower()
            moveChoice = input("-").lower()
            #for map movement
            if moveChoice == "north":
                if self.posY > 0:
                    self.posY -= 1
                    break
                else:
                    print("Thats the end of the island, you can't go there!\n")
            elif moveChoice == "south":
                if self.posY < (len(map.islandMap) - 1):
                    self.posY += 1
                    break
                else:
                    print("Thats the end of the island, you can't go there!\n")
            elif moveChoice == "east":
                if self.posX < (len(map.islandMap[self.posY]) - 1):
                    self.posX += 1
                    break
                else:
                    print("Thats the end of the island, you can't go there!\n")
            elif moveChoice == "west":
                if self.posX > 0:
                    self.posX -= 1
                    break
                else:
                    print("Thats the end of the island, you can't go there!\n")
            elif moveChoice == "back":
                break
            else:
                print('Please choose "north", "south", ' + 
                      '"east", "west" or "back"\n')


    def PrintInv(self):
        """prints player's inventory"""
        print("\nIn your inventory, you have:")
        print(f'-{self.coconuts} coconuts')
        if self.hasShovel:
            print("-A shovel")
        else:
            print("-No shovel")
        if self.hasKey:
            print("-A key")
        else:
            print("-No key")
        if self.hasTreasure:
            print("-The pirate's treasure")
        else:
            print("-No treasure")

    def ChangeHP(self, amountToChange):
        self.hp += amountToChange
        print(f"you have {self.hp} hp")

    def PrintStatus(self):
        print(f"you have {self.hp} hp")
        print(f"you have {-self.attack} attack")