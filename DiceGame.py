import random
while True:
    print('''1. roll the dice       2. exit''')
    user = int(input("Please enter a key\n"))
    if user==1:
        number = random.randint(1,6)
        print(number)
    else:
        break