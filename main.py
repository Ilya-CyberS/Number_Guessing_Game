"""number guessing game"""
import random


def start():
    print("Hello to number guessing game")
    print("The computer chooses a random number, and you have to find it.")
    print(f"Good Luck, {name.capitalize()}.", end="\n\n")


def computer():
    comp_number = random.randint(1, 100)

    return comp_number


def user_num():
    global count

    print(f"guess number {count}")

    try:
        user = int(input("take a guess: "))
        print()

    except ValueError:
        print("please enter a valid number:")
        user = user_num()

    while user > 100 or user < 1:
        user = int(input("again, only between 1 and 100: "))
        print()

    return user


def win_low_high(comp, guess):
    global playing
    global count

    if comp == guess:
        print("wow, you found it")
        print(f"the number was {comp}", end="\n\n")
        print(f"you guessed it in {count} attempts")

        play_again()

    elif comp > guess:
        print("your number is low!", end="\n\n")

    elif comp < guess:
        print("yo your too high!", end="\n\n")


def play_again():
    global playing
    print("do you wanna play again?")
    again = input("Y/N? ")

    if again == "y" or again == "Y":

        playing = True

    elif again == "N" or again == "n":
        print("see you soon later.")
        playing = False

    return None


playing = True
count = 0

def game():
    global count

    comp_num = computer()

    while playing and count < 7:
        count += 1
        guess = user_num()
        win_low_high(comp_num, guess)
    else:
        print("you lost. you can not guess more than 7 times.")


name = input("Enter your name? ")

start()
game()