'''
Write a program that asks the user how many Fibonnaci
numbers to generate and then generates them. Take this
opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers
in the sequence to generate.(Hint: The Fibonnaci seqence
is a sequence of numbers where the next number in the sequence
is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

def generateFibo(n):
    if n <= 1:
        return n
    else:
        return (generateFibo(n-1) + generateFibo(n-2))

n = int(input("How many Fibonacci numbers you want: "))
if n <= 0:
    n = int(input("Enter a positive number: "))
else:
    for i in range(n):
        print(generateFibo(i), end=" "),
    