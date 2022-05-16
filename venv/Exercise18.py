'''
Given two .txt files that have lists of numbers in them,
find the numbers that are overlapping. One .txt file has a
list of all prime numbers under 1000, and the other .txt file
has a list of happy numbers up to 1000.
'''
primefileread = []
with open('C:\\Users\\sraba\\OneDrive\\Documents\\Srabasti\\LinkedIn_Learning\\primes.txt') as primefile:
    line = primefile.readline()
    while line:
        primefileread.append(int(line))
        line = primefile.readline()

happyfileread = []
with open('C:\\Users\\sraba\\OneDrive\\Documents\\Srabasti\\LinkedIn_Learning\\happy.txt') as happyfile:
    line = happyfile.readline()
    while line:
        happyfileread.append(int(line))
        line = happyfile.readline()

countoverlap = []
for elem in primefileread:
    if elem in happyfileread:
        countoverlap.append(elem)

print(countoverlap)