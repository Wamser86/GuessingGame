import random

def random_number():
    return random.randint(0, 101)

def user_nums():
    while True:
        try:
            num = int(input("Please enter your tip : "))
            if num <= 0 or num > 100:
                print("choose a number from 0 to 100")
            break

        except ValueError:
            print("Try again")

def check():
    if random_number() == user_nums():
        print("Correct!")

user_nums()