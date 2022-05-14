'''
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains
only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
'''
import random

input1 = input("Enter a list of numbers separated by spaces: ")
input2 = input("Enter anoter list of numbers that is of different size than the already input: ")
inputlist1 =  input1.split(' ')
inputlist2 = input2.split(' ')
for i in range(len(inputlist1)):
    inputlist1[i] = int(inputlist1[i])
for i in range(len(inputlist2)):
    inputlist2[i] = int(inputlist2[i])

def common_members(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    if(len(set1.intersection(set2))>0):
        print(set1.intersection(set2))
    else:
        print("No common elements")

common_members(inputlist1, inputlist2)

# This code generates two random sets and then find the intersections
list1 = [random.randrange(1, 20, 1) for i in range(10)]
list2 = [random.randrange(1, 30, 1) for i in range(20)]
print(list1)
print(list2)
common_members(list1, list2)