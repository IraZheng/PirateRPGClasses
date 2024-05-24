###############################################################################
#Title: Pirate Adventure RPG
#Class: CS 30
#Assignment:Object-Orientated Programming: RPG - Classes
#Coder: Ira Zheng
#Version: 4.0
###############################################################################
'''A text-based RPG where you fight pirates'''
###############################################################################
# Imports and Global Variables ------------------------------------------------
import enemy
import map
import player

#player setup
Player1 = player.Player(0, 1, 0, False, False, False, 10, 10, 1)
#Enemy setup
Pirate1 = enemy.Pirate(0, 2, 3, 1, 2, 0)
Pirate2 = enemy.Pirate(0, 2, 3, 1, 2, 0)
Pirate3 = enemy.Pirate(1, 1, 3, 1, 2, 0)
Pirate4 = enemy.Pirate(1, 1, 3, 1, 2, 0)
Pirate5 = enemy.Pirate(2, 0, 3, 1, 2, 0)
Pirate6 = enemy.Pirate(2, 0, 3, 1, 2, 0)
Pirate7 = enemy.Pirate(2, 0, 3, 1, 2, 0)
Pirate8 = enemy.Pirate(2, 2, 3, 1, 2, 0)
Pirate9 = enemy.Pirate(2, 2, 3, 1, 2, 0)
Pirate10 = enemy.Pirate(2, 2, 3, 1, 2, 0)
Pirate11 = enemy.Pirate(3, 1, 3, 1, 2, 0)
Pirate12 = enemy.Pirate(3, 1, 3, 1, 2, 0)
Pirate13 = enemy.Pirate(3, 1, 3, 1, 2, 0)
#list of all enemies
enemyList = [Pirate1, Pirate2, Pirate3, Pirate4, Pirate5, Pirate6, Pirate7,
            Pirate8, Pirate9, Pirate10, Pirate11, Pirate12, Pirate13]
#map/tile setup
#initializing tiles
Tree1 = map.Tree()
Trap1 = map.Trap()
Camp1 = map.Camp()
Treasure1 = map.Treasure()
Start1 = map.Start()
Patrol1 = map.Patrol()
Shovel1 = map.Shovel()
Camp2 = map.Camp()
Patrol2 = map.Patrol()
Trap2 = map.Trap()
Camp3 = map.Camp()
Key1 = map.Key()
#Map
islandMap = [[Tree1, Trap1, Camp1, Treasure1], 
             [Start1, Patrol1, Shovel1, Camp2], 
             [Patrol2, Trap2, Camp3, Key1]]
#map export file
mapFile = 'map.txt'


# Functions -------------------------------------------------------------------
def encounterActions(action, room):
    '''
    allows the player to do different things in different encounters
    action: the action the player is taking
    room: the room the player is in
    '''
    #if room.actions[action] = True, the action has already been completed
    #for camp rooms
    if "Camp" in str(room):
        if action == "Fight the pirates":
            combat()
            #you beat the pirates if hp > 0
            if not Player1.hp <= 0:
                room.actions[action] = True
                room.description = "\nIt's where you fought a pirate camp"
                print("You beat the pirates")
    #for key room
    elif "Key" in str(room):
        if action == "Pick up the key":
            Player1.hasKey = True
            #already picked up the key
            room.actions[action] = True
            #change key description
            room.description = "\nThis is where you found the key"
            print("You have picked up the key")
    #for patrol room
    elif "Patrol" in str(room):
        if action == "Fight the pirates":
            combat()
            #you beat the pirates if hp > 0
            if not Player1.hp <= 0:
                room.actions[action] = True
                room.description = "\nIt's where you fought a pirate patrol"
                print("You beat the pirates")
    #for shovel room
    elif "Shovel" in str(room):
        if action == "Pick up the shovel":
            Player1.hasShovel = True
            #already picked up shovel
            room.actions[action] = True
            #change shovel description
            room.description = "\nThis is where you found the shovel"
            print("You have picked up the shovel")
    #start room should have no actions
    elif "Start" in str(room):
        pass
    #trap room
    elif "Trap" in str(room):
        if action == "Disable trap":
            room.actions[action] = True
            room.description = "\nIt's a disabled trap"
            print("Trap disabled!")
    #treasure room
    elif "Treasure" in str(room):
        if action == "Dig":
            #can only dig if you have the shovel
            if Player1.hasShovel:
                print("You have dug up the treasure")
                #unlocks the unlock option lol
                room.actions[action] = True
                room.actions["Unlock"] = False
                room.description = "\nIt's a locked treasure chest"
            else:
                print("You need a shovel to dig up the treasure!")
        elif action == "Unlock":
            #check for key
            if Player1.hasKey:
                print("You have unlocked the treasure")
                room.actions[action] = True
                room.actions["Take the treasure"] = False
                room.description = "\nIt's an unlocked treasure chest"
            else:
                print("You do not have a key")
        elif action == "Take the treasure":
            #win
            room.actions[action] = False
            print("\nYou have obtained the pirates treasure!")
            room.description = "\nIt's an empty treasure chest"
            Player1.hasTreasure = True
            print("Congratulations! \nYou have beat the game!")
            #end of game loop
            invalidChoice = True
            while invalidChoice:
                print("Do you wish to continue playing\n-Yes \n-No")
                choice = input("-").capitalize()
                if choice == "Yes":
                    #resets the chest to before taking the trasure
                    print("You put the treasure back in the chest")
                    print("Come back and pick it up when you want to")
                    #main menu loop is controlled by hasTreasure
                    Player1.hasTreasure = False
                    room.actions["Unlock"] = True
                    room.actions[action] = False
                    room.description = "\nIt's an unlocked treasure chest"
                    invalidChoice = False
                elif choice == "No":
                    print("Goodbye!")
                    invalidChoice = False
                else:
                    print('Please choose "Yes" or "No"')
    #for tree room
    elif "Tree" in str(room):
        if action == "Pick a coconut":
            if Player1.coconuts < 10:
                Player1.coconuts += 1
                print(f'You have {Player1.coconuts} coconuts')
            else:
                print("You cannot carry any more coconuts")


