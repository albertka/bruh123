import random
import sys



def main():
    
    choose = input("Welcome to rock paper scissors. Choose rock,paper or scissors(r/p/s): ")
    
    
    
    randomchoose = ai_guess(choose)
    checkWin(choose, randomchoose)


def ai_guess(choose):
    
    options = ['r','p','s']
    randomChoose = random.choice(options)
    return randomChoose
    
    
    
def checkWin(choose, randomChoose):
    
    if (choose==randomChoose):
        print ("Players have tied. ")               
    elif choose == "r" and randomChoose == 'p':
        print ("You LOSE.")
    elif choose == "p" and randomChoose == 'r':
        print ("You Won!")
    elif choose == "r" and randomChoose == 's':
        print ("You Won!")
    elif choose == "s" and  randomChoose == 'r':
        print ("You LOSE.") 
    elif choose == "p" and randomChoose == 's':
        print ("You LOSE.")
    elif choose == "s" and randomChoose == 'p':
        print ("You Won!")
    
    
    
if __name__ == "__main__":
    main()