import random 

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_num:
            print("Too high")
        else: print("Too low")
    print("Congrats! You guessed they right number!")

def computer_guess(x): 
    low = 1 
    high = x 
    feedback = ''  
    while feedback != 'c': 
        if low != high: 
            guess = random.randint(low,high)
        else: 
            guess = low # could also be high, doesnt matter. 
        feedback = input(f"Is {guess} too hight (H), to low (L), or correct (C)? ").lower()
        if feedback == 'h': 
            high = guess - 1 
        elif feedback == 'l': 
            low = guess + 1  

print(f"Nice the computer got {guess}...whorray...") 

computer_guess(10)
        