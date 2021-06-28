# Chiamaka Ugbaja
# 1772427

team_dict = {}  # empty dictionary for start up
i = 1  # starting index of dictionary
count = 1

for i in range(1, 6):  # repeats prompt 6 times
    j_num = int(input('Enter player {}\'s jersey number:\n'.format(i)))
    rating = int(input('Enter player {}\'s rating:\n'.format(i)))
    print()

    if 0 > j_num > 99 and 0 > rating > 9:  # check for the validity of inputs
        print('invalid entry')
        break
    else:
        team_dict[j_num] = rating

print("ROSTER")  # prints the output of input jersey num and rating
for j_num, rating in sorted(team_dict.items()):
    print("Jersey number: %d, Rating: %d" % (j_num, rating))


option = ''  # created menu option for input
while option.upper() != 'Q':  # shows menu and loops until user quits
    print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\n'
          'r - Output players above a rating\no - Output roster\nq - Quit\n')

    option = input('Choose an option:\n')

# for option a, it will add items to dictionary once j_num and rating are received
    if option == 'a':
        j_num = int(input('Enter a new player\'s jersey number:\n'.format(i)))
        rating = int(input('Enter the players\'s rating:\n'.format(i)))
        team_dict[j_num] = rating

# option d will delete item from dictionary
    elif option == 'd':
        j_num = int(input('Enter a jersey number:\n'))
        if j_num in team_dict.keys():
            del team_dict[j_num]

# option u will update player rating
    elif option == 'u':
        j_num = int(input('Enter a jersey number:\n'))
        if j_num in team_dict.keys():
            rating = int(input('Enter a new rating for player:\n'))
            team_dict[j_num] = rating

# option r will print all players with a specific ratings
    elif option == 'r':
        rating_input = int(input('Enter a rating:\n'))
        print('ABOVE {}'.format(rating_input))
        for j_num, rating in sorted(team_dict.items()):
            if rating > rating_input:
                print("Jersey number: %d, Rating: %d" % (j_num, rating))

# option o will print the entire roster with j_num and rating
    elif option == 'o':
        print("ROSTER")
        for j_num, rating in sorted(team_dict.items()):
            print("Jersey number: %d, Rating: %d" % (j_num, rating))
