'''
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25]) and makes
a new list of only the first and last elements
of the given list.
'''

userinput = input("Enter a list of number separated by spaces: ")
splitinput = userinput.split(' ')
for i in range(len(splitinput)):
    splitinput[i] = int(splitinput[i])

newlist = []
def firstlastnum(splitinput):
    newlist.append(splitinput[0])
    newlist.append(splitinput[-1])
    print(newlist)

firstlastnum(splitinput)

