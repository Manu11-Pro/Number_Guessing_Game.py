import random

num_to_guess_from = int(input("Enter number to guess from: "))
num_to_guess_to = int(input("Enter number to guess to: "))
print(f"Enter a guess from {num_to_guess_from} to {num_to_guess_to}")
num_to_guess = random.randint(num_to_guess_from, num_to_guess_to)
no_tries_wanted = int(input("Enter number of tries wanted: "))
no_user_guess = 0

while True:
        user_guess = int(input("Enter your guess: "))

        if user_guess == num_to_guess:
                print("You Guessed the Correct Number!")
                break
        elif user_guess >  num_to_guess:
                print("Too high")
                no_user_guess += 1
        elif user_guess <  num_to_guess:
                print("Too low!")
                no_user_guess += 1
        if no_user_guess == no_tries_wanted:
                print("You have guessed too many times!")
                print(f"The number was {num_to_guess}")
                break
