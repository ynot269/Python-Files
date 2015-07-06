import random

class Character:
    def __init__(self):
        self.name = str(input("Enter a name: "))
        self.mp = int(input("How much MP does this character have: "))
        self.hp = int(input("How much HP does this character have: "))
        self.atk = int(input("How much attack does this character have: "))
        self.defense = int(input("How much defense does this character have: "))

class GameMech:
    def __init__(self, aCharacter, target):
        print("A battle is starting")
    def getMP(self, aCharacter):
        return aCharacter.mp
    def getHP(self, aCharacter):
        return aCharacter.hp
    def getAtk(self, aCharacter):
        return aCharacter.atk
    def getDef(self, aCharacter):
        return aCharacter.defense
    def getName(self, aCharacter):
        return aCharacter.name
    def usePotion(self, aCharacter):
        aCharacter.hp += aCharacter.hp/10
        return aCharacter.hp/10
    def useSpecial(self, aCharacter, target):
        if aCharacter.mp >= aCharacter.mp/3:
            target.hp -= aCharacter.atk*2.5
            if target.hp - aCharacter.atk <= 0:
                print(aCharacter.name, "is using a special move!!!!!")
                print(target.name, "was attacked for", (aCharacter.atk*2.5), "points of damage.")
                self.dead(target)
                aCharacter.mp -= aCharacter.mp/3
            else:
                print(aCharacter.name, "is using a special move!!!!!")
                print(target.name, "was attacked for", (aCharacter.atk*2.5), "points of damage.")
                aCharacter.mp -= aCharacter.mp/3
        else:
            print("You do not have enough MP to use this move!")
    def dead(self, aCharacter):
        return aCharacter.name +" is now dead"
    def attack(self, aCharacter, target):
        if target.hp - aCharacter.atk <= 0:
            print(self.getName(target), "was attacked for", aCharacter.atk, "points of damage.")
            self.dead(target)
        else:
            print(self.getName(target), "was attacked for", aCharacter.atk, "points of damage.")
            target.hp = target.hp - aCharacter.atk

    def guard(self, aCharacter, target):
        if aCharacter.defense > target.atk:
            print(aCharacter.name + " was unharmed")
            if aCharacter.hp <= aCharacter.hp/2:
                self.retaliation(aCharacter, target)
        else:
            aCharacter.hp = aCharacter.hp -(target.atk - aCharacter.defense)
    def retaliation(self ,aCharacter, target):
        print(aCharacter.getName, " retaliated!")
        self.attack(aCharacter, target)
        
        if target.hp - aCharacter.atk <= 0:
            self.dead(target)
        else:
            target.hp = target.hp - aCharacter.atk

        
        
    def battleMenu(self, aNumber, aCharacter, target):
        if aNumber == 1:
            self.attack(aCharacter, target)
            

        if aNumber == 2:
            self.guard(aCharacter, target)
            
        if aNumber == 3:
            self.useSpecial(aCharacter, target)
            

        if aNumber == 4:
            heal = self.usePotion(aCharacter)
            print(aCharacter.name, "is using a potion")
            print(aCharacter.name,'healed for', heal, "health points!")

            

    def myTurn(self):
        print("1 = ATTACK")
        print("2 = GUARD")
        print("3 = SPECIAL")
        print("4 = POTION")

        aNumber = int(input("What would you like to do? "))
        return aNumber

    def oppTurn(self):
        print("It is the opponent's turn")
        randomNum = random.randint(1,4)
        return randomNum

    def charMenu(self, aCharacter):
        return ("Name:" + self.getName(aCharacter)+
        " HP: " + str(self.getHP(aCharacter))+ 
        " MP: " + str(format(self.getMP(aCharacter),'.0f')) +
        " Attack: " + str(self.getAtk(aCharacter))+
        " Defense: " + str(self.getDef(aCharacter)))      
