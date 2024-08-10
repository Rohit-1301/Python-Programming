import random

# Initialize scores
yourscore = 0
computerscore = 0

# Run the game logic 10 times
for i in range(10):
    # Simulate the choices (1 = Rock, 2 = Paper, 3 = Scissors)
    you = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
    computer = random.randint(1, 3)
    
    # Print the choices for each round (optional)
    print(f"Round {i+1}: You chose {you}, Computer chose {computer}")

    # Game logic to update scores
    if you == 1 and computer == 2:
        computerscore += 1
    elif you == 1 and computer == 3:
        yourscore += 1
    elif you == 2 and computer == 3:
        computerscore += 1
    elif you == 2 and computer == 1:
        yourscore += 1
    elif you == 3 and computer == 1:
        computerscore += 1
    elif you == 3 and computer == 2:
        yourscore += 1
    elif you == computer:
        pass  # No score change on a tie

# Print final scores
print(f"Your score: {yourscore}")
print(f"Computer's score: {computerscore}")



       