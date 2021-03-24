
"""
Guess the number!

Created on Aug 11, 2020
@author: Sahand-j
Refrences Automate the Boring stuff with Python Book example
"""

import random

print('Hello, what is your name?')
name = input()
print('Hi '+str(name) + ', im thinking of a number between 1 and 20, what am thinking?')

def guessTheNumber():
    """
    Main method for guessing the number game
    :@return(none): prints output messages based on users choice 
    """
    secretNumber = random.randint(1,20) # randomly generated number 
    try:
        
        for numberOfGuesses in range(1,7): # user gets 6 tries
            
            guess = int(input())
            if guess < secretNumber:
                print('Your guess is too LOW, Take another guess')

            elif guess > secretNumber:
                print('Your guess is too HIGH, Take another guess')
            
            else:
                break #is the correct guess
        
        if guess == secretNumber:
            print('Good job '+name+' it took you '+ str(numberOfGuesses) +' tries.')
        
        else:
            print('Nope, the number i was thinking of was '+ str(secretNumber))
    
    except:
        print('please enter a valid number!')
        guessTheNumber()

guessTheNumber() # start of program

