import random
from art_new import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = 0
if difficulty == "easy":
    attempts = 10
    print(f"You have {attempts} remaining to guess the number.")
elif difficulty == "hard":
    attempts = 5
    print(f"You have {attempts} remaining to guess the number.")
else:
    print("Please enter a valid difficulty.")

numbers = []
for i in range(1, 101):
    numbers.append(i)

number_to_be_guessed = random.choice(numbers)
# print(number_to_be_guessed)



def ask_for_guess():
    guess = int(input("Make a guess: "))
    global attempts
    if guess == number_to_be_guessed:
        print("You guessed the number!!")
    elif guess < number_to_be_guessed and attempts > 0:
        print("Too low!")
        attempts -= 1
        print(f"You have {attempts} remaining to guess the number.")
        ask_for_guess()
    elif guess > number_to_be_guessed and attempts > 0:
        print("Too high!")
        attempts -= 1
        print(f"You have {attempts} remaining to guess the number.")
        ask_for_guess()
    elif attempts == 0:
        print("You are out of guesses")

ask_for_guess()
