'''
Write a program (function!) that takes a list and returns a new list
that contains all the elements of the first list minus all the duplicates.
Extras:
Write two different functions to do this - one using a loop and constructing
a list, and another using sets.
'''

userinput = input("Enter a list of numbers with spaces between numbers: ")
newlist = userinput.split(' ')
for i in range(len(newlist)):
    newlist[i] = int(newlist[i])
setA = setB = set(newlist)
print(setA.union(setB))

# Using loop iteration
tmp = []
for i in newlist:
    if i not in tmp:
        tmp.append(i)
print(tmp)

