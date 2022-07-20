import random
import string 
from words import words 

def get_valid_word(words): 
    word = random.choice(words) #Randomly chooses a word from the given list. 
    while '-' in word or ' ' in word: 
        word = random.choice(words)

    return word.upper()

def hangman(): 
    word = get_valid_word(words)
    word_letters = set(word) #cast word letters to a set. 
    alphabet = set(string.ascii_uppercase) #pre-existing library
    used_letters = set() #Already guessed letters
    lives = 6

    while len(word_letters) > 0 and lives > 0:

        print('You have used these letters: ', ' '.join(used_letters), f'\nYou have {lives} lives left.') #Used Letters
        word_list = [letter if letter in used_letters else '-' for letter in word]#Gives the user the word they are guessing
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper() 
        if user_letter in alphabet - used_letters: 
            used_letters.add(user_letter)
            if user_letter in word_letters: 
                word_letters.remove(user_letter)
            else: 
                lives -= 1 
                print('Letter is not in the word.')
        elif user_letter in used_letters: 
            print('You can\'t use that letter again.')
        else: 
            print('Not the character we are looking for.')
    if lives == 0: 
        print('You lost...bitch')
    else: print('Nice work you guessed the word!')

hangman()