'''
Ask the user for a number and determine whether the number is prime or not
'''
num = int(input("Enter a number: "))
a = [div for div in range(2,num) if num%div == 0]

def prime(a):
    if len(a) >=1:
        print("The number is not a prime")
    else:
        print("The number is a prime")

prime(a)

