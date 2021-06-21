# Chiamaka Ugbaja
# 1772427
password = input()  # takes the password
new_password = ""

for letter in password: # look at each element in the password and replaces it with the required character
    if letter == 'i':
        new_password = new_password + '!'

    elif letter == 'a':
        new_password = new_password + '@'

    elif letter == 'm':
        new_password = new_password + 'M'

    elif letter == 'B':
        new_password = new_password + '8'

    elif letter == 'o':
        new_password = new_password + '.'

    else:
        new_password = new_password + letter # for every element that does not need to be changed just add it to the new_password

new_password = new_password + "q*s" # after the loop checking and making the replaces, amend this all the new_password

print(new_password)
