import random

guessesTaken = 0

myName = input("Hello! What is your name? ")

number = random.randint(1, 20)
print("Well, " + myName + ", I am thinking of a number between 1 and 20.")

for guessesTaken in range(6):
    guess = int(input("Take a guess: "))

    if guess < number:
        print("Your guess is too low")

    if guess > number:
        print("Your guess is too high")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guess my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')