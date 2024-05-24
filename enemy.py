###############################################################################
# Enemy Module
###############################################################################
class Enemy():
    def __init__(self, posX, posY, hp, attack, attackCooldown, attackTimer):
        '''
        posX: the x position of the enemy
        posY: the y position of the enemy
        hp: the health of the enemy
        attack: the attack of the enemy
        attackCooldown: the number of turns it takes for the player to attack
        attackTimer: allows for enemies to have the same cooldown but 
        staggers attacks
        '''
        self.posX = posX
        self.posY = posY
        self.hp = hp
        self.attack = -attack
        self.attackCooldown = attackCooldown
        self.attackTimer = attackTimer

    
    def ChangeHP(self, amountToChange):
        """changes the enemie's hp"""
        self.hp += amountToChange
        print(f"They have {self.hp} hp left")

    
    def CountDown(self):
        '''let enemy timer go up'''
        self.attackTimer += 1


class Pirate(Enemy):
    def __str__(self):
        return("Pirate")

    
    def Check(self):
        '''checks the pirate'''
        print(f"hp: {self.hp}")
        print(f"attack: {-self.attack}")

