'''
Write a function that takes an ordered list of numbers
(a list where the elements are in order from smallest to
largest) and another number. The function decides whether
or not the given number is inside the list and returns (then prints)
an appropriate boolean.
'''

userinput = input("Enter a list of number separated by spaces: ")
usernum = input("Enter another single number: ")

if str(usernum) in userinput:
    print("Yes, the single number, {}, is present in the list of numbers {}.".format(usernum,userinput))