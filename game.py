import random

number = random.randint(1, 25)

for attempt in range(5):
    guess = int(input("Guess a number between 1 and 25: "))

    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print("Correct!")
        break
else:
    print("Out of guesses. The correct number was", number)
