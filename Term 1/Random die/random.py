#benjamin vielstich
#9/25/2019
#random numbers
import random



def roll():
    die = random.randint(1,6)
    print(die)

def die_roll(rolls):
    for i in range(int(rolls)):
        roll()

rolls = input("how many times do you want to roll?")

die_roll(rolls)

input()
