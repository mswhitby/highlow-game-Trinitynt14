import random
random_num = random.randint(1,100)


def highlow():
    guess = int(input("pick a number between 1 and 100: "))
    while guess != (random_num):
        guess = int(input("comfirm "))
        if guess > (random_num):
            Again = int(input("try a lower number! "))
        else:
            if guess < (random_num):
                now = int(input("try a higher number! "))
        if guess == (random_num):
            print("You got it right!")

highlow()
