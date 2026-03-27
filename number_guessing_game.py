import random

num_to_guess_from = int(input("Enter number to guess from: "))
num_to_guess_to = int(input("Enter number to guess to: "))
print(f"Guess the number by entering a guess from {num_to_guess_from} to {num_to_guess_to}!")
num_to_guess = random.randint(num_to_guess_from, num_to_guess_to)
no_tries_wanted = int(input("Enter number of tries wanted: "))
print(f"You should guess the number in under {no_tries_wanted} tries,or else you will lose!")
no_user_guess = 0

while True:
        user_guess = int(input("Enter your guess: "))

        if user_guess == num_to_guess:
                print("You Guessed the Correct Number!")
                break

        no_user_guess += 1
        if user_guess >  num_to_guess:
                print("Too high!")
        elif user_guess <  num_to_guess:
                print("Too low!")
                
        if no_user_guess == no_tries_wanted:
                print("You have guessed too many times!")
                print(f"The number was {num_to_guess}")
                break
