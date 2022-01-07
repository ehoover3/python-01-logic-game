"""A logic game where user guesses a number based on clues."""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Hot, Warm, Cold, a logic game.

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are clues:

When I say:    That means:
  Hot           One digit is correct and in the right position.
  Warm          One digit is correct but in the wrong position.
  Cold          No digit is correct.

Example: if the secret number was 248 and you guessed 843, 
the clue would be Warm Hot.'''.format(NUM_DIGITS))

    while True:  # Main game loop.
        secretNum = getSecretNum()  # Get a new secret number
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:  # Loop until user wins or reaches max guesses
            guess = ''
            # Loop until user enters valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # User won, so end this loop
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        # Ask user to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')  # Create list of digits 0 to 9
    random.shuffle(numbers)  # Shuffle list into random order

    # Get first NUM_DIGITS digits in list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Return string with hot, cold, or warm clues."""
    # If win...
    if guess == secretNum:
        return 'You got it!'
    # Else give a clue
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Hot')  # A correct digit is in the correct place
        elif guess[i] in secretNum:
            clues.append('Warm')  # A correct digit is in the incorrect place
    if len(clues) == 0:
        return 'Cold'  # There are no correct digits at all
    else:
        clues.sort()  # Sort clues into alphabetical order to give away info
        return ' '.join(clues)  # Convert clues list to string


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
