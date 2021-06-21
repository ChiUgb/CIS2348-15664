# Chiamaka Ugbaja
# 1772427

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

solution = False # establishes the result false until proven true by the for loop

for x in range(-10, 11): # the first number in the list of number the user inputs with the range from -10 to 10
    for y in range(-10, 11): # takes second number within the same range
        if a * x + b * y == c and d * x + e * y == f: # plug the qualifying number into the equation
            print(x, y) # prints results
            solution = True

if not solution: # if numbers inputted are not within the range -10 through 10
    print("No solution")