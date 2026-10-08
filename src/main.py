import random


def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = 7

    print("welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts.")

    ## while True:
    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess: "))

            if guess < secret_number:
                print("Too low!")

            elif guess > secret_number:
                print("Too high!")

            else:
                print(f"Congratulations! You guessed it in {attempt} attempts!")
                return

        except ValueError:
            print("Please enter a valid number.")
    print(f"Game over! The number was {secret_number}.")

if __name__ == "__main__":
    play_game()                   