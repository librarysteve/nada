#!/usr/bin/python3
import random
from pyfiglet import Figlet

NUM_DIGITS = 3
MAX_GUESSES = 11

def main():
    print(makeBanner('NADA!'))
    print('''NADA is a deductive logic game
I'm thinking of a {} digit number with no repeated digits.
Try to guess it!
--------------------------------------------------------------
1Correct 	means one digit is correct and in the correct position.
1Off	 	means one is correct but not in the right place.
Nada	 	means none are correct.'''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print('Okay I have my number\nTry to guess it in {} guesses!'.format(MAX_GUESSES))
#        print('It might be:{}?'.format(secretNum))
        numGuesses = 1

        while numGuesses <= MAX_GUESSES:
            guess = ''

            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess number {}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break

            if numGuesses > MAX_GUESSES:
                print('Out of guesses!')
                print('The number was {}'.format(secretNum))

        print('play again? yes/no')

        if not input('> ').lower().startswith('y'):
            break

    print(makeBanner('Toodles!'))

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''

    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'you got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('1Correct')
        elif guess[i] in secretNum:
            clues.append('1Off')

    if len(clues) == 0:
        return 'Nada'
    else:
        clues.sort()
        return ' '.join(clues)

def makeBanner(title):
    a = Figlet(font='pagga')
    banner = a.renderText(title)
    return banner

if __name__ == '__main__':
    main()
