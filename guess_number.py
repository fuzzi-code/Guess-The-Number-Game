import random

# we guessing the computer's number


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input('Guess the number: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print('Yay! You guess the number!')


guess(10)

# computer guessing our number


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # can also be high as low=high
        feedback = input(
            f"Is {guess} too high(H) or too low(L), or correct(C) ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print('Yay! The computer guessed the correct number!!')


computer_guess(20)
