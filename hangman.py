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
    print(guesses)  
    
    guess = input(f'Player has {amountOfTurns} turn(s) left, Next Guess: ')
    guesses.append(guess.lower())
    
    if guess.lower() not in secretWord.lower():
        amountOfTurns -= 1
        if amountOfTurns == 0:
            break

    done = True
    for letter in secretWord: 
        if letter.lower() not in guesses:
            done = False
            
if done:
    print(f'You found the word! It was {secretWord}')
else: 
    print(f'Game Over, you lose! The word was {secretWord}')