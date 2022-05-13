fruits = ["apples", 'oranges', 'grapes', 'cherries', 'pears']
for fruit in fruits:
    print("I love eating "+fruit)

for number in range(1,11): #Given a starting and a ending number
    print (number)

for number in range(1,100,2): #Given a starting, ending and a step number
    print(number)


tempF = 40
while tempF > 32:
    print('The temperature is {} degree Fahrenheit'.format(tempF))
    tempF -= 1
    if tempF == 33:
        break

for number in range(1,20):
    #print(number % 3)
    if (number % 3) == 0:
        print("We are skipping all numbers divisible by 3")
        continue
    print("The number is {}".format(number))

for number in range(1,20):
    if number%3 == 0:
        pass
    else:
        print("The number is {}".format(number))