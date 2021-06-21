# Chiamaka Ugbaja
# 1772427

import csv
file = input()  # user input for the file
multiples = {}  # stores the words & its repeat count in this dictionary

with open(file, 'r') as csv_file:  # makes the file readable in the program
    read = csv.reader(csv_file)
    for row in read:  # goes through the row of the file
        for i in row:  # looks for work in the dictionary
            if i not in multiples.keys():
                multiples[i] = 1
            else:  # accounts for repeats of words
                multiples[i] += 1

for i in multiples.keys():  # prints result
    print(i + " " + str(multiples[i]))
