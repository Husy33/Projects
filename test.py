import random

def guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100")
    
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        if attempts > 10:
            print("Game over")
            break
        
        if guess < number:
            print("Too low!")
            print(f"Attempts used: {attempts}/10")
        elif guess > number:
            print("Too high!")
            print(f"Attempts used: {attempts}/10")
        else:
            print(f"Correct! You got it in {attempts} attempts")
            break

guessing_game()