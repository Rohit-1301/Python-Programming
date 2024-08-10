import random
 
computer_guess = random.randint(1,100)
guesses=0;

yourchoice = int(input("Enter your choice between 1 to 100: "))
while(yourchoice != computer_guess):
    if(yourchoice > computer_guess):
        print("Your choice is too high")
        guesses = guesses + 1
        yourchoice = int(input("Enter your choice between 1 to 100: "))
    else:
        print("Your choice is too low")
        guesses = guesses + 1
        yourchoice = int(input("Enter your choice between 1 to 100: "))

print("Congratulations you guessed it right")
print("Computer choice was: ",computer_guess)
print("You guessed it in:",guesses," guesses")
