# This is a guess the number game.

import random # imports random module
secretNumber = random.randint(1,20) #sets a variable named secretNumber, which is equal to a random number generated between 1 to 20.
print("I am thinking of a number between 1 and 20.") # informs user of the range of numbers.

# Ask the player to guess 6 times.
for guessesTaken in range (1,7): # for loop is used. user has 6 chances to guess
    print("Take a guess.") # prints "Take a guess."
    guess = int(input()) # user's input is stored in variable named guess.

    if guess < secretNumber: # sets condition. if guess is less than secretNumber, then next line is executed.
        print("Your guess is too low.")
    elif guess > secretNumber: # sets condition. if guess is greater than secretNumber, then next line is executed.
        print("Your guess is too high.")
    else:
        break # This condition is the correct guess!

if guess == secretNumber: # this is a new block. Next line is executed if user correctly guesses the number.
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else: # Next line is executed if user did not guess.
    print("Nope. The number I was thinking of was " + str(secretNumber))
