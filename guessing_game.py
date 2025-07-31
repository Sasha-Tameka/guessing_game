import random
#Variables

secret_word = "giraffe"
tries = 0
tries_limit = 3
out_of_guesses = False
guess_correctly = False

#prompt user

while not guess_correctly and not out_of_guesses:
    if tries < tries_limit:
        guess = input("Enter first guess: ").lower()
        if guess == secret_word:
            guess_correctly = True
            break
        guess_2 = input("Enter second guess: ").lower()
        guess_3 = input("Enter last guess: ").lower()
        tries +=1
        if secret_word in [guess, guess_2,guess_3]:
            guess_correctly= True
    else:
        out_of_guesses = True
if guess_correctly:
    print("You win!")
else:
    print("Out of Guesses, YOU LOSE!")


