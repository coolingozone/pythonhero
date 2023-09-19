# Solution:
import random

secret_number = random.randint(1, 100)
guessed = False

while not guessed:
    guess = int(input("Guess the secret number (between 1 and 100): "))
    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        guessed = True
    elif guess < secret_number:
        print("Try higher.")
    else:
        print("Try lower.")
