import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 3
    
    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it correctly.")
    
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        
        if guess == number_to_guess:
            print("You won!")
            return
        elif guess > number_to_guess:
            print(f"The number you guessed is greater than the number. The number is: {number_to_guess}")
        else:
            print(f"The number you guessed is less than the number. The number is: {number_to_guess}")
    
    print("You've used all your attempts. Game over!")

# Run the guessing game
guessing_game()
