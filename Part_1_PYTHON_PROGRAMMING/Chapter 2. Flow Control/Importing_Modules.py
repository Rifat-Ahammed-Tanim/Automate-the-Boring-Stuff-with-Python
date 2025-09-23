# from random import randint
# import random

# for i in range(5):
#     print(random.randint(1, 100))
    
    
# import sys
# while True:
#  print('Type exit to exit.')
#  response = input()
#  if response == 'exit':
#     sys.exit()
#  print('You typed ' + response + '.')

# This is a guess the number game.
# import random
# secretNumber = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')
# # Ask the player to guess 6 times.
# for guessesTaken in range(1, 7):
#  print('Take a guess.')
#  guess = int(input())
#  if guess < secretNumber:
#     print('Your guess is too low.')
#  elif guess > secretNumber:
#     print('Your guess is too high.')
#  else:
#     break # This condition is the correct guess!
# if guess == secretNumber:
#  print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
# else:
#  print('Nope. The number I was thinking of was ' + str(secretNumber))


import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:  # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    # Player input loop
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  # Quit the program.
        if playerMove in ['r', 'p', 's']:
            break
        print('Type one of r, p, s, or q.')

    # Display what the player chose
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Computer move
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    else:
        computerMove = 's'
        print('SCISSORS')

    # Decide winner
    if playerMove == computerMove:
        print('It is a tie!')
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1
