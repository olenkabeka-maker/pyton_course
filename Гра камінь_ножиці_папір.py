import random
print("Let's play rock, paper, scissors")
player = input("Choose rock, paper, or scissors by typing r, p, s:")
if player == 'r' or player == 'p' or player == 's':
    computer = (random.randint(1, 3))
    if (computer == 1 and player == 'r' or computer == 2 and player == 'p' or computer == 3 and player == 's'):
        print("It's a draw")
    elif (computer == 1 and player == 'p' or computer == 2 and player == 's' or computer == 3 and player == 'r'):
        print("Congradulations! You win!")
else:
    print("Your input was in the format, no game for you")
