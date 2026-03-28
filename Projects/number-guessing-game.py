import random

number = random.randint(1,1000)
guess = (int(input("Guess a number between 1 and 1000:")))
while guess != number:
    if guess < number:
        guess = (int(input("Too low:")))
    if guess > number:
        guess = (int(input("Too high:")))
print("You won!")