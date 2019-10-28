# Gavin Howard
# 10/22/19
# Craps

import random


def roll_dice():
    rolled_num = random.randint(2, 12)
    print("You rolled", rolled_num)
    return rolled_num


def create():
    print("What would you like your initial bankroll to be?")
    funds = int(input("> "))
    if funds < 0:
        print("That's an invalid entry, please try again.")
    print(f"Your initial bankroll is {funds}")
    return funds


def play_game():
    funds = create()
    print("How much would you like to bet?")
    bet = int(input("> "))
    while bet < 0 or bet > funds:
        print("Please enter a valid bet.")
        print("How much would you like to bet?")
        bet = int(input("> "))
    roll = roll_dice()
    if roll == 7 or roll == 11:
        print("You have won! Congratulations!")
        funds = funds + bet
        print(f"Your new bankroll is {funds}")
    elif roll == 2 or roll == 3 or roll == 12:
        print("You have lost!")
        funds = funds - bet
        print(f"Your new bankroll is {funds}")
    else:
        print(f"You have made point! Your point is {roll}, and you must keep rolling until you roll {roll} again or you roll a 7!")
        point = roll
        roll = roll_dice()
        while roll != point and roll != 7:
            roll = roll_dice()
        if roll == point:
            print("You have made point! You win!")
            funds = funds + bet
            print(f"Your new bankroll is {funds}")
        elif roll == 7:
            print("You rolled a 7! You lose!")
            funds = funds - bet
            print(f"Your new bankroll is {funds}")
    print("Would you like to play again? Y or N.")
    answer = input("> ")
    if answer is "Y":
        play_game()
    elif answer is "N":
        print("Thanks for playing!")
    else:
        print("Please enter a valid response. Y or N.")


print(play_game())
