'''
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
'''

strofnums = input("Enter a list of numbers separated by paces: ")
indexnum = input("Enter the number up to which the list is printed: ")
printlist = []
inputlist = strofnums.split(' ')
for i in range(len(inputlist)):
    inputlist[i] = int(inputlist[i])

if int(indexnum) in inputlist:
    for i in range(len(inputlist)):
        if inputlist[i] < int(indexnum):
            printlist.append(inputlist[i])
        else:
            continue
else:
    print("The number is not in the list of numbers input by the user")
print(printlist)

print(inputlist)        #for checking
print(type(inputlist))  #for checking