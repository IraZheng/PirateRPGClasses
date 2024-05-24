###############################################################################
# Player Module
###############################################################################
class Player():
    def __init__(self, posX, posY, coconuts, hasShovel, 
                 hasKey, hasTreasure, hp, maxHP, attack):
        '''
        posX: the x position of the player
        posY: the y position of the player
        coconuts: the number of coconuts the player has
        hasShovel: a bool if the player has the shovel
        hasKey: a bool if the player has the key
        hasTreasure: a bool if the player has the treasure
        hp: the health of the player
        maxHP: the most health the player can have at any given time
        attack: the attack of the player
        '''
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
        self.maxHP = maxHP
        self.attack = -attack


    def Move(self, map):
        """
        Allows players to move through the map
        map: the map that the player is moving on
        """
        while True:
            print("Which direction do you move?")
            #prints movement options
            if self.posY > 0:
                print("-Move north")
            if self.posY < (len(map) - 1):
                print("-Move south")
            if self.posX < (len(map[self.posY]) - 1):
                print("-Move east")
            if self.posX > 0:
                print("-Move west")
            #print("-Move north \n-Move south \n-Move east \n-Move west")
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
                if self.posY < (len(map) - 1):
                    self.posY += 1
                    break
                else:
                    print("Thats the end of the island, you can't go there!\n")
            elif moveChoice == "east":
                if self.posX < (len(map[self.posY]) - 1):
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
        """
        changes the player's hp
        amountToChange: the change in hp
        """
        self.hp += amountToChange
        print(f"you have {self.hp} hp")

    
    def PrintStatus(self):
        """prints the player's hp and attack"""
        print(f"you have {self.hp} hp")
        print(f"you have {-self.attack} attack")

