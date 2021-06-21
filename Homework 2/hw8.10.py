# Chiamaka Ugbaja
# 1772427

user_input = input()
no_spaces = ""

for i in user_input:  # look through each letter and adds it to new variable, no_spaces
    if i != ' ':
        no_spaces += i

backward = ""
for i in no_spaces:  # evaluates the phrase without space (no_spaces) to see if it match with backwards
    backward = i + backward
if no_spaces == backward:  # if everything matched
    print(user_input + " is a palindrome")
else:  # discrepancies will result in no palindrome
    print(user_input + " is not a palindrome")