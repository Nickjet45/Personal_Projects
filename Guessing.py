import random


def guess_Number():
    guessed_number = -1
    hidden_number = random.randint(0, 100)
    current_guesses = 0
    print("I'm thinking of a number between 0 and 100 please guess it...")

    while guessed_number is not hidden_number:
        current_guesses = current_guesses + 1
        guessed_number = int(input('Please guess the number '))
        if guessed_number > hidden_number:
            print('The number is lower please guess again')
        elif guessed_number < hidden_number:
            print('The number is higher please guess again')
        elif guessed_number == hidden_number:
            print('You have correctly guessed the number which was {}'.format(hidden_number))
            print('It took you {} guesses'.format(current_guesses))
            break


def roll_Dice():
    response = input('Would you like to roll the dice?[Y/N] ')
    if 'y' or 'Y' in response:
        while True:
            number_of_sides = int(input('How many sides would you like for the dice to have? '))
            rolled_number = random.randint(1, number_of_sides)
            print('You rolled {}'.format(rolled_number))
            new_response = input('Would you like to roll again?[y/n] ')
            if 'y' in new_response:
                print('Restarting program...')
            elif 'Y' in new_response:
                print('Restarting program')
            elif 'N' in new_response:
                print('Cancelling program...')
                break
            elif 'n' in new_response:
                print('Cancelling program....')
                break

    elif 'n' or 'N' in response:
        print('Cancelling program....')


