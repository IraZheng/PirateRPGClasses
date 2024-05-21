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

Player1 = player.Player(0, 1, 0, False, False, False, 10, 1)

#add enemies here
Pirate1 = enemy.Pirate(0, 2, 3, 1, 2, 0)
Pirate2 = enemy.Pirate(0, 2, 3, 1, 2, 0)
enemyDict = {Pirate1: map.islandMap[Pirate1.posY][Pirate1.posX], 
             Pirate2: map.islandMap[Pirate2.posY][Pirate2.posX]}
# Functions -------------------------------------------------------------------
def encounterActions(action, room):
    '''
    allows the player to do different things in different encounters
    action: the action the player is taking
    room: the room the player is in
    '''
    #if room.actions[action] = True, the action has already been completed
    if "Camp" in str(room):
        if action == "Fight the pirates":
            Combat()
            if not Player1.hp <= 0:
                room.actions[action] = True
                room.description = "\nIt's where you fought a pirate camp"
                print("You beat the pirates")
    elif "Key" in str(room):
        if action == "Pick up the key":
            Player1.hasKey = True
            #already picked up the key
            room.actions[action] = True
            #change key description
            room.description = "\nThis is where you found the key"
            print("You have picked up the key")
    elif "Patrol" in str(room):
        if action == "Fight the pirates":
            Combat()
            if not Player1.hp <= 0:
                room.actions[action] = True
                room.description = "\nIt's where you fought a pirate patrol"
                print("You beat the pirates")
    elif "Shovel" in str(room):
        if action == "Pick up the shovel":
            Player1.hasShovel = True
            #already picked up shovel
            room.actions[action] = True
            #change shovel description
            room.description = "\nThis is where you found the shovel"
            print("You have picked up the shovel")
    elif "Start" in str(room):
        pass
    elif "Trap" in str(room):
        if action == "Disable trap":
            room.actions[action] = True
            room.description = "\nIt's a disabled trap"
            print("Trap disabled!")
    elif "Treasure" in str(room):
        if action == "Dig":
            if Player1.hasShovel:
                print("You have dug up the treasure")
                room.actions[action] = True
                room.actions["Unlock"] = False
                room.description = "\nIt's a locked treasure chest"
            else:
                print("You need a shovel to dig up the treasure!")
        elif action == "Unlock":
            if Player1.hasKey:
                print("You have unlocked the treasure")
                room.actions[action] = True
                room.actions["Take the treasure"] = False
                room.description = "\nIt's an unlocked treasure chest"
            else:
                print("You do not have a key")
        elif action == "Take the treasure":
            room.actions[action] = False
            print("\nYou have obtained the pirates treasure!")
            room.description = "\nIt's an empty treasure chest"
            Player1.hasTreasure = True
            print("Congratulations! \nYou have beat the game!")
            invalidChoice = True
            while invalidChoice:
                print("Do you wish to continue playing\n-Yes \n-No")
                choice = input("-").capitalize()
                if choice == "Yes":
                    print("You put the treasure back in the chest")
                    print("Come back and pick it up when you want to")
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
    elif "Tree" in str(room):
        if action == "Pick a coconut":
            Player1.coconuts += 1
            print(f'You have {Player1.coconuts} coconuts')


def Combat():
    '''a function that handles battles'''
    combatList = []
    for object in enemyDict:
        if enemyDict[object] == map.islandMap[Player1.posY][Player1.posX]:
            combatList.append(object)
    while True:
        print("\nYou are in combat")
        for target in range(len(combatList)):
            print(f"-{target + 1}.{combatList[target]}")
        try:
            choice = int(input("-"))
        except ValueError:
            print("\nPlease choose one of the listed numbers")
            continue
        if 1 <= choice <= len(combatList):
            #print(choice)
            while True:
                print(f"\n{choice}.Pirate")
                print("-Check\n-Attack\n-Back")
                action = input("-").capitalize()
                if action == "Check":
                    combatList[choice-1].Check()
                    for target in combatList:
                        target.CountDown()
                    break
                elif action == "Attack":
                    print("\nYou have hit the Pirate")
                    combatList[choice-1].ChangeHP(Player1.attack)
                    for target in combatList:
                        #print("counting down")
                        target.CountDown()
                        #print(target.attackTimer)
                    break
                elif action == "Back":
                    break
                else:
                    print("Invalid action")
        else:
            print("\nPlease choose one of the listed numbers")
        for target in combatList:
            if target.hp <= 0:
                combatList.remove(target)
                #print(combatList)
                #print(enemyDict)
        for target in combatList:
            if target.attackTimer == target.attackCooldown:
                print(f"\nYou have been attacked by {str(target)}")
                Player1.ChangeHP(target.attack)
                target.attackTimer = 0
            #print(target.attackTimer)
        if Player1.hp <= 0:
            break
        if len(combatList) == 0:
            break


def mainMenu():
    """
    Main menu
    allows player to choose options and run code
    """
    while not Player1.hasTreasure:
        playerLocation = map.islandMap[Player1.posY][Player1.posX]
        print(playerLocation.description)
        #if you are in trap room
        if ("Trap" in str(playerLocation) and 
            not playerLocation.actions["Disable trap"]):
            print("You take damage from the spikes!")
            Player1.ChangeHP(-1)
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
                        Player1.Move()
                    else:
                        print("The pirates are blocking your way!")
                else:
                    print("Okay!\n")
                    Player1.Move()
            #if it is a valid action and the action is not completed yet
            elif (choice in playerLocation.actions and 
                  not playerLocation.actions[choice]):
                encounterActions(choice, playerLocation)
            #heals by 1 when using a coconut
            elif Player1.coconuts > 0 and choice == "Use a coconut":
                Player1.coconuts -= 1
                Player1.ChangeHP(1)
            elif choice == "Check status":
                Player1.PrintStatus()
            elif choice == "Inventory":
                Player1.PrintInv()
            elif choice == "Map":
                map.viewMap()
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
map.mapExport()
mainMenu()