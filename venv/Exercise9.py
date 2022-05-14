'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they
guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
import random


gameon = True
while(gameon):
    randnum = random.randrange(1, 10)
    guessnum = int(input("Guess the number that was generated between 1 and 9: "))
    if randnum == guessnum:
        print("You have guessed the number exactly. The random number is {}".format(randnum))
    if randnum > guessnum:
        print("You  have guessed a lower number. The random number is {}".format(randnum))
    if randnum < guessnum:
        print("You  have guessed a higher number. The random number is {}".format(randnum))
    str = input('If you want to quit, type exit else hit enter to continue: ')
    if str == 'exit':
        gameon = False

