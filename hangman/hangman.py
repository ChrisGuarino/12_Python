import random
import string 
from words import words 

def get_valid_word(words): 
    word = random.choice(words) 
    while '-' or ' ' in words: 
        word = random.choice(words)
    
    return word 

def hangman(): 
    word = get_valid_word(words)
    word_letters = set(word) #cast word letters to a set. 
    alphabet = set(string.ascii_uppercase) #pre-existing library
    used_letters = set() #Already guessed letters

    user_letter = input('Guess a letter: ').upper() 
    if user_letter in alphabet - used_letters: 
        used_letters.add(user_letter)
        if user_letter in word_letters: 
            word_letters.remove(user_letter)


user_input = input("Type something...")
print(user_input)
