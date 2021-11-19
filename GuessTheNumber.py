import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("Guess the number"))
    if user == number:
        print("Hurray!")
        print(f"You guessed the correct number, it's {number}")
        break
if user != number:
    print(f"Incorrect guess, the number is {number}")