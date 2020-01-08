#benjamin vielstich
#guess the number game
#10/28/2018

import random


rmin = 1
rmax = 10
mtrys = 5



            

def get_num_in_range(rmin,rmax):
    while True:
        guess = input("what is your guess")
        if guess.isdigit():
            guess = int(guess)
            if guess >= rmin and rmax:
                return guess
    print("not a good value")

def play_guess_my_number(mtrys, rmin, rmax):
    x = random.randint(rmin, rmax)
    trys = 0
    guess = get_num_in_range(rmin, rmax)
    trys += 1
    while trys != mtrys and x != guess:
        
        if guess > x:
            print("guess lower")
        else:
            print("guess higher")
        guess = get_num_in_range(rmin, rmax)
        trys += 1
    if guess == x:
        print("you won!!!")
    else:
        print("you lose")

def options(gamemode,rmin,rmax,mtrys):
    options = str.format("""
                        {} mode

                        1. Easy mode
                        2. Normal mode
                        3. Hard mode
                        4. Custom""",str(gamemode))
    print(options)
    ochoice =int(input())
    if ochoice == 1:
        gamemode = "Easy"
        rmin = 1
        rmax = 10
        mtrys = 5
        play_guess_my_number(mtrys, rmin, rmax)
    if ochoice == 2:
        gamemode = "Normal"
        rmin = 1
        rmax = 15
        mtrys = 4
        play_guess_my_number(mtrys, rmin, rmax)
    if ochoice == 3:
        gamemode = "Hard"
        rmin = 1
        rmax = 20
        mtrys = 3
        play_guess_my_number(mtrys, rmin, rmax)
    if ochoice == 4:
        rmin = input("what is the minimum number")
        rmax = input("what is the largest number")
        mtrys = input("how many tries")
        play_guess_my_number(mtrys, rmin, rmax)
    

def menu():   
    gamemode = "easy"
    menu = str.format("""
                         Guess the number

                         {} mode

                                 Options
                                 
                         1. Play game
                         2. Options
                         3. Quit""",str(gamemode))
    while True:
        print(menu)
        choice = input()
        if int(choice) == 1:
            play_guess_my_number(mtrys,rmin,rmax)
        if int(choice) == 2:
            options(gamemode,rmin,rmax,mtrys)
            

menu()
