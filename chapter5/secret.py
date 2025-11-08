import random

secret = random.randint(1, 100)
min_value = 1
max_value = 100

while True:
    guess = int(input(f"Guess the secret number between {min_value} and {max_value}: "))

    if guess < min_value or guess > max_value:
        print(f"Please guess a number within the range {min_value} to {max_value}.")
        continue

    if guess < secret:
        print("Too low!")
        min_value = guess + 1
    elif guess > secret:
        print("Too high!")
        max_value = guess - 1
    else:
        print("Congratulations! You've guessed the secret number.")
        break
