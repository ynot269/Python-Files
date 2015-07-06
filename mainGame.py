import random
import battle




#add buttons

    
        
def main():
#enter characters
    char1 = battle.Character()
    char2 = battle.Character()
    
    
#start the game    
    newGame = battle.GameMech(char1, char2)

#duration of game based on amount of HP
    turnCount = 0
#assign a check value for randNum because it hasn't been assigned in the below function
#until after it''s  used    
    randNum = 0
    while char1.hp > 0 and char2.hp > 0:
        print("Turn: ",turnCount)
#users turn 
        status = str(input("Would you like to check your stats? (Yes/No) "))
        if status == 'Yes':
            stat1 = newGame.charMenu(char1)
            stat2 = newGame.charMenu(char2)
            print(stat1 + "\n" + stat2)
        
        number = newGame.myTurn()
        
#due to the way this game is built, added a condition where the attacked character
#would heal the amount dealt because if the attack goes through first, and the opponent defends?
        if number == 2:
            if randNum == 1:
                newGame.guard(char1, char2)
                char1.hp += newGame.getAtk(char2) - newGame.getDef(char1)
                
            elif randNum == 3:
                newGame.guard(char1, char2)
                char1.hp += newGame.getAtk(char2) * 2.5 - newGame.getDef(char1)
        newGame.battleMenu(number, char1, char2)       

#opponents turn based on a random number generated between 1-4
        randNum = newGame.oppTurn()
        print(randNum)
        
        if randNum == 2:
            if number == 1:
                newGame.guard(char2, char1)
                char2.hp += newGame.getAtk(char1) - newGame.getDef(char2) 
            elif number ==3:
                newGame.guard(char2, char1)
                char2.hp += (newGame.getAtk(char1) * 2.5) - newGame.getDef(char2)
        newGame.battleMenu(randNum, char2, char1)
        
        if char1.hp <= 0:
            print(newGame.dead(char1))
            print("You lose")
            restart = str(input("Would you like to start over (Yes/No)"))
            if restart == "Yes":
                main()
        elif char2.hp <= 0:
            print(newGame.dead(char2))
            print("You win")
            restart = str(input("Would you like to start over (Yes/No)"))
            if restart == "Yes":
                main()
        turnCount+=1
        
        
main()

