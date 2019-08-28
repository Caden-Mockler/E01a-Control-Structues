#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') # Displays the wording in paranthesis
colors = ['red','orange','yellow','green','blue','violet','purple'] # Lists available answers to be randomized between
play_again = '' # Gives the options to play again
best_count = sys.maxsize            # the biggest number #the number represented cant be larger that number of colors shown
while (play_again != 'n' and play_again != 'no'): # Establishes answer n meaning no, to not play again
    match_color = random.choice(colors) # Makes the color to match be random
    count = 0 #Count begins at 0
    color = '' # Creates path for answer to correspond with option
    while (color != match_color): # Path to choosing correct color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line #Dislays text after guess
        color = color.lower().strip() #Ignores spacing and capitalization
        count += 1 # Inrease counts by 1
        if (color == match_color): # Path for if the color guessed is correct
            print('Correct!') # Text displayed is color is correct
        else: # Alternate path
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #Displays text and number of guesses, when wrong
    print('\nYou guessed it in {0} tries!'.format(count)) #Text displayed is chosen correctly along with number of guesses it took
    if (count < best_count): #Compares current count to best attempt
        print('This was your best guess so far!') # Text if this was the least number of guesses it took
        best_count = count # Path to display if least number of guesses so far
    play_again = input("\nWould you like to play again? ").lower().strip() # Text giving option to replay program
print('Thanks for playing!') # Text for is the player chooses to quit