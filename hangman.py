import random
import re
from arr_of_symbols import *

# Open words.txt and read all its values
# that can be used for the hangman game.
with open('words.txt', 'r') as f:
    allText = f.read()
    # Split all the words a single [] value for the array 
    words = list(map(str, allText.split()))

# Loop through the array and pick one random value.
# The chosen random value will be the word to guess
secretWord = random.choice(words)

amountOfTurns = 9   # amounts of turns that the player have
guesses = []        # array field for guessed characters that the user fill in the input
done = False        # If false, the game will run, if true, the game will stop
guessesLeft = amountOfTurns

while not done:
    # Show the name of the game
    print('H A N G M A N')
    # At every wrong guess a symbol (drawing line) in the terminal appears
    # as how it goes in the original hangman game 
    print(hangman_arr[guessesLeft - amountOfTurns])
    for letter in secretWord:
        if letter.lower() in guesses:
            # If the guessed letter is in word, push the letter this in the 'array'
            print(letter, end=" ")
        else:
            # If the guessed letter in NOT in the word, the array remain '_'
            print("_", end=" ")
    # Every pushed element (letter) in the array (guesses) automatically adds an comma at the end
    print(guesses, end=", ")
    
    # Allow the user to fill in a value
    guess = input(f'\nPlayer has {amountOfTurns} turn(s) left, Next Guess: ')
    
    # Set up the regexp to find all char pattern from a-zA-Z, which is entered by the use
    letterIsValid = re.findall('[a-zA-Z]', guess)
    
    # Check if entered letter is valid
    if letterIsValid:
        # Check if letter is in secret word
        if guess not in secretWord.lower():
            print(f'The guessed \'{guess}\' value is not part of the word!')
        # Check if player has only given just one value
        # if false, send back a message that only one character is allowed and that 
        # the player has to try it again without costing a point
        if len(letterIsValid) > 1:
            print(f'\'{guess}\' is invalid! Only one alpha letter (a-z) is allowed for each turn. Try again!')
            amountOfTurns += 1
        # check if input is empty
    else:
        # Sends back a message that the input is invalid.
        print(f'\'{guess}\' is invalid! Only alpha letters (a-z) are allowed. Try again!')
        amountOfTurns += 1
    # Append the valid value to the series (array) of guesses  
    guesses.append(guess.lower())
        
    # If use does not enter a value in the input, the counter of amountOfTurns will not go up.
    if guess == '':
        amountOfTurns -= 1
     
    # If the guessed letter is not in the word, the turns will be decreased
    if guess.lower() not in secretWord.lower():
        amountOfTurns -= 1
        # If amountOfTurns reached 0, the game will stop
        if amountOfTurns < 1:
            break

    done = True

    for letter in secretWord:
        if letter.lower() not in guesses:
            done = False

# If the player guessed all the letters before the amountOfTurns reached 0, the player has won.         
if done:
    print(f'You Won! The word was \'{secretWord}\'')
else:
    # If the player dit NOT guessed all the letters AND the amountOfTurns reached 0, the player will lose.
    # The last hangman image will appear as well
    print(f'\nGame over, you lost! The word was \'{secretWord}\'\n{hangman_arr[-1]}')
