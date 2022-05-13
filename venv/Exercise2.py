'''
The exercise comes first (with a few extras if you want the extra challenge or want to
spend more time), followed by a discussion. Enjoy!
Ask the user for a number. Depending on whether the number is even or odd, print out
an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''
n = int(input("Enter a number: "))
if n%4 == 0:
    print("The number is a multiple of 4")
elif n%2 == 0:
    print("You have entered an even number. The even number is {}".format(n))
else:
    print("You have entered an odd number. The odd number is {}".format(n))

check = int(input("Enter a 2nd number: "))
if n%check == 0:
    print("The 2nd number divides the 1st number evenly")
else:
    print("The 2nd number does not divide the 1st number evenly")

