import random

print("""
***********************************************
* Welcome to the Guessing Game and Good Luck! *
*     Now take a number between 0 and 100     *
***********************************************
""")

def user_num():
    while True:
        try:
            u_num = int(input("Please enter your tip : "))

            if u_num <= 0 or u_num > 100:
                print("choose a number from 1 to 100")
                continue
            return u_num
            break

        except ValueError:
            print("Try again! Only whole numbers are allowed!")


def check(ran):
    count = 0

    while True:

        if count == 3:
            print("ijfojdf")
            break

        else:
            user_number = user_num()

            if ran == user_number:
                print("""
                ***************
                * YOU GOT IT! *
                ***************
                """)
                break

            elif ran < user_number:
                count += 1
                print("try again! Maybe a little lower!")
                print("You are at attempt", count, "of 3")


            elif ran > user_number:
                count += 1
                print("try again! Maybe a little higher!")
                print("You are at attempt", count, "of 3")





ran = random.randint(0, 2)
print(ran) #nur für test
while True:
    check(ran)
    while True:
        repeat = input("Go again?")
        if repeat.upper() == "N":
            print("see you soon!")
            quit()
        elif repeat.upper() != "Y":
            print("please enter Y or N")
        else:
            break





