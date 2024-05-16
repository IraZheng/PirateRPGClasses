###############################################################################
# Enemy Module
###############################################################################
class Enemy():
    def __init__(self, posX, posY, hp, attack, attackCooldown, attackTimer):
        self.posX = posX
        self.posY = posY
        self.hp = hp
        self.attack = -attack
        self.attackCooldown = attackCooldown
        self.attackTimer = attackTimer

    def ChangeHP(self, amountToChange):
        self.hp += amountToChange
        print(f"They have {self.hp} hp left")

    def CountDown(self):
        self.attackTimer += 1

class Pirate(Enemy):
    def __str__(self):
        return("Pirate")

    def Check(self):
        print(f"hp: {self.hp}")
        print(f"attack: {self.attack}")

