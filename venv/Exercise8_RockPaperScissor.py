'''
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner,
and ask if the players want to start a new game)
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock
'''

playerA = input("Player A, enter either rock, paper or scissor: ")
playerB = input("Player B, enter either rock, paper or scissor: ")

#Clumsy way of writing the code as 9 different comparisons have to be made. Think of another method
if playerA == 'rock' and playerB == 'rock':
        print("Game is a draw")
if playerA == 'rock' and playerB == 'paper':
        print("Player B wins as she has {}".format(playerB))
if playerA == rock and playerB == 'scissor':
        print("Player A wins as she has {}".format(playerA))
#Clumsy way of writing the code. Think of another method

# CODE IS NOT COMPLETED. I GOT BORED!!!