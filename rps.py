import random
import sys



def main():
    
    choose = input("Welcome to rock paper scissors. Choose rock,paper or scissors(r/p/s): ")


def ai_guess():
    if choose == "p":
        choose = 1
    elif choose == "s":
    choose = 2 
    
    if (Choose==p):
        r=0
    elif (Choose==s):
        r=3
    else:
        r=0
        
    
    randomChoose = random.randint(0,2)
    if (randomChoose == 0):
        randomChoose = str(r)
        
    elif (randomChoose == 1):
        randomChoose = str(p)
    
    else:
        randomChoose =str(s)
    
    
def checkWin(randomChoose, Choose):
    if (randomChoose == Choose):
        print ("Players have tied. ")
    elif (randomeChoose < Choose):
        print ("You Won!!")
    else:
        print ("You Lost")
    
    
if __name__ == "__main__":
    main()