import random
import sys

def main():
    
    randomNum=random.randint(0,4)
    bob = ["Wedenesday", "Albert", "Computer", "Science", "Python", "Hangman"]
    word = bob[randomNum]
    word=word.lower()
    print ("The amount of letters in your word is "+str(len(word))+ "."+(" You have 5 lives remaining."))
    inputt = input("Guess your letter: ")

letter = ["A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letter = letter.lower
def checkWin(guessed_letters, selected_word):
    if word == ("Wedenesday"):
        ["", ] = True
    elif word == ("Albert"):
        
    elif word == ("Computer"):
        
    elif word == ("Science"):
        
    elif word == ("Hangman"):
        
    else:
        

if __name__ == "__main__":
    main()
