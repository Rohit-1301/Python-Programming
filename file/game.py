import os
import random
def game():
    file=file_path = r"C:\Users\rg975\OneDrive\Desktop\python programming\file\game.txt"
    print("Hello, welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    score = random.randint(1, 100)
   
   
    with open(file) as f:
        hiscore=f.read()
        if hiscore!="":
            hiscore=int(hiscore)
        else:
            hiscore=0

    print("Your score is",score)
    if score>hiscore:
           with open(file, "w") as f:
            f.write(str(score))
        
    return score
    
game()