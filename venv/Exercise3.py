'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
'''

inputnum = int(input("Please enter a number: "))
divisorlist = []
print(range(1, inputnum+1)) #checking

for i in range(1, inputnum+1):
    if i == 1  or i == inputnum:
        continue              # 1 divides every number and thus ignoring
    elif inputnum % i == 0:
        divisorlist.append(i)
    else:
        continue
print(divisorlist)
