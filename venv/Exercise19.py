'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old), except use f-strings instead of the + operator to
print the resulting output message.
'''
from datetime import date


name = input("What is your name? ")
age = int(input("What is your age? "))
today = date.today()
year = today.year  +(100-age)
print(f"Your name is {name} and you will turn 100 years old in the year {year}")