# Import packages
import random

# Define variables
word_list = ['cat', 'computers', 'mouse', 'dice', 'python', 'hippocampus', 'divinely', 'television', 'android', 'procedurally']
wrong_guessed_letters = []
right_guessed_letters = []
selected_word = ''
unique_letters = set()
random_selector = -1
progress = ''
quit = 0
head_space = '   '
torso_space = '   '
leg_space = '   '

#############
# Functions #
#############

# Initial game setup with word selection
def game_setup():
    global selected_word
    random_selector = random.randint(0, 9)
    selected_word = word_list[random_selector]
    for i in selected_word:
        unique_letters.add(i)
    print('There are ' + str(len(selected_word)) + ' letters in the word.')

# Print statements that run every turn
def turn_print():
    global progress
    print()
    print('You have made ' + str(len(right_guessed_letters) + len(wrong_guessed_letters)) + ' guesses.')
    print('You have made ' + str(len(right_guessed_letters)) + ' correct guesses.')
    print('You have made ' + str(len(wrong_guessed_letters)) + ' incorrect guesses.')
    print('You have guessed the following incorrect letters: ' + str(wrong_guessed_letters))
    print_gallows()
    print()
    # Displays correct guesses and unguessed characters formatted as the word
    progress = ''
    for i in selected_word:
        if i in right_guessed_letters:
            progress += i
        else:
            progress += '-'
    print(progress)

# Prints the gallows and person being hanged
def print_gallows():
    global head_space, torso_space, leg_space
    # Creates the appropriate number of body parts for display
    if len(wrong_guessed_letters) >= 1:
        head_space = ' o '
        if len(wrong_guessed_letters) >= 2:
            if len(wrong_guessed_letters) == 2:
                torso_space = ' | '
            elif len(wrong_guessed_letters) == 3:
                torso_space = '/| '
            else:
                torso_space = '/|\\'
            
            if len(wrong_guessed_letters) >= 5:
                leg_space = '/  '
                if len(wrong_guessed_letters) >= 6:
                    leg_space = '/ \\'

    print('______')
    print(' |   |')
    print(head_space + '  |')
    print(torso_space + '  |')
    print(leg_space + '  |')
    print('_____|___')

# Sets all variables back to their default values
def clear_variables():
    global wrong_guessed_letters, right_guessed_letters, selected_word, unique_letters, random_selector, progress, head_space, torso_space, leg_space
    wrong_guessed_letters = []
    right_guessed_letters = []
    selected_word = ''
    unique_letters = set()
    random_selector = -1
    progress = ''
    head_space = '   '
    torso_space = '   '
    leg_space = '   '

# Prints and handles all end of game logic
def end_game_print():
    global quit
    # Print the final word along with congratulations and final guesses
    print(selected_word)
    print('You guessed the word! It took you ' + str(len(right_guessed_letters) + len(wrong_guessed_letters)) + ' guesses.')
    # Take user input to quit or continue
    user_input = input('Would you like to play again? [Y] or [N]')
    user_input.lower()
    if user_input == 'n':
        print('Thanks for playing!')
        quit = 1
    else:
        clear_variables()


################
# Main Program #
################

def main():
    print('Welcome to Hang Man!')

    # Run until the user quits
    while (quit != 1):
        game_setup()

        # Runs until all letters are guessed
        while len(unique_letters) > len(right_guessed_letters):
            turn_print()

            # Takes user input and makes it lowercase
            user_input = input('Guess a letter: ')
            user_input.lower()

            # Checks if user_input is new or repeated
            if user_input not in right_guessed_letters and user_input not in wrong_guessed_letters:
                # Checks if user_input is correct or not
                if user_input in unique_letters:
                    right_guessed_letters.append(user_input)
                else:
                    wrong_guessed_letters.append(user_input)
                    print(user_input + ' is not in the word.')
            else:
                print('You already guessed that letter!')
        
        # Prints final number of guesses and gives quit option after the word has been guessed
        end_game_print()

if __name__ == '__main__':
    main()
