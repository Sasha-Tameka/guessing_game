import random

# Variables
secret_word = "giraffe"  # lowercase for consistent comparison
tries = 0
tries_limit = 3
out_of_guesses = False
guess_correctly = False
hint_1 = "Hint: it's an animal"
hint_2 = "Hint: It has 7 letters"

#Validation FUnction
def get_valid_guess(prompt):
    while True:
        guess = input(prompt).lower().strip()

        if not guess:
            print("Please enter a word")
            continue
        if not guess.isalpha():
            print("Enter only letters")
            continue
        if len(guess)<2:
            print("Word must be at least 2 letters!")
            continue
        return guess

# Letter Feedback Function
def get_letter_feedback(guess, secret_word):
    feedback = []
    secret_letter = list(secret_word)


# Game Loop
while not guess_correctly and not out_of_guesses:
    tries += 1
    guess = get_valid_guess(f"Enter guess #{tries}: ").lower().strip()
    if tries == 1:
        print(hint_1)
    elif tries == 2:
        print(hint_2)

    if guess == secret_word:
        guess_correctly = True
    elif tries >= tries_limit:
        out_of_guesses = True

# Result
if guess_correctly:
    print("You win!")
else:
    print("Out of Guesses, YOU LOSE!")


