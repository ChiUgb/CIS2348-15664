# Chiamaka Ugbaja
# coding problem 1

print('Birthday Calculator\nCurrent Day')
cmonth = int(input('Month: '))
cday = int(input('Day: '))
cyear = int(input('Year: '))

print('Birthday')
bmonth = int(input('Month: '))
bday = int(input('Day: '))
byear = int(input('Year: '))

years = cyear - byear - 1
if bmonth < cmonth: # checks month to see if birth month has passed in order to add a year
    years = years + 1
elif bmonth == cmonth:
    if bday < cday:
    # this assures that if current month and birth month are equal then look at days to assure it passed birth day in order to at a year
        years = years + 1
if cmonth == bmonth and cday == bday: # check if months and days match for birthday prompt
    print('Happy Birthday!')
print('You are', years, 'years old.')