def combat():
    '''a function that handles battles'''
    #creates a combat list with the pirates in the same room as you
    combatList = []
    for object in enemyList:
        if (islandMap[object.posY][object.posX] == 
            islandMap[Player1.posY][Player1.posX]):
            combatList.append(object)
    #combat option loop
    while True:
        print("\nYou are in combat")
        for target in range(len(combatList)):
            print(f"-{target + 1}.{combatList[target]}")
        #allows use of coconuts during battle
        if Player1.coconuts > 0:
            print("-Use a coconut")
        choice = input("-").capitalize()
        if choice == "Use a coconut" and Player1.coconuts > 0:
            if Player1.hp < Player1.maxHP:
                Player1.coconuts -= 1
                print("\nYou have used a coconut")
                print(f"You have {Player1.coconuts} coconuts left")
                Player1.ChangeHP(1)
                for target in combatList:
                    target.CountDown()
            else:
                print("You are already at max hp")
        else:
            #uses numbers to differentiate the different enemies
            try:
                numChoice = int(choice)
            except ValueError:
                print("\nPlease choose one of the listed numbers")
                continue
            if 1 <= numChoice <= len(combatList):
                #enemy loop
                while True:
                    print(f"\n{numChoice}.Pirate")
                    print("-Check\n-Attack\n-Back")
                    action = input("-").capitalize()
                    if action == "Check":
                        combatList[numChoice-1].Check()
                        for target in combatList:
                            target.CountDown()
                        break
                    elif action == "Attack":
                        print("\nYou have hit the Pirate")
                        combatList[numChoice-1].ChangeHP(Player1.attack)
                        for target in combatList:
                            target.CountDown()
                            #print(target.attackTimer)
                        break
                    elif action == "Back":
                        break
                    else:
                        print("Invalid action")
            else:
                print("\nPlease choose one of the listed numbers")
        #removes dead enemies from the lists
        for target in combatList:
            if target.hp <= 0:
                combatList.remove(target)
                #del(target)
                enemyList.remove(target)
                #print(combatList)
                #print(enemyList)
        #alive enemies will attack if their cooldown is up
        for target in combatList:
            if target.attackTimer == target.attackCooldown:
                print(f"\nYou have been attacked by {str(target)}")
                Player1.ChangeHP(target.attack)
                target.attackTimer = 0
            #print(target.attackTimer)
        #exits combat loop if player dies or all enemies die
        if Player1.hp <= 0:
            break
        if len(combatList) == 0:
            break


def mainMenu():
    """
    Main menu
    allows player to choose options and run code
    """
    #while the player hasn't won
    while not Player1.hasTreasure:
        playerLocation = islandMap[Player1.posY][Player1.posX]
        print(playerLocation.description)
        #if you are in trap room
        if ("Trap" in str(playerLocation) and 
            not playerLocation.actions["Disable trap"]):
            print("You take damage from the spikes!")
            Player1.ChangeHP(-3)
        #if the player is alive
        if Player1.hp >= 1:
            print("What do you do?")
            #prints action as an option if action is not completed yet
            for action in playerLocation.actions:
                if (not playerLocation.actions[action]):
                    print(f'-{action}')
            if Player1.coconuts > 0:
                print("-Use a coconut")
            print("-Check status\n-Inventory\n-Move\n-Map\n-Quit")
            #takes user's choice
            choice = input("-").capitalize()
            #choice handler
            if choice == "Move":
                #if there are pirates, restrict movement
                if ("Camp" in str(playerLocation) or 
                    "Patrol" in str(playerLocation)):
                    if playerLocation.actions["Fight the pirates"]:
                        print("Okay!\n")
                        Player1.Move(islandMap)
                    else:
                        print("The pirates are blocking your way!")
                else:
                    print("Okay!\n")
                    Player1.Move(islandMap)
            #if it is a valid action and the action is not completed yet
            elif (choice in playerLocation.actions and 
                  not playerLocation.actions[choice]):
                encounterActions(choice, playerLocation)
            #heals by 1 when using a coconut
            elif Player1.coconuts > 0 and choice == "Use a coconut":
                #cannot heal at max hp
                if Player1.hp < Player1.maxHP:
                    Player1.coconuts -= 1
                    print("\nYou have used a coconut")
                    print(f"You have {Player1.coconuts} coconuts left")
                    Player1.ChangeHP(1)
                else:
                    print("You are already at max hp")
            elif choice == "Check status":
                Player1.PrintStatus()
            elif choice == "Inventory":
                Player1.PrintInv()
            elif choice == "Map":
                map.viewMap(mapFile)
            elif choice == "Quit":
                print("\nYou have quit your adventure")
                break
            else:
                print("That's not a valid option!")
        else:
            print("\nYou have died")
            break
            

def intro():
    '''prints an intro'''
    print("After a massive hurricane, you are seperated from your crew")
    print("You wash up on a pirate infested island")
    print("You realise that there is treasure on the island and " + 
          "decide to steal it")


# Main ------------------------------------------------------------------------
intro()
map.mapExport(islandMap, mapFile)
mainMenu()