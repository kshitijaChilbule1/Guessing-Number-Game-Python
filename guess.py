import random

random_number = random.randrange(1, 10)
guess = None
max_guesses = 3
guess_count = 0

while(guess != random_number and guess_count <= max_guesses):
    guess = int(input("Enter number between 1 to 10  :  "))
    guess_count += 1

    if guess == random_number:
        print("congratulations! you won!")
        break
    elif guess > random_number:
        print("Your Guess is too High, try again!")
    elif guess < random_number:
        print("Your Guess is too Low, try again!")
print("GoodBye...")