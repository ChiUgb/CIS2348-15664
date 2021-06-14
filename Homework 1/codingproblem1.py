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
if bmonth < cmonth:
    years = years + 1
elif bmonth == cmonth:
    if bday < cday:
        years = years + 1
if cmonth == bmonth and cday == bday:
    print('Happy Birthday!')
print('You are', years, 'years old.')
