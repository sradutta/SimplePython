"""
Write a program (using functions!) that asks the user for a
long string containing multiple words. Print back to the user
the same string, except with the words in backwards order
"""

userinput = input("Enter a long string containing multiple words: ")
strlist = userinput.split(' ')
rvsstr = strlist[::-1]
str = ' '.join([str(item) for item in rvsstr])
print(str)

# Another method:
mystr = ' '
for str in rvsstr:
    mystr += ' '+str
print(mystr)
