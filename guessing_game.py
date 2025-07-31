import random

# Variables
secret_word = "giraffe"  # lowercase for consistent comparison
tries = 0
tries_limit = 3
out_of_guesses = False
guess_correctly = False

# Prompt user
while not guess_correctly and not out_of_guesses:
    tries += 1
    guess = input(f"Enter first guess #{tries}: ").lower()

    if guess == secret_word:
        guess_correctly = True
    elif tries >= tries_limit:
        out_of_guesses = True

# Result
if guess_correctly:
    print("You win!")
else:
    print("Out of Guesses, YOU LOSE!")


