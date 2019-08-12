import random

def main():

    answer = random.randint(1,10)

    input("Welcome to the random number guessing game! Please select your difficulty. Easy, Medium, or Hard. ")

    tries=4    
    while (tries>0):
    
        guess = int(input("Guess a number between 1 and 10: "))
        
        if (answer == guess):
            print("You win! ")
            
            break
        elif (guess>answer):
            print ("Guess is too big. ")
            tries=tries-1
            print ("You have " + str(tries) +" tries left.")            
            
        elif (guess<answer):
            print ("Guess is too small.")
            tries=tries-1
            print ("You have " + str(tries) +" tries left.")            
            
        elif tries==1:
    
            print ("You Lose "+ str(answer) + " was the correct number.")
            
            break
            

if __name__ == "__main__":
    main()
