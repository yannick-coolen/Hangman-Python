import random

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

while not done:
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
    guess = input(f'Player has {amountOfTurns} turn(s) left, Next Guess: ')

    # Check if value is an alpha letter (a-z)
    # if true the value is valid
    # else the letter will NOT be filled in and the player has to try again in the same turn
    if guess.isalpha():
        # Append valid value to array of guesses
        guesses.append(guess.lower())
        if guess not in secretWord.lower() and len(guess) == 1 :
            print(f'The guessed {guess} value is not part of the word!')

    else:
        # Sends back a message that the input is invalid.
        print(f'{guess} is invalid! Only alpha letters (a-z) are allowed. Try again!')
        amountOfTurns += 1

    # Check if player has only given just one value
    # if false, send back a message that only one character is allowed and that 
    # the player has to try it again in the same turn
    if len(guess) > 1:
        print('Invalid! Only one character (a-z) is allowed each turn. Try again!')
        amountOfTurns += 1

    # If the guessed letter is not in the word, the turns will be decreased
    if guess.lower() not in secretWord.lower():
        amountOfTurns -= 1
        # If amountOfTurns reached 0, the game will stop
        if amountOfTurns == 0:
            break

    done = True

    for letter in secretWord:
        if letter.lower() not in guesses:
            done = False

# If the player guessed all the letters before the amountOfTurns reached 0, the player has won.         
if done:
    print(f'You Won! The word was {secretWord}')
else:
    # If the player dit NOT guessed all the letters AND the amountOfTurns reached 0, the player will lose.         
    print(f'Game Over, you lose! The word was {secretWord}')
