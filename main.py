import random

def guess(x):

    random_num = random.randint(1, x)
    guess = 0

    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_num:
            print("Too High! Guess Again")
        elif guess < random_num:
            print("Too low! Guess Again")

    print("WOOOO!, You got it....")

def computer_guess(x):

    low = 0
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        elif low == high:
            guess = low #could also be high b/c they are ==

        feedback = input(f"Is {guess} too high (H) oh too low (L). Is it correct (c): ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print("You guess my number right")

computer_guess(10000)      
