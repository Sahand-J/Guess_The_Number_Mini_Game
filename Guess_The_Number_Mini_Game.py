#guess the number program

import random

print('Hello, what is your name?')
name = input()
print('Hi '+str(name) + ', im thinking of a number between 1 and 20, what am thinking?')
def guessTheNumber():
    secretNumber = random.randint(1,20)
    try:
        for numberOfGuesses in range(1,7):
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
guessTheNumber()

