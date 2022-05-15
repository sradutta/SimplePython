'''
Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the
user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly
in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they
have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user
makes throughout teh game and tell the user at the end.
'''
import random
import math

def randgenmethod1():
    rand1 = random.randrange(1000, 9999,1)
    print(rand1)

#Another method
def randgenmethod2():
    seed = '0123456789'
    rand2 = ''
    for i in range(4):
        rand2 = rand2 + seed[math.floor(random.random()*10)] #seed is a string; num is a string; random.random() generates a number between 0 and 1
    print(rand2)

def compare(userinput):
    if len(userinput) < 4 or len(userinput) > 4:
        print("You have not guessed a 4 digit number. You have guessed {}".format(userinput))
        print("The game has ended as a 4-digit number was not guessed by a player")

    #randnum = str(randgenmethod1())
    #randnum = str(randgenmethod2())
    randnum = str(3135)     # Testing

    if randnum == userinput:
        print("Congratulations! You have won and the game is over")
        quit()

    cow = 0
    bull = 0
    for i in range(4):
        if userinput[i] in randnum:
            pos = randnum.find(userinput[i])
            if pos == i:
                cow += 1
            else:
                bull += 1
    print("The number of cows is {} and the number of bulls is {}".format(cow, bull))

goon = True
while goon:
    userinput = input("Enter a 4 digit number: ")
    compare(userinput);
    ans = input("Do you want to quit? Y/N: ")
    if ans == 'Y':
        goon = False
    else:
        goon = True