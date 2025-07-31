import random
import time

#scoring variables
score = 0
games_played = 0
games_won = 0

# Variables
secret_word = " "
tries = 0
tries_limit = 3
out_of_guesses = False
guess_correctly = False


# Difficulty-based word lists
word_lists = {
    "easy": ["cat", "dog", "sun", "car", "book"],  # 3-4 letters
    "medium": ["apple", "piano", "garden", "bridge"],  # 5-6 letters
    "hard": ["elephant", "butterfly", "crocodile"]  # 7+ letters
}

#Let user choose difficulty (or pick randomly)
difficulty = input("Choose difficulty (easy/medium/hard) or Enter for random: ").lower()
if difficulty not in word_lists:
    difficulty = random.choice(list(word_lists.keys()))

secret_word = random.choice(word_lists[difficulty])
print(f"Playing on {difficulty} mode!")

hint_1 = f"Hint: it's a {difficulty} word"
hint_2 = f"Hint: It has {len(secret_word)} letters"

#scoring function
def calculate_score(tries_used,word_length,difficulty,time_taken):
    base_points = 100

    #points remaining for guesses
    guess_bonus = (4- tries_used) * 50

    #points for word difficulty
    difficulty_multiplier = {"easy" : 1.0, "medium" : 1.5, "hard": 2.0}
    difficulty_bonus = int(base_points * difficulty_multiplier.get(difficulty,1.0))

    #points for word length
    length_bonus = word_length * 10

    #time bonus
    time_bonus = max(0,60 - int(time_taken))*2



# Validation Function
def get_valid_guess(prompt):
    while True:
        guess = input(prompt).lower().strip()
        if not guess:
            print("Please enter a word")
            continue
        if not guess.isalpha():
            print("Enter only letters")
            continue
        if len(guess) < 2:
            print("Word must be at least 2 letters!")
            continue
        return guess


# Letter Feedback Function
def get_letter_feedback(guess, secret_word):
    feedback = []
    secret_letters = list(secret_word)

    # First pass: exact matches (Green)
    for i in range(len(guess)):
        if i < len(secret_word) and guess[i] == secret_word[i]:
            feedback.append('G')
            secret_letters[i] = None  # Mark as used
        else:
            feedback.append('?')  # Placeholder

    # Second pass: wrong position matches (Yellow)
    for i in range(len(guess)):
        if feedback[i] == '?':  # Not already green
            if guess[i] in secret_letters:
                feedback[i] = 'Y'
                secret_letters[secret_letters.index(guess[i])] = None
            else:
                feedback[i] = 'R'

    return feedback


def display_feedback(guess, feedback):
    print(f"Word: {guess.upper()}")
    colors = {'G': '🟩', 'Y': '🟨', 'R': '🟥'}
    print("".join(colors.get(f, '⬜') for f in feedback))

def introduction():
    print("")


# Game Loop
while not guess_correctly and not out_of_guesses:
    tries += 1

    # Show hints BEFORE asking for guess
    if tries == 1:
        print(hint_1)
    elif tries == 2:
        print(hint_2)

    # Get the guess
    guess = get_valid_guess(f"Enter guess #{tries}: ")

    # Check if correct
    if guess == secret_word:
        guess_correctly = True
    else:
        # Show feedback for wrong guesses
        feedback = get_letter_feedback(guess, secret_word)
        display_feedback(guess, feedback)

        # Check if out of tries
        if tries >= tries_limit:
            out_of_guesses = True

# Result
if guess_correctly:
    print("You win!")
else:
    print("Out of Guesses, YOU LOSE!")