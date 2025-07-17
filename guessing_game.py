#Variables

secret_word = "Giraffe"
guess = ""
tries = 0
tries_limit = 3
out_of_guesses = False

#prompt user

while guess != secret_word:
    guess = input("Enter first guess: ")
    tries +=1
print("You win!")


