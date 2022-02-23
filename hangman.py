# import random word from txt
import random

with open('words.txt', 'r') as f:
    allText = f.read()
    words = list(map(str, allText.split()))
    
# set the random word ready for the hangman game
secretWord = random.choice(words)

amountOfTurns = 9
guesses = []
done = False



while not done:
    for letter in secretWord:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print(guesses, end=", ")  
    
    guess = input(f'Player has {amountOfTurns} turn(s) left, Next Guess: ')
    
    if guess.isalpha():
        guesses.append(guess.lower())
    else: 
        print(f'{guess} is invalid! Please, enter one valid character')
        amountOfTurns += 1    
        
    if len(guess) > 1:
        print('Please, enter one valid character')
        amountOfTurns += 1 
    
    if guess.lower() not in secretWord.lower():
        amountOfTurns -= 1
        if amountOfTurns == 0:
            break

    done = True
    for letter in secretWord: 
        if letter.lower() not in guesses:
            done = False
            
if done:
    print(f'You Won! The word was {secretWord}')
else: 
    print(f'Game Over, you lose! The word was {secretWord}')