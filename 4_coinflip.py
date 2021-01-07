# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list
# of heads and tails. Your program breaks up the experiment into two parts:
# the first part generates a list of randomly selected 'heads' and 'tails' values,
# and the second part checks if there is a streak in it.
# Put all of this code in a loop that repeats the experiment 10,000 times so we can find out
# what percentage of the coin flips contains a streak of six heads or tails in a row.
# As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.

import random #import this module so we can use random.randint()
numberOfStreaks = 0
counterH = 0 # CounterH is for heads
counterT = 0 # CounterT is for tails
for experimentNumber in range(10000): #
    headsOrtails = [] # Initialize an empty list within the for loop so that every iteration starts with empty list
    # Part 1: Code that creates a list of 100 'heads' or 'tails' values.
    for CoinFlip in range(100): # for loop will iterate up to range of 100
        randomNumber = random.randint(0,1) # flips the coin
        if randomNumber == 0: # Assigns 0 to heads
            result = 'H'
            headsOrtails.append(result) # Appends result to headsOrtails list

        if randomNumber == 1: # Assigns 1 to tails
            result = 'T'
            headsOrtails.append(result) # Appends result to headsOrtails list

    # Part 2: Code that checks if there is a streak of 6 heads or tails in a row.
    for CoinFlip in range(len(headsOrtails)): # for loop will iterate through length of the headsOrtails list
        if headsOrtails[CoinFlip] == 'H': # Inspect headsOrtails list with Coinflip as the index.
            counterH += 1 # Add 1 to counterH if result is heads
            counterT = 0 # Reset counterT to 0 if result is heads. This means streak for tails is broken.
        if counterH == 6: # If counterH has reached six, it means that there have been 6 consecutive results for heads.
            numberOfStreaks += 1 # Add 1 to numberOfStreaks counter.
            counterH = 0 # Reset counterH, streak is over.
            break
        if headsOrtails[CoinFlip] == 'T': # Inspect headsOrtails list with Coinflip as the index.
            counterT += 1 # Add 1 to counterT if result is tails
            counterH = 0 # Reset counterH to 0 if result is tails. This means streak for heads is broken.
        if counterT == 6: # If counterT has reached six, it means that there have been 6 consecutive results for tails.
            numberOfStreaks += 1 # Add 1 to numberOfStreaks counter.
            counterT = 0 # Reset counterH, streak is over.
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
