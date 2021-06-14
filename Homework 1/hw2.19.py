# Chiamaka Ugbaja
# hw 2.19

lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave_nec = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))
print()
print('Lemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave_nec), 'cup(s) agave nectar\n')

servings2 = float(input('How many servings would you like to make?\n'))
print()
print('Lemonade ingredients - yields', '{:.2f}'.format(servings2), 'servings')
print('{:.2f}'.format(servings2 * (2/6)), 'cup(s) lemon juice')
print('{:.2f}'.format(servings2 * (16/6)), 'cup(s) water')
print('{:.2f}'.format(servings2 * (2.5/6)), 'cup(s) agave nectar')

print()
print('Lemonade ingredients - yields', '{:.2f}'.format(servings2), 'servings')
print('{:.2f}'.format((servings2 * (2/6))/16), 'gallon(s) lemon juice')
print('{:.2f}'.format((servings2 * (16/6))/16), 'gallon(s) water')
print('{:.2f}'.format((servings2 * (2.5/6))/16), 'gallon(s) agave nectar')
