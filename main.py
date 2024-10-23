import random


def number_guessing_game():
    # Step 1: Generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    # Step 2: Initialize the guess counter
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    # Step 3: Start the guessing loop
    while True:
        try:
            # Step 4: Ask the player to input a guess
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increment the number of attempts

            # Step 5: Compare the guess with the random number
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                # Correct guess
                print(f"Congratulations! You guessed the correct number {random_number} in {attempts} attempts.")
                break  # End the loop when the correct number is guessed
        except ValueError:
            # Handle the case where the input is not an integer
            print("Please enter a valid number.")


# Call the function to start the game
number_guessing_game()
