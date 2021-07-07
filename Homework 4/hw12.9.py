# Chiamaka Ugbaja
# 1772427

info = input().split()  # splits the input by space
first_name = info[0]
while first_name != '-1':  # as long as the list is no exited (-1) then it will run the program
    try:
        age = int(info[1]) + 1  # incremented age to the second element in info
    except ValueError:
        age = 0 # if value is not a single word the the age output is 0 (the corrected print)
    print('{} {}'.format(first_name, age))

    info = input().split()
    first_name = info[0]
