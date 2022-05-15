'''
Given a .txt file that has a list of a bunch of names,
count how many of each name there are in the file, and
print out the results to the screen.
'''

count = {}
with open("C:\\Users\\sraba\\OneDrive\\Documents\\Srabasti\\LinkedIn_Learning\\names.txt") as fname:
    line = fname.readline()
    while line:
        line = line.strip()  #reads the string and get rid of all trailing spaces including \n
        if line in count:
            count[line] += 1
        else:
            count[line] = 1
        line = fname.readline()
print(count)