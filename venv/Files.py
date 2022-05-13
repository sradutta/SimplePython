with open('C:\\Users\\sraba\\OneDrive\\Desktop\\Database\\ConsoleDates.csv','rU') as inputfile:
    header = next(inputfile)
    for line in inputfile:
        line = line.rstrip().split(',')
        print(line)


