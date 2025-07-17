#Variables

secret_word = "Giraffe"
guess = ""
tries = 0
tries_limit = 3
out_of_guesses = False

#prompt user

while guess != secret_word and not out_of_guesses:
    if tries < tries_limit:
        guess = input("Enter first guess: ")
        tries +=1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")


