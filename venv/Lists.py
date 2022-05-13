#The following are lists:
fruits = ["apples", "pears", "peaches"]
years = [3, '1998', 2.5, 987, '1994']
print(fruits, years)

#Various Python Methods
fruits.append("oranges")
print(fruits)

fruits.extend(years)
print(fruits)

fruits.remove("apples")
print(fruits)

fruits.pop(0)  #removes the item at index 0
print(fruits)

fruits.pop(-1)
print(fruits)

numbers = [100, -1, -10, 0, 2.5, 6, 4, 8, 9, 10]
numbers.sort()
print(numbers)

print(1000 in numbers)
print('apple' in fruits)
print(fruits.count('peaches'))
fruits.extend(['peaches', 'peaches', 'peaches'])
print(fruits.count('peaches'))
print(fruits.index('peaches'))