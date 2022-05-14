'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''

inputstr = input("Enter a string: ")
reverse_inputstr = inputstr[::-1]
if inputstr == reverse_inputstr:
    print("This is a palindrome and the string is {}".format(inputstr))
else:
    print("This is not a palindrome")